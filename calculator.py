import easygui as g
while True:
    Qq=g.buttonbox(msg="what do you want to do?",choices=["calculate","quit"])
    if Qq == "quit":
        break
    f=g.buttonbox(msg="choose one!",choices=["addition","subtraction","multiplication","division"])
    if f == "addition":
        a1=g.enterbox("what's the 1st addend?")
        a2=g.enterbox("what's the 2nd addend?")
        a1=int(a1)
        a2=int(a2)
        answer=a1+a2
        answerf="the answer is"+" "+str(answer)
        g.msgbox(answerf)
    if f =="subtraction":
        s1=g.enterbox("what's the minuend?")
        s2=g.enterbox("what's the subtrahead?")
        s1=int(s1)
        s2=int(s2)
        answer=s1-s2
        answerf="the answer is"+" "+str(answer)
        g.msgbox(answerf)
    if f =="multiplication":
        m1=g.enterbox("what's the 1st factor?")
        m2=g.enterbox("what's the 2st factor?")
        m1=int(m1)
        m2=int(m2)
        answer=m1-m2
        answerf="the answer is"+" "+str(answer)
        g.msgbox(answerf)
    if f =="division":
        d1=g.enterbox("what's the dividend?")
        d2=g.enterbox("what's the divisor?")
        d1=int(d1)
        d2=int(d2)
        answer=d1-d2
        answerf="the answer is"+" "+str(answer)
        g.msgbox(answerf)
        
    


        
    
