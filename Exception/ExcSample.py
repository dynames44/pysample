from Class import sampleClass1

#런타임에서 발생한 에러는 하나로  
try:
    t1: sampleClass1 = sampleClass1()
except Exception as e:
    print("오류 타입:", type(e))
    print("오류 내용:", e)
    print("클래스 생성 실패!!!")
    
#에러별 케이스 구분     
try:
    x: float = 1 / 0
except ZeroDivisionError:  # 특정 오류만 잡음
    print("0으로 나눴어요!") 
except ValueError:  # 특정 오류만 잡음
    print("값 문제예요!")
except Exception as e:
    print("기타 오류:")    
    print("오류 타입:", type(e))
    print("오류 내용:", e)    

#에러별 그룹별로 구분 가능
try:
    x: float = 1 / 0
except (ZeroDivisionError, ValueError) as e:  # 특정 오류만 잡음
    print("0으로 나눴거나 값 문제예요") 
    print("오류 내용:", e)    
except Exception as e:
    print("기타 오류:")    
    print("오류 타입:", type(e))
    print("오류 내용:", e)    
    
#조건 가능 : try구문이 에러나지 않았을때 실행할 구문 
try:
    t1: sampleClass1 = sampleClass1("봉구")
except Exception as e:
    print("오류 타입:", type(e))
    print("오류 내용:", e)
    print("클래스 생성 실패!!!")
else:
    t1.defineC()        

    try:
        t1.color()
    except Exception as e:
        print("오류 타입:", type(e))
        print("오류 내용:", e)
        print("color 실행 실패!!!")
        
#에러를 발생시키고 싶지 낳으면 pass 처리 
try:
    x: float = 1 / 0
except Exception as e:
    pass    
        
#없는 에러를 억지로 만들기 : raise
try:
    x: float = 1 / 1
    raise ZeroDivisionError
except Exception as e:
    print("오류 타입:", type(e))
    print("오류 내용:", e)
