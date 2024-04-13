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

# Testing 
print(get_number(1))  #  print 4
print(get_number(5))  #  print 15
print(get_number(10))  # print 25
print(get_number(30))  # print 70
