#파이썬 조건문 

i = 1
type = "int"

#IF 조건문: - ":"으로
# 처리내역은 줄바꿈 후 들여쓰기
print("IF 조건문 =========")
if i==1:
    print(True)
    print()

#IF 조건문:
#    처리
# else:
#    처리
print("IF ~ Else 조건문 =========")
if i > 1:
    print("큼=========")
else :
    print("작음========")
print()

print("IF ~ elif ~ Else 조건문 =========")
#IF 조건문:
#    처리
# elif 조건문:
#    처리
# else:
#    처리
if i > 2:
    print("2보다 큼=========")
elif i > 1:
    print("1보다 큼=========")
else:
    print("작음========")
print()

#조건문 연산자 같다(==), 크다 (>), 작다(<) 등 산술비교 제외
print("조건문 연산자 =========")
if i == 1 and type == "int":
    print("and 조건 ========")

if i > 1 or type == "int":
    print("or 조건 ========")

if not type == "str":
    print("not 조건 ========")
    print()

#조건부 표현식 (삼항 연산자)
#변수명 = [조건이 맞을때] 조건식 [조건이 틀릴때]  
#else if 적용 안됨  : elseif는 중복조건으로처리
x = 10
result = True if x > 5 else False
print("삼항 연산자=========")
print(result)

#삼항 연산자elif 적용 안됨  : elif는 중복조건으로처리
score = 85
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print("삼항 연산자 elIF======",grade)
print()

#데이터 타입이랑 비교 In, NOT In
#비교 리스트, 튜플, 문자열 대상 사용
#True/False로 결과 반환
condList = ['h', 'e', 'l', 'l', 'o']
condTuple =  tuple('hello') #('h', 'e', 'l', 'l', 'o')로 변환 된다.
condStr = 'hello'

print("IN/NOT IN =========")
print("List IN ========", 'h' in condList)
print("List not IN ========", 'hh' not in condList)
print("Tuple IN ========", 'h' in condTuple)
print("Tuple not IN ========", 'hh' not in condTuple)
print("STRING IN ========", 'h' in condStr)
print("STRING not IN ========", 'hh' not in condStr)
print()

#분기문(분기조건)
print("분기문(분기조건) =========")
value = 33
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3 | 4:
        print( "Value is 3 or 4")
    case _:
        print("Value is something else")