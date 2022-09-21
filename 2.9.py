m=input("month:")
d=int(input("date:"))
if(d>1 and d<=31):
    if(m=='april'or m=='may'):
        print("sumer")
    elif(m=='june'and d<=20):
        print("sumer")
    elif(m=='march'and d>=20):
        print("sumer")
    elif(m=='july'or m=='aug'):
        print("spring")
    elif(m=='june'and d>=21):
        print("spring")
    elif(m=='september'and d<=21):
        print("spring")    
    elif(m=='october'or m=='nov'):
        print("fall")
    elif(m=='september'and d>=22):
        print("fall")
    elif(m=='december'and d<=21):
        print("fall")
    elif(m=='february' or m=='jan'):
        print("winter")
    elif(m=='march'and d<=19):
        print("winter")
    elif(m=='december' and d>=20):
        print("winter")
else:
    print("wrong input")
