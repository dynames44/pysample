import traceback
import logging

#traceback 오류 추적 
def test1():
    return 1/0

def test2():
    test1()
    
def test3(): 
    try:
        test2()
    except:
        print(traceback.format_exc())
       
#test3()        

#traceback & 로거 조합  
# 로깅 설정 (파일 저장 + 콘솔 출력 둘 다 가능)
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
         logging.FileHandler("error.log", encoding='utf-8'),  
        logging.StreamHandler()             # 콘솔에도 출력
    ]
)

def risky_function():
    return 1 / 0  # 예외 발생

def main():
    try:
        risky_function()
    except Exception as e:
        # traceback 포함된 에러 로그 남기기
        tb = traceback.format_exc()
        logging.error("예외 발생:\n%s", tb)
        
main()