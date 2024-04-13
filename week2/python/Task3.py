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

# 測試
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
