#-*- coding:UTF-8 -*-
class Person(object):   #创建一个人的类
    def __init__(self,name):
        super(Person, self).__init__()
        self.name=name
        self.gun=None#用来保存枪对象的引用
        self.hp=100
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        #把子弹装到弹夹中
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
    #把弹夹安安装到枪中
        gun_temp.baocun_danjia(dan_jia_temp)
    def naqiang(self,gun_temp):#拿起一把枪
        self.gun=gun_temp
    def __str__(self):
        if self.gun:
            return "%s的血量为%d,他有枪  %s"%(self.name,self.hp,self.gun)
        else:
            if self.hp>0:
                return "%s的血量为%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s 敌人已挂........"%self.name
    def kou_ban_ji(self,diren): #让枪发射子弹打敌人
        self.gun.fire(diren)#枪.开火（敌人）
    def dao_xue(self,sha_shang_li):#根据杀伤力，掉相应的血量
        self.hp-=sha_shang_li

class Gun(object):
    def __init__(self,name):  #创建枪的型号
        super(Gun, self).__init__()
        self.name=name
        self.danjia=None #用来记录弹夹对象的引用
    def baocun_danjia(self,dan_jia_temp):
    # 用一个属性来保存这个弹夹对象的引用
        self.danjia=dan_jia_temp
    def __str__(self):
        if self.danjia:
            return "枪的信息为：%s,%s" % (self.name,self.danjia)
        else:
            return "枪的信息为：%s,这把枪中没有弹夹" % (self.name)
    def fire(self,diren):#枪从弹夹中获取一发子弹，然后这发子弹去击中敌人
        zidan_temp=self.danjia.tanchu_zidan() #弹夹弹出一颗子弹
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:("弹夹中没有子弹了......")



class Danjia():
    def __init__(self,max_num): #创建弹匣,一个弹匣最多可以装多少子弹
        super(Danjia, self).__init__()
        self.max_num=max_num
        self.zi_dan_list=[]#用来记录所有子弹的引用
    def baocun_zidan(self,zi_dan_temp):
        #将这颗子弹保存
        self.zi_dan_list.append(zi_dan_temp)
    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zi_dan_list),(self.max_num))
    def tanchu_zidan(self):#弹出最上面的那颗子弹
        if self.zi_dan_list:
            return self.zi_dan_list.pop()
        else:
            return None

class Zidan():
    def __init__(self,sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li=sha_shang_li  #子弹的杀伤力
    def dazhong(self,diren):#让敌人掉血
        diren.dao_xue(self.sha_shang_li)
def main():
    # 1.创建一个对象为老李
    laoli=Person("老李")
    #2.创建一个对象为枪
    ak47=Gun("AK47")
    #3.创建一个弹匣对象
    dan_jia=Danjia(20)
    #4.创建一些子弹
    for i in range(15):
        zi_dan=Zidan(10)
        #5.老李把子弹安装到弹夹中
        laoli.anzhuang_zidan(dan_jia,zi_dan)
    #6.老李把弹夹安装到枪中
    laoli.anzhuang_danjia(ak47,dan_jia)
    #测试弹夹、枪的信息
    #print(dan_jia)
    #print(ak47)
    #7.老李拿枪
    laoli.naqiang(ak47)
    #测试老李对象
    #print(laoli)


    #8.创建一个敌人
    gebi_laownag=Person("隔壁老王")
    print(gebi_laownag)


    #9老李开枪打敌人
    for i in range(30):
        laoli.kou_ban_ji(gebi_laownag)
        print(gebi_laownag)
        print(laoli)
if __name__ == '__main__':
    main()

#核心思想：一个对象创建出来后，如果另一个对象想使用，只需要在对象里添加一个属性指向那个对象的引用