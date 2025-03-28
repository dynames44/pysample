from collections.abc import KeysView, ValuesView, ItemsView

# 딕셔너리 생성 및 선언
listData: list[dict[str, str]] = []
dictData1: dict[str, str] = {'seqId': '001', 'name': 'name001', 'phoneNo': '010-1010-0001'}  # javascript Json 생성과 동일 
dictData2: dict[str, str] = dict(seqId="002", name="name002", phoneNo="010-2020-0002")
dictData3: dict[str, str] = {}  # 빈 딕셔너리 생성, dict()를 사용 하는거 보다 자원사용, 속도에서 효율적

print("생성 --------------------------------------------")
print("dictData1:::", dictData1)
print("dictData2:::", dictData2)

# 딕셔너리 set
dictData3["seqId"] = "0003"  # 딕셔너리 [키] = 값
dictData3["name"] = "name003"
dictData3["phoneNo"] = "010-3030-0003"

print("dictData3:::", dictData3)
print()

# 딕셔너리 data get
print("딕셔너리 데이터 접근 방법 --------------------------------------------")
print("Get Method:::", dictData3.get("seqId"))  # get 메서드를 사용하여 접근
print("Get Key Value:::", dictData3["name"])  # 키값 사용하여 접근
print()

# # 딕셔너리 키 존재 여부 확인
print("딕셔너리 키 존재 여부 확인 --------------------------------------------")
print("seqId Key Exist:::", "seqId" in dictData3)  # 딕셔너리에 있는 Key : True
print("test Key Not Exist:::", "test" in dictData3)  # 딕셔너리에 없는 Key : False
print("test Data Get Default::", dictData3.get("test", "nope"))  # 딕셔너리에 해당 키가 없을때 : 기본값 설정
print()

# 딕셔너리 활용
print("딕셔너리  활용 --------------------------------------------")
dictData4: dict[str, str] = dictData3.copy()  # 딕셔너리 복사
dictData4["seqId"] = "0004"  # 키값 수정
del dictData4["phoneNo"]  # 키 삭제

print("dictData3 #2:::", dictData3)  # 복사한 객체의 변형이 발생 하였으니 원본은 변화 x
print("dictData4:::", dictData4)

dictData4.clear()  # 딕셔너리의 모든 항목 삭제
print("dictData4 #3:::", dictData4)

# 딕셔너리가 비어 있는지 확인
if dictData4:
    print("dict Not Empty")
else:
    print("dict Empty")
print()

# 딕셔너리 활용  #2
print("딕셔너리 활용 #2 --------------------------------------------")
dictData5: dict[str, str | list[dict[str, str]]] = dictData3.copy()
dictKeys: KeysView[str] = dictData5.keys()  # 딕셔너리 Key 반환
dictValues: ValuesView[str | list[dict[str, str]]] = dictData5.values()  # 딕셔너리 Value 반환
dictItems: ItemsView[str, str | list[dict[str, str]]] = dictData5.items()  # 딕셔너리 Key,Value 반환

print("dictData5:::", dictData5)
print("dictKeys:::", dictKeys)
print("dictValues:::", dictValues)
print("dictItems:::", dictItems)
print()

print("그 외 --------------------------------------------")
listData.append(dictData1)
listData.append(dictData2)
dictData5["listData"] = listData  # 딕셔너리에 리스트 데이터를 받아서 쓸수 있다.

print("listData:::", listData)
print("dictData5:::", dictData5)
