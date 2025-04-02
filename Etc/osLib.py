import os
from pathlib import Path

#시스템 환경경변수 조회
env_dict :dict = dict(os.environ)

#for d in env_dict:
    #print(d ,":",env_dict.get(d))

#시스템 커멘드 실행
a = os.system("cls")

#시스템 커멘드 실행 결과를 파일 형태로 출력한다.
f = os.popen("dir")
print(f.read())  

# 현재 디렉토리 
o = os.getcwd() 
p = Path.cwd()
print(p)
print(o)  

# 현재 디렉토리의 모든 파일/폴더
#files = os.listdir(".")  
#print("files::::",files)

# 디렉토리 이동
os.chdir("Class")
print("변경 디렉토리::::",Path.cwd()) 

#경로 지정/결합
base = Path("D:/Python/Skeleton")/ "pysample" #pathlib : Path("경로") / "추가경로" / "추가경로"
target = os.path.join("D:\Python\Skeleton", "pysample") #("경로","추가경로","추가경로")
print("base::::",base) 
print("target::::",target) 
print() 

#경로 존재 확인
targetResult: bool = True if os.path.exists(target) else False
baseResult: bool = True if base.exists() else False
print("targetResult::::",targetResult) 
print("baseResult::::",baseResult) 
print() 

#디렉토리 여부 확인
baseFile = base / "README2.md"

print(os.path.isdir(base))	
print(base.is_dir())
print(baseFile.is_dir())
print() 

#파일 여부 확인
print(os.path.isfile(baseFile))	
print(base.is_file())
print(baseFile.is_file())




