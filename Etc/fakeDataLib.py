import tempfile, time
from pathlib import Path
'''
    임시파일 생성 
    : 경로와 파일명을 반환 받을수 있는 임시 파일을 생성및 사용 후 삭제
    
    file = tempfile.NamedTemporaryFile
    (
         dir = 파일경로 
        ,prefix = "파일명 접두사"
        ,suffix="확장자"
        ,delete=프로세스종료후 삭제여부
    )
'''
# 저장할 경로
save_dir = Path("D:/my_temp")

# 폴더가 없으면 생성
save_dir.mkdir(parents=True, exist_ok=True)

# 임시 파일 생성
with  tempfile.NamedTemporaryFile(
    dir=save_dir,
    prefix="sample_",
    suffix=".log",
    delete=False 
)  as temp:

    temp.write(b"hello")       
    temp.flush()               
 #   print("파일 경로:", temp.name)

#delete 옵션 지정이 없으면 프로세스 종료 후 파일은 삭제 된다.
f = tempfile.NamedTemporaryFile()
#print("f1::::",f.name)  

#delete 옵션 지정 없이 타이머를 사용하여 파일 삭제 할 수 있다.
time.sleep(5)

#Dummy Data 생성 
from faker import Faker

#Faker.seed(1234)  #  seed를 지정 하면 항상 같은 값으로 Dummy Data를 생성해 준다.
#fake = Faker('ko_KR') 로케일 설정 - 지정 없으면 영어로 데이터 생성 

fake = Faker('ko_KR')

# print(fake.name())         # 이름
# print(fake.address())      # 주소
# print(fake.email())        # 이메일
# print(fake.date_of_birth()) # 생년월일
# print(fake.company())      # 회사명

#dic 형태의 데이터 생성 
users = [ 
    {
        "id": i+1,
        "name": fake.name(),
        "email": fake.email(),
        "registered_at": fake.date_time_this_decade()
    }
    for i in range(4)
]

#list 형태의 데이터 생성 
userNameList = [fake.name() for i in range(4)]

print("users:::::",users)
print("userNameList:::::",userNameList)