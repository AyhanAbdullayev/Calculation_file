from datetime import date 
from os.path import exists

if not exists("table.txt"):
    with open("table.txt","w") as f:
        f.write("Function name   |Worked Time|Arguments|Operation|Result\n")

def calculation(func):
    def inner(a,oper,b):
        try:
            result = func(a,oper,b)
            result = str(result)
        except ZeroDivisionError as Z:
            result = str(Z)
        a_name = f"{func.__name__:<16}"
        Worked_time = f"{date.today()}"
        Operation = oper
        a = str(a)
        b = str(b)
        with open("table.txt","a") as f:
            f.write(f"{a_name}| {Worked_time}|  {a},{b}    |    {Operation}    |{result}\n")
    return inner

@calculation

def calculation(a,oper,b):
    if(oper=="+"):
        return a+b
    elif(oper=="-"):
        return a-b
    elif(oper=="*"):
        return a*b
    elif(oper=="/"):
        return a/b
    else:
        print("Error")

a = int(input())
oper =  input()
b = int(input())
calculation(a,oper,b)