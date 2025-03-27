#클패스 파일이 포함된 패키지 디렉토리에 __init__.py 가 지정되어 있의면 
from  Class import sampleClass1, sampleClass2 # from 패키지명 import 클래스1,클래스2  

# Class.sampleClass1 형태의 네임스페이스로 클래스를 임포트 해서 쓴다.
#from Class.sampleClass1 import sampleClass1
#from Class.sampleClass1 import sampleClass1

t1 = sampleClass1();
t2 = sampleClass2();

