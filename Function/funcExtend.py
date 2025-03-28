# 함수 선언시 파마미터에 대한 힌트를 선언한다.

from typing import Optional, Union, Literal, Callable
import traceback

# Optional : 파라미터 값이 있을수도 있고 없을 수도 있음 
# 단 디폴트 None 선언이 없음 에러
# def exOptional (name : Optional[str]) -> None:  에러 name에 None을 명시 해야 함 
def exOptional (name : Optional[str] = None) -> None: # 시턴값 없는 Void 함수,  문자열 타입의 name 이라는 파마미터를 받음 , 단. 파라미터 없어도 실행에 문제 없음
    
    if name is not None:
        print(f"Param name ::: {name}")
    else:
        print(f"Param name ::: None")    
        
exOptional()
exOptional("Bong!!!")

#Union 변수에 나열된 타입 중 하나를 인정한다
def exUnion( age : Union [str, None]) -> None:
    if age is not None:
        print(f"Param age ::: {age}")
    else:
        print(f"Param age ::: None")        
    
exUnion("Bong!!!")

# 그런데 말입니다....
# 나열된 변수형이 아닌데 에러 안남 
# 말그대로 힌트지 강제 규정 아님 
exOptional(3)
exUnion(3) 

# 그래도 에러 나길 원한다면????
# 강제 체크로직 추가 
def exOptionalExds(name: Optional[str] = None) -> None:
    try:
        if not isinstance(name, (str, type(None))):
            raise TypeError("name는 str 또는 None만 가능합니다.")
        
    except Exception as e:
        print("오류 타입:", type(e))
        print("오류 내용:", e)
        
    else:
        if name is not None:
            print(f"Param name ::: {name}")
        else:
            print(f"Param name ::: None")                    

exOptionalExds(3)

# Literal 나열된 Literal 중 하나를 변수로 받는다.
# 기본적으로는 당연히 강재성은 없다. 그러나 억지로 강제 할수도.....
def exLiteral(level: Literal["DEBUG", "INFO", "ERROR"]) -> None:
    
    try:
        if level not in ("DEBUG", "INFO", "ERROR"):
            raise ValueError(f"허용되지 않은 level 값입니다: {level}")
        
    except Exception as e:
        print("오류 타입:", type(e))
        print("오류 내용:", e)
        
    else:
        print(f"level::::::{level}")    
    
exLiteral("INFO") #정상동작
exLiteral("INFO1") #오류 발생

def hello(name: str) -> None:
    print(f"Hello~, {name}")
    
def hi(name: str, age: int) -> None:
    print(f"Hi~ {name}, Age {age}")    

def exCallable(func: Callable[[str, int], None], value: str, age: int =0) -> None:
    #func(value,age)

    #어거지로 같이 쓰자면.... 
    try:
        if func.__name__ == "hello":
            func(value)
        else:
            func(value, age)        
        
    except Exception as e:
        print("오류 타입:", type(e))
        print("오류 내용:", e)

exCallable(hello, "Bong")
exCallable(hi, "Goo")