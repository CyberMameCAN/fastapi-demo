# FastAPI demo

## Refer

- [Poetry + fastAPI + VScode](https://zenn.dev/fuyu/scraps/5a17cd49801e15)
- [Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/)
- [FastAPI](https://fastapi.tiangolo.com/ja/)
- [iFlake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)
- [ google / yapf ](https://github.com/google/yapf)

## 説明

PoetryとFastAPIで初期の環境を作ってみる。

## 動かし方
    cd fastapi_demo
    poetry run uvicorn fastapi_demo.main:app --reload
    
### グレゴリー級数でのπの計算を表示

http://localhost:8000/enshuritsu/gregory_prog/1000

enshuritsu/gregory_prog/{1000回計算}

### モンテカルロ法でのπの計算を表示

http://localhost:8000/enshuritsu/montecalro/1000

enshuritsu/montecalro/{1000回計算}
