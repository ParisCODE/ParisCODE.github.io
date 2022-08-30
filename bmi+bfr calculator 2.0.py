import time
import easygui as g
def BMI_BFR():
    height = float(g.enterbox("请输入身高(m)："))
    weight = float(g.enterbox("请输入体重(kg)："))
    age = int(g.enterbox("请输入年龄:"))
    sex = g.buttonbox("请选择性别：", choices=["男", "女"])
    if sex == "男":
        sex = 1
    else:
        sex = 0
    #获取所需的数据
    BMI = (weight / (height * height))
    BFR = 1.2 * (round(BMI, 1)) + 0.23 * age - 5.4 - 10.8 * sex
    #获取的数据进行计算
    text = "你的BMI为:" + str(round(BMI, 1)) + "\n"
    if round(BMI, 1) <= 18.5:
        g.msgbox(text+"你的身材：偏瘦")
    elif 18.5 < round(BMI, 1) <= 24.0:
        g.msgbox(text+"你的身材：正常")
    elif 24.0 < round(BMI, 1) <= 28.0:
        g.msgbox(text+"你的身材：超重")
    elif round(BMI, 1) > 28.0:
        g.msgbox(text+"你的身材：肥胖")
    else:
        g.msgbox("计算错误，请重新输入")
    text = "你的体脂率BFR为" + str(round(BFR, 2)) + "\n"
    if round(BFR, 1) < 10.0:
        g.msgbox(text+"体脂率不足")
    elif 10.0 < round(BFR, 1) <= 20.0:
        g.msgbox(text+"体脂率正常")
    elif round(BFR, 1) > 20:
        g.msgbox(text+"体脂率偏高")
    else:
        g.msgbox("计算错误，请重新输入")
while True:
    btn=g.buttonbox(msg="请选择：",choices=["计算BMI,BFR","quit"])
    if btn == "quit":
        break
    BMI_BFR()
