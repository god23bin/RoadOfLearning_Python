info = {'1':['601398','工商银行',5.51], '2':['000001','平安银行',8.94], \
        '3':['601939','建设银行',6.89], '4':['601328','交通银行',5.61]}
no = input("请输入编号：")

while no in info:
    print("股票代码：%s, 股票名称：%s, 买入价： %.2f" %(info[no][0], info[no][1], info[no][2]))
    no = input("请输入编号：")
else:
    print("无查询结果")