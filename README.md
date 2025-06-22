## 💡 アイデア出しAIエージェント
実現可能性まで含めたアイデアを最終的に出してくれるアイデア出しAIエージェントです。
```
# 仮想環境の構築
python -m venv .venv # 仮想環境を作成 (初回のみ)
source .venv/bin/activate # 仮想環境をアクティベート (Windowsの場合は .\ .venv\Scripts\activate)
pip install -r requirements.txt

# 開発
adk web
```
`http://localhost:8000`で開発鯖が立ち上がります。   
`.env.example`を`.env`にして、Google gemini API keyを追加してください。
