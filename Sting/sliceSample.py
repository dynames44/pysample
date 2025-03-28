str1: str = "0123456789"
slc1: str = str1[1]
slc2: str = str1[0:2]  # 범위 0~1 이전 
slc3: str = str1[2:4]
slc4: str = str1[:4]
slc5: str = str1[4:]
slc6: str = str1[-6:]  # 리버스는 마이너스 인덱스

print(slc1)
print(slc2)
print(slc3)
print(slc4)
print(slc5)
print(slc6)
