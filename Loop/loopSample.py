
#for 변수 in 시퀀스: <<":"
#    실행할 코드 <<들여쓰기
#변수: 각 반복에서 시퀀스의 현재 요소를 나타내는 변수입니다.
#시퀀스: 반복할 수 있는 객체 (리스트, 튜플, 문자열, range 등).

#List For
print("List For::::::")
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print("List  :::", f)
print()

#tuple For
print("tuple For::::::")
colors = ("red", "green", "blue")
for c in colors:
    print("tuple  :::", c)
print()

#string For
print("string For::::::")
string = "Python"
for s in string:
    print("string  :::", s)
print()

#range() 함수 사용
print("range def For::::::")
for i in range(5):
    print(":::::",i)
print()

#Dict For
dictData1 = {'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}
print("Dict  For::::::")
#딕셔너리 그대로 for문을 돌리면 key값만 반환
for d in dictData1:
    print("dict1  :::", d)
print()

print("Dict key For::::::")
#딕셔너리의 key만 반환
for k in dictData1.keys():
    print("dict key  :::", k)
print()

print("Dict values For::::::")
#딕셔너리의 values만 반환
for k in dictData1.values():
    print("dict values  :::", k)
print()

print("Dict item For #1::::::")
#딕셔너리의 키,값 모두 반환
#하나의 변수로 받으면 튜플 형태로 반환
for k in dictData1.items():
    print("dict item #1 :::", k)
print()

print("Dict item For #2::::::")
#딕셔너리의 키,값 모두 반환
#하나의 변수로 받으면 튜플 형태로 반환
for k, v in dictData1.items():
    print("dict key :::", k, ",value::::",v)
print()

print("enumerate ::::::")
# 리스트를 enumerate 형태로 변환 index 값을 추출
print("List enumerate::::::")
for i,f in enumerate(fruits):
    print("List index, value :::",i, f)
print()

#for break,continue
#break: 반복문을 중단하고 빠져나옵니다.
#continue: 현재 반복을 건너뛰고 다음 반복을 계속합니다.
print("for break ::::::")
for i in range(10):
    if i == 5:
        break
    print("break ::::::",i)
print()

print("for continue ::::::")
for i in range(10):
    if i % 2 == 0:
        continue
    print("continue ::::::",i)
print()

#list * dict for :
# 딕셔너리 활용 : 생성된 딕셔너리를 List에 Insert
listData = []
dictData3 = {}
dictData2 = dict(seqId="002", name="name002", phoneNo = "010-2020-0002")
listData.append(dictData1)
listData.append(dictData2)
listData.append(dictData3)

print("list * dict for --------------------------------------------")
for idx,data in enumerate(listData):
    for k, v in data.items():
        print("dict idx, key, value::::",idx,k,v)
print()
