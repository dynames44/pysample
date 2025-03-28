#파이썬 조건문 

i: int = 1

#IF 조건문: - ":"으로
# 처리내역은 줄바꿈 후 들여쓰기
print("IF 조건문 =========")
if i == 1:
    print(True)
    print()

#IF 조건문:
#    처리
# else:
#    처리
print("IF ~ Else 조건문 =========")
if i > 0:
    print("큼=========")
else:
    print("작음========")
print()

print("IF ~ elif ~ Else 조건문 =========")
#IF 조건문:
#    처리
# elif 조건문:
#    처리
# else:
#    처리
i: int = 2

if i > 2:
    print("2보다 큼=========")
elif i > 1:
    print("1보다 큼=========")
else:
    print("작음========")
print()

#조건문 연산자 같다(==), 크다 (>), 작다(<) 등 산술비교 제외
print("조건문 연산자 =========")
if i == 2 and isinstance(i, int):
    print("and 조건 ========")

if i > 1 or isinstance(i, int):
    print("or 조건 ========")
print()

#조건부 표현식 (삼항 연산자)
#변수명 = [조건이 맞을때] 조건식 [조건이 틀릴때]  
#else if 적용 안됨  : elseif는 중복조건으로처리
x: int = 10
result: int = 1 if x > 5 else 0
print("삼항 연산자=========")
print(result)
print()

#삼항 연산자elif 적용 안됨  : elif는 중복조건으로처리
score: int = 85
grade: str = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print("삼항 연산자 elIF======", grade)
print()

# #데이터 타입이랑 비교 In, NOT In
# #비교 리스트, 튜플, 문자열 대상 사용
# #True/False로 결과 반환
condList: list[str] = list('hello')
condTuple: tuple[str, ...] = tuple('hello')
condStr: str = 'hello'

print("List IN ========", 'h' in condList)
print("List not IN ========", 'hh' not in condList)
print("Tuple IN ========", 'h' in condTuple)
print("Tuple not IN ========", 'hh' not in condTuple)
print("STRING IN ========", 'h' in condStr)
print("STRING not IN ========", 'hh' not in condStr)
print()

#분기문(분기조건) : 매칭이 확실할때만....(조건을 쓸수 있긴하지만...없다고 보는게 속편함함)
print("분기문(분기조건) =========")
value: int = 3
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3 | 4:
        print("Value is 3 or 4")
    case _:
        print("Value is something else")
