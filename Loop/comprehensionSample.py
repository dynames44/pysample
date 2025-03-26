# Comprehension (컴프리헨션)
# list, dictionary, set, generator에서 사용
# 반복문과 조건문을 결합하여 하나의 구문으로 간결하게 표현

# Syntax: [expression for item in iterable if condition]
# - expression: 각 아이템에 적용할 표현식
# - item: 반복 가능한 객체의 개별 항목 , For in 의 변수
# - iterable: 리스트, 튜플, 문자열 등
# - condition: (선택사항) 특정 조건만 만족하는 항목 포함

# --- 리스트 컴프리헨션 ---
print("Comprehension list ::::::")
listData1 = [i for i in range(1, 11)]  # 1부터 10까지 각 값을 리스트 형태 [] 로 저장 
print("listData1 ::::::", listData1)

# 조건절 적용
listData1 = [i for i in listData1 if i % 2 == 0]
print("list condition ::::::", listData1)

# 중첩 조건절
listData1 = [i for i in range(1, 11) if i % 2 == 0 if i < 5]
print("list dual condition ::::::", listData1)

# if-else 사용
listData2 = [i * 2 if i % 2 == 0 else i for i in range(1, 11)]
print("list else condition ::::::", listData2)

# 2차원 리스트 펼치기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("type1 ::::::", flattened)

# # 중첩 변수 사용
data = [[x, y] for x in range(1, 6) for y in range(1, 4)]
print("type2 ::::::", data)

# 중첩 조건절
data = [(x, y) for x in range(1, 4) for y in range(1, 4) if x % 2 == 1 if y > 1] #x는 홀수 y는 2,3만 
print("type3 ::::::", data)

# --- 딕셔너리 컴프리헨션 ---
print("Comprehension dictionary ::::::")
name = ["왕춘삼", "김덕팔", "황갑득"]
age = [23, 14, 42]

# 키 하나에 value 모두 할당 (마지막 값만 남음)
dictData1 = {key: value for key in name for value in age}
print("dictData1 ::::::", dictData1)

# zip 활용 (정상적인 매핑)
dictData2 = {key: value for (key, value) in zip(name, age)}
print("dictData2 ::::::", dictData2)

# 조건절 포함
dictData3 = {key: value for (key, value) in zip(name, age) if value > 20}
print("dictData3 ::::::", dictData3)

# 조건에 따른 값 변경
dictData4 = {k: ("성인" if v >= 20 else "미성년자") for k, v in zip(name, age)}
print("dictData4 ::::::", dictData4)

# --- 셋 컴프리헨션 ---
print("Comprehension set ::::::")
setData = {i for i in range(10) if i % 2 == 0}
print("setData ::::::", setData)

# # --- 제너레이터 컴프리헨션 ---
# print("Comprehension generator ::::::")
# gen = (i * i for i in range(1, 6) if i % 2 == 1)
# print("gen ::::::", list(gen))  # 실제 꺼내려면 list() 또는 반복 필요

# # 제너레이터와 조건 처리
# lines = (line.strip() for line in ["  hi  ", "hello ", " bye"] if line.strip())
# print("lines ::::::", list(lines))
