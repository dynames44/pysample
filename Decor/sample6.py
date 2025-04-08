class multiDecoator:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, arg, **kwargs):
        self.count += 1
        print(f"함수 호출: {self.count}회")
        preprocessed_arg = self.preprocess_args(arg)
        result = self.execute_function(preprocessed_arg, kwargs)
        self.postprocess_result(result)
        return self.func(result)

    def preprocess_args(self, arg): # 인자 전처리
        print(f"전처리: {arg}")

        if isinstance(arg, int):
            return arg * 2

        return arg

    def execute_function(self, arg, kwargs): # 본 함수 실행
        print(f"실행: {arg} {kwargs}")
        return arg

    def postprocess_result(self, result): # 결과 후처리
        print(f"후처리: {result}")
        
    def process_end(self, rtn):
        print("끝::::::",rtn)

#데코레이터 적용 함수
@multiDecoator
def sample_function(x):
    print(f"원본 함수 실행: {x}")
    return x + 1

#실행 구문
aa = sample_function(5)
#print(f"최종 결과: {result}")

sample_function.process_end(aa)
