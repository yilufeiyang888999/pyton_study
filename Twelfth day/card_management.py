# -*- coding:UTF-8 -*-
card_info = []  # 定义一个列表用来存储名片


def print_menu():
    """"完成菜单打印"""
    print("*" * 50)
    print("  名片管理系统")
    print("1.添加一个新名片：")
    print("2.删除一个名片：")
    print("3.更改一个名片：")
    print("4.查找一个名片")
    print("5.显示所有名片")
    print("6.保存信息")
    print("7.退出系统")
    print("*" * 50)


print_menu()


# 1.打印功能提示
def add_new_card_infor():
    """"完成添加一个新的名片"""
    new_name = input("请输入新名片的名字:")
    new_phone = input("请输入新的电话号码:")
    new_mail = input("请输入新的E-mail:")
    new_addr = input("请输入新的地址:")
    new_info = {}  # 定义一个新的字典，用来存储一个新的名片
    new_info['name'] = new_name
    new_info['phone'] = new_phone
    new_info['mail'] = new_mail
    new_info['addr'] = new_addr
    global card_info
    card_info.append(new_info)  # 定义一个列表，将字典添加到列表中。
    print(card_info)


def del_card_info():
    global card_info
    while True:
        del_name = input("请输入你要删除的名字:")
        find_2 = 0
        for line in card_info:
            if line['name'] == del_name:
                find_2 = 1
                card_info.remove(line)
                # break
        if find_2 == 1:
            print("已删除！！！")
        else:
            print("你输入的名字不存在！！！")
        print(card_info)
        break


def alter_card_info():
    global card_info
    while True:
        old_name = input("请输入要修改的名字：")
        find_3 = 0
        for line in card_info:
            if line['name'] == old_name:
                Change_Name = input("请输入新的姓名：")
                Change_Phone = input("请输入新的电话：")
                Change_Mail = input("请输入新的邮箱：")
                Change_Addr = input("请输入新的地址:")
                line['name'] = Change_Name
                line['phone'] = Change_Phone
                line['mail'] = Change_Mail
                line['addr'] = Change_Addr
                find_3 = 1
                break
        if find_3 == 1:
            print("已修改！！！")
        else:
            print("你输入的用户不存在！！")
        print(card_info)
        break


def find_card_info():
    global card_info
    find_name = input("请输入你要查询人的名字：")  # 定义一个变量来存储查询输入的名字
    for tmp in card_info:
        if find_name == tmp["name"]:
            print("%s\t%s\t%s\t%s\t" % (tmp['name'], tmp['phone'], tmp['mail'], tmp['addr']))
            find_flang = 1
            break
        else:
            print("查无此人！！！")


def show_card_info():
    global card_info
    print("姓名 电话 邮箱 地址")
    for tmp in card_info:
        print("%s\t%s\t%s\t%s\t" % (tmp['name'], tmp['phone'], tmp['mail'], tmp['addr']))
def save_2_file():
#把添加的信息添加到文件
    f=open("backup.data","w")
    f.write(str(card_info))
def load_infor():
    try:
        global card_info
        f=open("backup.data")
        card_info=eval(f.read()) #不能用list
        f.close()
    except Exception:
        pass
def main():
    #加载之前的数据到程序中
    load_infor()
    while True:
        num = int(input("请输入操作序号1-6："))  # 获取用户输入
        # 根据用户输入来选择相应的功能
        if num == 1:
            add_new_card_infor()
        elif num == 2:  # 删除
            del_card_info()
        elif num == 3:
            alter_card_info()
        elif num == 4:
            find_card_info()
        elif num == 5:
            show_card_info()
        elif num == 6:
            save_2_file()
        elif num==7:
            break
        else:
            print("输入有误，请重新输入！！！")

if __name__ =="__main__":
     main()
