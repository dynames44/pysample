'''
  set.......  
  할당되는 인자들 중 중복 제거
  : 배열 형태의 리스트인자들의 중복 제거가 필요하면 리스트 >> set >> 리스트
  
  내 지식의 한계 일지는 모르겠지만 튜플 처럼 활용도가 높지 않을듯..
  결국 현재 개발의 트랜드상 대부분은 리스트(Array-List), 딕셔너리로(Map-Hasable) 해결 되지 않을까?
'''
# set 생성 및 선언
set1 = {'ABC', 'BCD', 'DEF', 'ABC'}
list1 = ['ABC', 'BCD', 'DEF', 'ABC']
set2 = set(list1) # list 인자 중복제거 
set3 = set("babnana") #char At 근데 중복은 제거

print(set1)
print(list1)
print(set2)
print(set3)
