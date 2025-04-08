def outer( a : int ):
    x = 10 
    z = x*a
    
    def inner(b : int):
        return z * b
    
    return inner

inner = outer(2)  
rtn : int = inner(10)          

print("rtn::::",rtn)


def outer():
    x = 10 
    
    def inner():
        return x
    
    return inner

inner = outer()  
rtn : int = inner()          