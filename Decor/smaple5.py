'''조건에 따른 데코레이터 실행  예제'''

apply = False

def decorator(func):

    print("데코레이터 :::::conditional_decorator")
        
    def wrapper(x, y):
        
        x = x*2
        y = y*3
        
        print("x:::::::",x)
        print("y:::::::",y)
        
        return func(x, y)
    return wrapper
	
def conditional_decorator(apply_decorator):
    def decorator1(func):

        print("데코레이터 :::::apply_decorator")

        if not apply_decorator:
            return func  

        def wrapper(x, y):

            x = x/2
            y = y/3
            
            print("x1:::::::",x)
            print("y2:::::::",y)

            return func(x, y)
        return wrapper
    return decorator1

@decorator
@conditional_decorator(apply)
def my_function(x, y):
    return x+y

aa = my_function(2, 3)
print("my_function:::::",aa)