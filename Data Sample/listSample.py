#리스트 생성 & 할당
dataList1 = [] #빈 리스트 생성
dataList2 = [1,3,7,2] #리스트 생성 & 값 할당
dataList3 = [1,2,3, ['test','comp']] #리스트는 다른 리스트를 인자로 가질수 있다

print("리스트 생성 & 할당 --------------------------------------------")
print("dataList1:::",dataList1)
print("dataList2:::",dataList2)
print("dataList3:::",dataList3)

#리스트가 비었는지 체크
if dataList1:
    print("list Not Empty")
    
else:
    print("list Is Empty")
print()

#리스트 요소 접근, 할당, 수정, 삭제
print("리스트 접근 --------------------------------------------")
print("list get :::",dataList2[0])  #1 
print("list get last :::",dataList2[-1]) #2 
print("중복 리스트 요소 접근 :::",dataList3[-1][0]) #test
print("리스트 요수값의 인덱스 번호  :::",dataList2.index(2)) #2가 리스트 몇번째에 있는지
print()

#그외 리스트 메소드
print("그외 리스트 메소드 --------------------------------------------")
print("List count :::",len(dataList2)) #리스트 요소 갯수
print("List data :::",dataList2.count(7) )#리스트 요소 값 갯수갯수 : 지정된 값이 리스트에 몇개 있는지
print()

delListdata = dataList2.pop(0) #지정한 인덱스의 요소를 삭제하고 삭제된 항목의 값을 반환한다. : 인덱스를 지정하지 않으면 맨 뒤에 값을 삭제
print("deldata :::",delListdata)
print("pop dataList2 :::",dataList2)
print()
dataList2.remove(7) #지정된 값의 리스트 요소를 삭제한다. : 지정된 값이 하나 이상이면 맨 앞에 것만 삭제 된다.
print("remove dataList2 :::",dataList2)


print("range 이용한 List 생성 --------------------------------------------")
#리스트 구성요소가 정수형에 한해서 range 함수를 이용 하여 생성 가능
rangeList1 = list(range(11)) # 10까지 생성
rangeList2 = list(range(1, 11))# 1부터 10까지 생성
rangeList3 = list(range(1,10,2))# 1부터 10까지 2씩 증가 하며 생성
rangeList4 = list(range(10,0,-1))# 10부터 2까지 1씩 감수 하며 생성
print("rangeList1 :::",rangeList1)
print("rangeList2 :::",rangeList2)
print("rangeList3 :::",rangeList3)
print("rangeList4 :::",rangeList4)
print()

#List 안에 dict(java-map) 포함
dictList = []
dictData1 = {'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}
dictData2 = dict(seqId="002", name="name002", phoneNo = "010-2020-0002")
dictList.append(dictData1)
dictList.append(dictData2)

print("List + Dict --------------------------------------------")
print("dictList:::",dictList)
print("List count :::",len(dictList))
print("List address :::",dictList[0])
print()