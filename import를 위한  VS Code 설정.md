
# ✅ 모듈파일 import를 위한  VS Code 설정 정리

## 📁 디렉토리 구조 예시

```
my_project/
├── .env
├── .vscode/
│   └── settings.json
├── lib/
│   └── mod1.py
├── class/
│   └── class1.py
├── venv/
└── ...
```

## 📄 1. `.env` 파일 생성

`my_project/.env`:

```env
PYTHONPATH=.
```

> 현재 프로젝트 루트(`.`)를 Python 모듈 검색 경로에 추가  
> `from lib import mod1` 또는 `from lib.mod1 import hello` 등 자유롭게 import 가능

## 📄 2. VS Code 설정 추가

`my_project/.vscode/settings.json`:

```json
{
  "python.envFile": "${workspaceFolder}/.env"
}
```

> VS Code가 `.env` 파일을 자동으로 읽어서  
> PYTHONPATH를 실행 환경에 반영하도록 설정

## ✅ 임포트 예시

### `lib/mod1.py`:

```python
def hello():
    print("Hello from mod1!")
```

### `class/class1.py`:

```python
from lib.mod1 import hello

hello()  
```

> 또는  
> ```python
> from lib import mod1
> mod1.hello()
> ```

## 🚀 실행 방법

- VS Code에서 `class1.py` 열고 `F5` 누르거나
- 터미널에서:

```bash
python class/class1.py
```

## 💡 git에 공유할 파일

- `.env` ✅ (PYTHONPATH 설정)
- `.vscode/settings.json` ✅ (환경 반영용)
- `.vscode/launch.json` ❌ (개인 설정이라 공유 불필요)

## 📄 `.gitignore` 참고 예시

```gitignore
# Ignore virtual env
venv/

# Ignore pycache
__pycache__/
*.pyc

# Ignore personal launch configs, but keep settings
.vscode/launch.json
```
