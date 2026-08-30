# WazaName-AI

WazaName-AIは作品などに登場する技の命名サポートするためのアプリです。

## 説明

ジャンル、属性、タイプ、その他の情報を入力することでAIが10個技名に使えそうな単語を生成してくれます。チャット内容は基本的に10回分保存されるため、過去の生成物も確認することができます。

## 使用方法
### 注意
このアプリはGoogleAIStudioのAPIキーが必要となるため18歳以上の方しか使用することはできません。  

1. [GoogleAIStudio](https://aistudio.google.com/prompts/new_chat) でAPIキーを取得する。
2. このリポジトリをダウンロードし、次のコマンドを行う。(仮想環境で行うことを推奨)
```
pip install google-genai
pip install flask
```
3. apikey.txt, secret.txtファイルを作成し、apikey.txtに先ほど入力したAPIキーを、secret.txtにシークレットキー(適当なキー)を入力する。
4. main.pyを実行する。