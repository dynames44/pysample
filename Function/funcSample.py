# 파이썬 함수 기본 사용법  
# def 함수이름(매개변수):
#     실행할 코드
#     return 결과값
#
# 리턴변수 = 함수이름(인자값) 

# 리턴 값 없는 함수
def say_hello():
    print("hello!!!")

say_hello()
print()

def greet(name):
    print(f"{name}, Hi!!!!")

greet("Bong")
print()

# 리턴 값 있는 함수
def add(a, b):
    return a + b

result = add(3, 5)
print(f"func return :::: {result}")
print()

# n 개 리턴 값 있는 함수
def multRtn(a, b):
    return a + b, a * b, a / b

result = multRtn(3, 5) # 변수 하나로 받은 튜플 형태로 받는다.
print(f"func return :::: {result}")
print()

result1, result2, result3 = multRtn(3, 5) # 변수 리턴값 만큼 변수를 지정하거나 
print(f"func return1 :::: {result1}")
print(f"func return2 :::: {result2}")
print(f"func return3 :::: {result3}")
print()

#튜플형태로 활용 한다.
print(f"func return1 :::: {result[0]}")
print(f"func return2 :::: {result[1]}")
print(f"func return3 :::: {result[2]}")
print()

#Parameter 기본값 사용 함수
def usedefault(name="Uracle"):
    print(f"hi~ {name}!!!")

usedefault()
usedefault("Bong")
print()

#Argument에  Parameter 값값 사용 함수
def introduce(name):
    print(f"hi~ {name}!!!")

introduce(name="Bong")
#introduce(name1="Bong") # introduce 함수가 name1이라는 파라미처가 없으니 에러 발생 
print()

#Parameter를 가변인자로 받는 함수
# *파라미터명 : 튜플형태로 받아서 사용한다, 함수 안에서는 튜플이 가진 기능을 활용해 구현 가능  
# **파라미터명 : 키: 밸류..딕셔너리 형태로 받아서 사용한다.
 
# 가변 인자
def total(*params):
    totalSum = sum(params)
    print(f"Total:: {totalSum}")

total(1, 2, 3)
total(10, 20, 30, 40)
print()

# 키 : 밸류 가변 인자
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(seqId="001", name="name001", phoneNo='010-1010-0001')
print()

#show_info({'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}) # 키 : 밸류 가변 인자를 받는 함수라고 해도 익셔너리 타입으로 보내면 에러 발생 
dict = {'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}
show_info(**dict) # 딕셔너리 앞에 **을 넣어 언팩 해서 보내면 가능 
print()

dictData3 = {}
dictData3["seqId"] = "0003" 
dictData3["name"] = "name003"
dictData3["phoneNo"] = "010-3030-0003"

show_info(**dictData3) # 딕셔너리 앞에 **을 넣어 언팩 해서 보내면 가능 
print()

#일반 파라미터, 가변 파라미터 혼용 쌉가능 
def ssap(str, *params, **kwargs):
    totalSum = sum(params)
    print(f"str:: {str}")
    print(f"Total:: {totalSum}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
    
ssap("nono", 1, 2, 3,**dictData3)    
print()

#람다 함수 : 축양으로 가독 가능한 내용에만 사용 권장 
# 함수명 = lamda param1,param2 : 함수 표현식 
square = lambda x: x + 1
print(square(5))
print()