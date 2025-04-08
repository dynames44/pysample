#데코레이터 외부 함수
def booster(func):

    #데코레이터 실행(반환)
    def innerFunc(*params):
        a = 2 * params[0]
        b = 3 * params[1]
        
        print("a:::::",a)
        print("b:::::",b)
        
        result = func(a, b) #콜백 함수 실행
        return result

    return innerFunc

'''
    외부 함수를 @+함수명
    데코레이터 적용되는 함수(파라미터)
    형태로 호출
'''
@booster
def add(x, y): #콜백 함수
    return x + y

#함수 호출할때 값만 넣어 호출 
result = add(1, 2)
print("Result:", result)



#데코레이터 외부 함수
def booster2(func):

    #데코레이터 실행(반환)
    def innerFunc2(**params):
        a = 2 * params["x"]
        b = 3 * params["y"]
        
        print("a2:::::",a)
        print("b2:::::",b)
        
        result = func(a, b) #콜백 함수 실행
        return result

    return innerFunc2

'''
    외부 함수를 @+함수명
    데코레이터 적용되는 함수(파라미터)
    형태로 호출
'''
@booster2
def add2(x, y): #콜백 함수
    return x + y

#함수 호출할때 키:값 형태로 호출 
dict_param = {'x': 1, 'y': 2}
result2 = add2(**dict_param)
print("result2:", result2)

