#클패스 파일이 포함된 패키지 디렉토리에 __init__.py 가 지정되어 있의면 
from  Class import sampleClass1, sampleClass2 # from 패키지명 import 클래스1,클래스2  

# Class.sampleClass1 형태의 네임스페이스로 클래스를 임포트 해서 쓴다.
#from Class.sampleClass1 import sampleClass1
#from Class.sampleClass1 import sampleClass1

t1 = sampleClass1("Bong")
print(f"너의 이름은 {t1.name}") #클래스의 멤버 변수를 인스턴스에서 뽑아 쓸수 있다.

t2 = sampleClass2("Bong",30)

t2.sample1() # 부모 클래스내 메소드 호출
t2.info("노원") # 자식 클래스내 메소드 호출

t2.hobby = "golf" #클래스 내에 없는 멤버 변수도 생성가능, 단!!! 생성한 인스턴스에 한정된다.
print(f"너의 취미는 {t2.hobby}") 

t1.defineC() #원본 메소드
t2.defineC("t2") # 자식클래스에서 재정의된 메소드 

t2.colors("white") #자식 클래스에서 부모를 super()호 호출
print(t2.color)