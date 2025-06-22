```
# 仮想環境の構築
python -m venv .venv # 仮想環境を作成 (初回のみ)
source .venv/bin/activate # 仮想環境をアクティベート (Windowsの場合は .\ .venv\Scripts\activate)
pip install -r requirements.txt

# dev
adk web
```

`.env.example`を`.env`にして、Google gemini API keyを追加してください。
