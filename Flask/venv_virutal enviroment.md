## 가상환경 생성/설치/사용

가상 환경(virtual environment)은 독룁된 파이썬 실행 환경을 사용할 수 있도록 해줍니다. 이는 기존 설치한 패키지의 다른 버전과 충동을 일으킬 수 있어, 독립된 가상 환경을 구성하여 프로젝트를 운영하는 것을 권장한다고 한다.

생성
```
$ python3 -m venv venv #가상환경 생성

$ pip freeze > requirements.txt #패키지 정보기록
```

설치
```
$ python3 -m venv venv #가상환경 생성

$ pip install -r requirements.txt #패키지 설치
```

실행/종료
```
$ source venv/bin/activate #가상환경 실행

$ deactivate #가상환경 종료
```

