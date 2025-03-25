#난수발생 
from random import *
randInt1 = randrange(1,45) # From 이상 To 미만
randInt2 = randint(1,20) # From 이상 To 이하
print(f"램덤1:::{randInt1}")
print(f"램덤2:::{randInt2}")

#대소문자 구분 , 문자열 길이
str1 = "AAA"
str2 = "Aaaa"

boolStr1 = str1.isupper();
boolStr2 = str2[0].isupper();

print(boolStr1)
print(boolStr2)
print(len(str1))
print(len(str2))

#문자열 변환 : 단. python의 replace는 replace all
# replace first를 원하면 파이썬 내장함수 re.sub() 사용 
str3 = "This is dog."
print(f"str3::::{str3}")

str4 = str3.replace("dog","cat")
print(f"str4::::{str4}")

#문자열에서 찾기 
findStr1 = "dogcatdogfish"
print(f"Cat is exist ::::{findStr1.find('cat')}")
print(f"Bird is not exist ::::{findStr1.find('bird')}") #존재하지 않으면 -1반환  
print(f"Second dog ::::{findStr1.find('dog',1)}") #첫번째 dog 뒤로 find
print(f"Reverse find dog ::::{findStr1.rfind('dog')}") #뒤에서 find

#문자열에서 갯수 찾기 
print(f"Dog count ::::{findStr1.count('dog')}")