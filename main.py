import os
from google import genai
from flask import *

ApiKey = open("apikey.txt", "r", encoding="utf-8").read().strip()
client = genai.Client(api_key=f'{ApiKey}')
sample_text = """
  ジャンル. 属性. タイプ. その他の情報.
  これらの情報から10個、技名を提案します。
  1. 技名1
  2. 技名2
  3. 技名3
  4. 技名4
  5. 技名5
  6. 技名6
  7. 技名7
  8. 技名8
  9. 技名9
  10. 技名10
  以上です。お役に立てれば光栄です。
  """

design = open("design.css", "r", encoding="utf-8").read()

app = Flask(__name__)
app.secret_key = open("secret.txt", "r", encoding="utf-8").read().strip()
@app.route("/", methods=["GET", "POST"])
def html():
  if "history" in session:
    session["history"] = session["history"]
  else:
    session["history"] = []
  player_text = f"""
  <head>
    <meta charset="UTF-8">
    <title>技名生成AI</title>
  </head>
  <style>
    {design}
  </style>
  <body>
  <h1>技名を生成してみよう</h1>
  <div class="player-text">
    <form action="/" method="post">
      <input type="text" name="Genre" placeholder="ジャンルを入力してください(例: 攻撃、防御)"><br>
      <input type="text" name="Attribute" placeholder="属性を入力してください(例: 火、水、風)"><br>
      <input type="text" name="Type" placeholder="タイプを入力してください(例: 物理、魔法)"><br>
      <textarea name="Info" placeholder="その他に詳しい情報があれば入力してください"></textarea><br>
      <button type="submit" onclick="">決定</button>
    </form>
  </div>
  """
  if request.method == "GET":
    return f"{player_text}"
  else:
    try:
      genre_value = request.form["Genre"]
      attribute_value = request.form["Attribute"]
      type_value = request.form["Type"]
      info_value = request.form["Info"]
      response = client.models.generate_content(
          model="gemini-3-flash-preview",
          contents=f"あなたはプロのヒーローものを描いている作家です。ジャンル: {genre_value}\n属性: {attribute_value}\nタイプ: {type_value}\nその他の情報: {info_value}\n\n上記の情報をもとに、技名を10個生成し、マークダウンではなくhtml形式で返してください。情報が技に全く関係ない言葉であれば「すみません、生成できません。」と返してください。また、返答は次のもののようにしてください。{sample_text}。",
      )
      session["history"].append(
          f"AI > {response.text}<br>")
      if len(session["history"]) > 10:
        del session["history"][0]
      ai_response = ""
      for item in session["history"]:
        ai_response += f"{item}"
      return f"""{player_text}<br>
        <div class="ai-response">
          {ai_response}
        </div>
      """
    except Exception as e:
      return f"""{player_text}<br>
        <div class="ai-response">
          System > エラーが発生しました。不要な情報が入っていないか確認の上、再度お試しください。<br>
          エラー内容: {str(e)}<br>
        </div>
      """

if __name__ == "__main__":
  app.run()
