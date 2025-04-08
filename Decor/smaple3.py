'''
    데코레이터 확장 : 데코레이터에 인자 추가 
    - 데코레이터에 인자값을 전달하는 함수 추가 (booster)
    - 데코레이터는 원본 함수(func)를 받아서 구현 함수(wrapper)를 반환
    - wrapper 함수는 실제로 콜백 함수 실행 전/후로 가공/출력 작업을 처리
'''
def booster(factor):  #데코레이터 생성자 (옵션 인자 받는 함수)
    
    def decorator(func):  #콜백 함수 등록 (원본 함수 받기)
        
        def wrapper(*params):  #콜백 함수 실행부 (원본 함수 실행 전 가공)
            
            # 원본 함수에 넘길 인자 가공
            a = factor * params[0]
            b = factor * params[1]
            
            # 중간 출력 (디버깅 or 로깅 용도)
            print("factor:::::", factor)
            print("a:::::", a)
            print("b:::::", b)
            print()
            
            # 가공된 인자로 원본 함수 실행
            return func(a, b)  #콜백 함수 실행
        
        return wrapper  #wrapper 반환하여 실행 준비
    
    return decorator  #decorator 반환하여 데코레이터 완성

#실행부
for f in [2, 4, 6]:
    @booster(factor=f)  # booster 로 데코레이터 생성 + 옵션 전달
    def add(x, y):
        return x + y

    result = add(1, 2)  # dict 형태는 아님, 별 하나로 tuple 전달
    print("Result:", result)
    print()
