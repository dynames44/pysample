'''
 python 변수 활용 
 F Sting 사용 예제 
 
 고정된 문자열과 변수값을 출력 할때 "Sting" +  변수 + "Sting" 형태로 쓰지 않는다.
 : java , C 당연히 모두 있는건데...파이썬이 좀더 쓰기 거지 같음 
 : f""
'''
name: str = "bong"
printStr1: str = f"hi...{name}!!"
print(printStr1)

inta: int = 5
intb: int = 3
print(f"{inta} + {intb} = {inta + intb}")

def greet(name: str) -> str:
    return f"{name} goo to see you"

print(f"{greet(name)}")  

#F String을 쓰지 않으려면
print("hi...%s!!" % name)  
print("hi...{}!!".format(name))  
print("hi...{} & {}!!".format(name, "goo"))  
print("hi...{1} & {0}!!".format(name, "goo"))
