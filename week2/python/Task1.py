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
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian