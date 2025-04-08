'''
데코레이터 체이닝 : 전체 기능을 단계적으로 처리하고, 최종적으로 본 함수를 실행한다.

@logger
@cache
@authenticator
콜백 함수...

- 데코레이터 함수는 선언 순서대로 감싸며,
- 각 함수의 wrapper 안에서는 바로 하위(wrapper)의 함수를 호출한다.

- 본 함수 실행 전에 전처리 / 권한 체크 / 데이터 검증 등을 처리할 수 있다.
- 기능별로 데코레이터를 분리해두면, 필요에 따라 추가하거나 제거하기 쉽다.

자바스크립트로 비유하면 다음과 비슷하다:

function logger(param1, param2) {
    cache(param1, param2);
    authenticator(param1, param2);
    // 본 함수 실행
}
'''

_cache = {}

# 사용자 권한 체크
def authenticator(func):
    
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user != 'admin':
            raise PermissionError("Access denied: Admins only")
        print("Access granted.")
        print()
        return func(*args, **kwargs)
    
    return wrapper

# 계산 결과 캐시
def cache(func):
    
    def wrapper(*args, **kwargs):
        
        key = (args, tuple(kwargs.items()))
        if key in _cache:
            print("Cache hit!")
            return _cache[key]
        print("Cache miss! Computing result...")
        print()
        result = func(*args, **kwargs)
        _cache[key] = result
        return result
    
    return wrapper

# 호출 기록 남기기
def logger(func):
    
    def wrapper(*args, **kwargs):
        
        print(f"Calling function logger with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function logger returned {result}")
        print()
        return result
    
    return wrapper

# 체이닝 : 순서대로 실행한다. 각 데코레이터의 wrapper는 자신이 아닌 다음 데코레이터의 wrapper를 실행한다.
@logger
@cache
@authenticator
def compute(x, y, user=None):
    print(f"Call Back!!!!! compute {x} + {y}")
    print()
    return x + y

# 실행
try:
    result1 = compute(3, 4, user='admin')  # 정상 통과
    print("result1::::::", result1)

    # 권한이 없는 경우 (guest), 흐름 설명:
    # logger wrapper → cache wrapper → authenticator wrapper (PermissionError 발생)
    compute(3, 4, user='guest')

except Exception as e:
    print("Error:", e)
