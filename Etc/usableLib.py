# filter 함수에 파리미터를 적용했을때, 결과가 True가 되는 값들만 만환한다.
# Map : 함수에  파리미터를 적용했을때 처리 결과를 반환한다.
# 파라미터를 반복형으로 쓸수 있으면 반복문으로 함수를 실행하는 번거로움 해소용으로 사용
# filter는 결과를 True/False로 리턴하는 함수만 적용 가능 
def filterExal1(i : int):
    return i >0

rtnList : list = list(filter(filterExal1, [-1,2,-2,0,3]))
print("rtnList:::::",rtnList)

rtnList : list = list(map(filterExal1, [-1,2,-2,0,3]))
print("rtnList:::::",rtnList)


# 원론은 파라미터는 하나만 받아서 쓸수 있지만 함수안에서 가공해서 사용한다면 N개의 파라이터 형태로 쓸수도 있다
def add_pair(pair):
    x, y = pair
    return x + y > 5

rtnList : list = list(filter(add_pair, [(1, 2), (3, 4), (5, 6)]))
print("rtnList:::::",rtnList)

rtnList : list = list(map(add_pair, [(1, 2), (3, 4), (5, 6)]))
print("rtnList:::::",rtnList)
print()

#jSon, 딕셔너리 변환 
import requests, json

#.json 파일을 읽어와서 딕셔너리 객체로 변환 
#json.load("파일객체")

#json 형태의 문자열을 딕셔너리로 변환 
str1 = '{"name" : "test", "age":"15"}'
dict1 = json.loads(str1)
print("name::::::",dict1.get("name"))
print("age::::::",dict1.get("age"))
print()
#API에서 리턴받은 
#Contents Type이 application/json 아닌 경우....혹은 오류 일때....

# 정상일때 .json()으로 딕셔너리 타입 자동 변환 
#res = requests.get("https://api.example.com/user/1")
#data = res.json()

#정상이 아닐때 text받아서 json 타입으로 변환 
#data = json.loads(res.text)