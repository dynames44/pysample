# 파이썬 함수 기본 사용법  
# def 함수이름(매개변수):
#     실행할 코드
#     return 결과값
#
# 리턴변수 = 함수이름(인자값) 

# 리턴 값 없는 함수
def say_hello() -> None:
    print("hello!!!")

say_hello()
print()

def greet(name: str) -> None:
    print(f"{name}, Hi!!!!")

greet("Bong")
print()

# 리턴 값 있는 함수
def add(a: int, b: int) -> int:
    return a + b

result: int = add(3, 5)
print(f"func return :::: {result}")
print()

# n 개 리턴 값 있는 함수
def multRtn(a: int, b: int) -> tuple[float, int, float]:
    return a + b, a * b, a / b

result: tuple[float, int, float] = multRtn(3, 5)
print(f"func return :::: {result}")
print()

result1: float
result2: int
result3: float
result1, result2, result3 = multRtn(3, 5)
print(f"func return1 :::: {result1}")
print(f"func return2 :::: {result2}")
print(f"func return3 :::: {result3}")
print()

print(f"func return1 :::: {result[0]}")
print(f"func return2 :::: {result[1]}")
print(f"func return3 :::: {result[2]}")
print()

# Parameter 기본값 사용 함수
def usedefault(name: str = "Uracle") -> None:
    print(f"hi~ {name}!!!")

usedefault()
usedefault("Bong")
print()

# Argument에 Parameter 값값 사용 함수
def introduce(name: str) -> None:
    print(f"hi~ {name}!!!")

introduce(name="Bong")
# introduce(name1="Bong")  # introduce 함수가 name1이라는 파라미터가 없으니 에러 발생
print()

# Parameter를 가변인자로 받는 함수
# *파라미터명 : 튜플형태로 받아서 사용한다
# **파라미터명 : 딕셔너리 형태로 받아서 사용한다

def total(*params: int) -> None:
    totalSum: int = sum(params)
    print(f"Total:: {totalSum}")

total(1, 2, 3)
total(10, 20, 30, 40)
print()

def show_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(seqId="001", name="name001", phoneNo='010-1010-0001')
print()

# 딕셔너리를 언팩해서 넘기기
dict_param: dict[str, str] = {'seqId': '001', 'name': 'name001', 'phoneNo': '010-1010-0001'}
show_info(**dict_param)
print()

dictData3: dict[str, str] = {}
dictData3["seqId"] = "0003" 
dictData3["name"] = "name003"
dictData3["phoneNo"] = "010-3030-0003"

show_info(**dictData3)
print()

# 일반 파라미터, 가변 파라미터 혼용 가능
def ssap(str: str, *params: int, **kwargs: str) -> None:
    totalSum: int = sum(params)
    print(f"str:: {str}")
    print(f"Total:: {totalSum}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")    

ssap("nono", 1, 2, 3, **dictData3)
print()

# 람다 함수
square: callable = lambda x: x + 1
print(square(5))
print()
