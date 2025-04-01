#다른 경로에 있는 모듈을 쓰려면 파이썬 패스 설정이 우선시 되어야 한다.
#import를 위한  VS Code 설정.md 참조 
from module import mathModule as md, printModule as pt
#Module 패키지에 __init__으로 접근 허용범위를 지정했으니 아래처럼 써도 무방하다.
#from Module import *

add : int = md.add(3,4)
multi : int = md.multi(2,3)

print(f"add::::{add}")
print(f"multi::::{multi}")

pt.hello();