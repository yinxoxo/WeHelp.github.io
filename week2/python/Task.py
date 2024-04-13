#Test1
def find_and_print(messages, current_station):
# your code here
    #建立捷運綠線地圖，不含支線
    green_line_stations = [
        "Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan", 
        "Beimen","Ximen","Xiaonanmen","Chiang Kai-shek Memorial Hall","Guting","Taipower Building",
        "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"
    ]

    #額外處理小碧潭支線，額外距離+1
    branch_to_main = {"Xiaobitan": ("Qizhang", 1)}

    distances = {}  # 存放每個朋友的站點距離，key=name ,value=距離

    for friend, message in messages.items(): #items()方法，遍歷messages每個鍵值對，將名字放入friend，訊息放入message
        station_found = False #預設為還沒找到車站，接著繼續找
        # 先檢查是否提及『支線』車站
        for branch, (main_station, extra) in branch_to_main.items():
            if branch.lower() in message.lower(): #檢查訊息內有分支車站 #lower將字串都轉成小寫
                station_index = green_line_stations.index(main_station)  # 找出支線所連結的『主站』在綠線裡的位置 #使用index()取出車站索引的值
                distance = abs(station_index - green_line_stations.index(current_station)) + extra #計算好友與主站的距離#abs取絕對值
                distances[friend] = distance #將算好的距離，賦值給好友
                station_found = True #找到車站，不再繼續收尋
                break

        # 再檢查是否提到主線車站
        if not station_found:
            for station in green_line_stations:#檢查訊息內是否有綠線車站
                if station.lower() in message.lower():
                    station_index = green_line_stations.index(station)
                    distance = abs(station_index - green_line_stations.index(current_station))
                    distances[friend] = distance
                    break

    # 找出距離最近的朋友
    if distances:
        nearest_friend = min(distances, key=distances.get) #min找出最小的項目 #key指定要查的資料 #get取得值
        print(nearest_friend)
    else:
        print("No friends found.")
 
   
#朋友及對應位置的字典
messages={
    "Leslie":"I'm at home near Xiaobitan station.", 
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.", 
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Vivian":"I'm at Xindian station waiting for you."
}

#Tesk2
def book(consultants, hour, duration, criteria):

    # 為每個顧問增加一個管理預定時間的列表bookings
    for consultant in consultants:
        if "bookings" not in consultant: #如果顧問還沒有列表bookings這個『鍵』，則新增
            consultant["bookings"] = []

    # 先：找到符合時間要求的顧問
    available_consultants = [] #建立一個空列表，存放預約時間內沒有時間衝突的顧問
    for consultant in consultants:#檢查consultant裡面的每位顧問
        overlapping = False #建立一個表示時間衝突的變數，預設為沒有衝突及代表每顧問都可用
        for booking in consultant["bookings"]: #檢查顧問的bookings內有沒有衝突
            if not (hour + duration <= booking["start"] or hour >= booking["end"]):
                overlapping = True #時間衝突發生時！
                break
        if not overlapping: #如果時間沒有衝突，就將顧問加入available_consultants列表
            available_consultants.append(consultant)

    # 再： 根據標準來排序顧問
    if criteria == "price": #標準是價格 
        #使用sorted() 函數將available_consultants資料進行排序 
        #key參數指定排序的依據 #lambda函數可以定義沒有名稱的函數，lambda參數列表:表達式
        selected_consultant = sorted(available_consultants, key=lambda x: x["price"], reverse=False)#reverse參數控制排序方向，False為小到大
    elif criteria == "rate": #標準是評價
        selected_consultant = sorted(available_consultants, key=lambda x: x["rate"], reverse=True)
    else:
        print("Invalid criteria")
        return

    # 決定預定哪個顧問或"No Service"
    if available_consultants and selected_consultant: #如果有符合時間需求的顧問以及依標準排序好的顧問列表
        selected_consultant = selected_consultant[0]  # 選擇排序的第一位顧問
        selected_consultant["bookings"].append({"start": hour, "end": hour + duration})
        print(f"{selected_consultant['name']}") #f""將字符串格式化
    else:
        print("No Service")   

#顧問名單-字典
consultants=[
    {"name":"John", "rate":4.5, "price":1000}, 
    {"name":"Bob", "rate":3, "price":1200}, 
    {"name":"Jenny", "rate":3.8, "price":800},
]

#Test3
def func(*data):
    # 建立名字-中間名的字典
    middle_names = {}
    # 找出中間名字
    for name in data:
        length = len(name)
        # 根據名字長度找中間名字
        if length == 2 or length == 3 :
            middle_name = name[1]  # 如果是兩字、三字名，中間字是第二個
        elif length == 4 or length==5:
            middle_name = name[2]  # 如果四字名，中間字是第三個
      

        # 將中間名和對應的完整姓名存放在字典中
        if middle_name not in middle_names: #檢查『中間名』是否已存在字典中
            middle_names[middle_name] = []  #沒有的話新增一個『中間名』作為key
        middle_names[middle_name].append(name) #用.append()方法（在列表尾端中加一筆新資料），即為將name加入『中間名』key所對應的『值』列表

    # 尋找只有一個的中間名，並找出對應的完整姓名 
        #使用字典的.values()方法，叫出middle_names 字典中所有的值
        #使用列表推導式[expression for item in iterable if condition]
    unique_name = [names[0] for names in middle_names.values() if len(names) == 1] #用names[0]提出列表出的第一筆資料，若止血names就會提出列表型態的資料

    # 打印结果
    if unique_name:
        print(unique_name[0])
    else:
        print("沒有")

#Test4
def get_number(index):
    cycle_length = 3  #數列為+4+4-1 三個一循環，視為一週期
    cycles_completed = index // cycle_length  # 完成的周期数
    remainder = index % cycle_length  #資料在週期中的哪個位置

    value = cycles_completed *7 #跑完一個週期會+7

    if remainder == 1: #資料在週期的第一個位置時+4
        value += 4  
    elif remainder == 2: #資料在週期的第二個位置時+8
        value += 8 

    return value

#print
print("===Task 1===")
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian
print("===Task 2===")
book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service 
book(consultants, 14, 3, "price") # John
print("===Task 3===")
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
print("===Task 4===")
print(get_number(1))  #  print 4
print(get_number(5))  #  print 15
print(get_number(10))  # print 25
print(get_number(30))  # print 70