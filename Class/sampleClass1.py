class sampleClass1:
    def __init__(self, name: str) -> None:  # 생성자 
        self.name = name  # 인스턴스 생성때 받은 name을 클래스 전역으로 사용한다.
        #print(f"Hi~.{name}!!")    
        
    def sample1(self) -> None:
        print("sampleClass1")
        
    def defineC(self) -> None:
        print("sampleClass1.defineC Call")
        
    # 파이썬은 메소드 오버로드는 지원되지 않는다. 
    # 파라미터나 구현이 다른 함수가 정의 되면 오버라이드 된다.    
    # def defineC(self,name): 
    #     print(f"{name} 인스턴스가 sampleClass1.defineC Call")                 
        
    def defineColor(self, color: str) -> None:        
        self.color = color
        print(f"너의 색깔을 찾아라..{color}")
