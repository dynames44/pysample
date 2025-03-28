from  Class import sampleClass1

#런타임에서 발생한 에러는 하나로  
try:
    t1 = sampleClass1()
except Exception as e:
    print("오류 타입:", type(e))
    print("오류 내용:", e)
    print("클래스 생성 실패!!!")
    
#에러별 케이스 구분     
try:
    x = 1 / 0
    
except ZeroDivisionError:  # 특정 오류만 잡음
    print("0으로 나눴어요!") 
    
except ValueError:  # 특정 오류만 잡음
    print("값 문제예요!")
    
except Exception as e:
    print("기타 오류:")    
    print("오류 타입:", type(e))
    print("오류 내용:", e)    
