#print("Hello World")
#print("Bye World")

temp = 10

def displaytemp():
    t = int(round(temp))
    if t < 10:
        print("its cold")
    elif t in range(10,23):
        print("Compfhy ")
    elif t >= 23:
        print("HOT")
    else:
        print("error")
    
    
    
displaytemp()


