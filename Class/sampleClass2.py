from .sampleClass1 import sampleClass1 #상속을 위해 import

class sampleClass2(sampleClass1): # sampleClass1 상속 다중상속이면 ","로 구분분
    def __init__(self,name,age): #생성자 
        sampleClass1.__init__(self,name) #부모 클래스 초기화 다중상속이면 각각 초기화 
        self.age = age 
        print(f"Hi~.{self.name}!!")   #name을 전역 처리한것은 부모 클래스 부모것 가져다 씀  
        print(f"{self.name}~ age:::{age}!!")    
    
    def info(self,region): #전역으로 사용되는 self는 필수로 받는다 
        print(f"너의 이름은 {self.name} 어디서 왔나? {region}")
        
    def defineC(self,name): #sampleClass1 defineC 메소드 오버라이딩 (재정의)
        print(f"{name} 인스턴스가 sampleClass2.defineC Call") 
        
    #부모 클래스 메소드 사용 : super().메소드(params) -  super() 콜하면 self는 넘기지 않아도 된다.
    def colors (self, color): 
        super().defineColor(color)
        print("부모 클래스에서 실행!!!!")