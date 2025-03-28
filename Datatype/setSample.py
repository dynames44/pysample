'''
  set.......  
  할당되는 인자들 중 중복 제거
  : 배열 형태의 리스트인자들의 중복 제거가 필요하면 리스트 >> set >> 리스트
  
  내 지식의 한계 일지는 모르겠지만 튜플 처럼 활용도가 높지 않을듯..
  결국 현재 개발의 트랜드상 대부분은 리스트(Array-List), 딕셔너리로(Map-Hasable) 해결 되지 않을까?
'''
# set 생성 및 선언
set1: set[str] = {'ABC', 'BCD', 'DEF', 'ABC'}
list1: list[str] = ['ABC', 'BCD', 'DEF', 'ABC']
set2: set[str] = set(list1)  # list 인자 중복제거 
bananaList: list[str] = list("babnana")  # list는 입력값 그대로 char At  
bananaSet: set[str] = set("babnana")     # set은 중복 제거 된 char At 

print(f"set1:::::{set1}")
print(f"list1:::::{list1}")
print(f"set2:::::{set2}")
print(f"bananaList:::::{bananaList}")
print(f"bananaSet:::::{bananaSet}")
print()

# 그외 n개의 set 값의  합집합, 교집합 추출 
# 리스트 > set 변환 > 리스트 변환 형식으로 활용도 가능 ....
# 샘플은 의미 없어서 생략 
# 더이상 set 효용성? 글쎄.....  
