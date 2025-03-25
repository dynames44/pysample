
## ✅ 파이썬 개발 가상환경 설정 가이드



### 0. 파이썬 설치, Path 설정

> 설마 파이썬 설치 안하고 저대로 했더니 안된다고 할까봐 일단 써 놓는다.



### 1. 가상환경 생성

```
python -m venv venv
```

> 외부 라이브러리를 OS 전역에 설치하지 않고  해당 프로젝트 전용으로 격리된 환경 구성

---



### 2. 가상환경 활성화

#### 🔹 Windows (PowerShell)

```
.\venv\Scripts\activate
```



> 실행 권한 에러 시:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```



#### 🔹 macOS

```
source venv/bin/activate
```

---



### 3. 라이브러리 설치 및 실행

```
pip install -r requirements.txt
```

---



### ❗ 왜 꼭 이렇게 해야 하는가?

> - Maven 없이 스프링 앱 실행됨?  
> - `package.json` 없이 Node 돌아감?  
> - 된다고 한  그대는  최소 러키가이, 중간은 능력자, 최대는 신... 😎
