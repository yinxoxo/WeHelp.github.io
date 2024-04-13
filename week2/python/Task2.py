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

#Testing
book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service 
book(consultants, 14, 3, "price") # John