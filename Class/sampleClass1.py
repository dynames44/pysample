class sampleClass1:
    def __init__(self,name): #생성자 
        self.name = name # 인스턴스 생성때 받은 name을 클래스 전역으로 사용한다.
        #print(f"Hi~.{name}!!")    
        
    def sample1(self):
        print("sampleClass1")