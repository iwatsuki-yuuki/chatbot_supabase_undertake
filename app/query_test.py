import openai, os
from supabase import create_client
from dotenv import load_dotenv
import numpy as np

# 環境変数の読み込み
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
client = openai.OpenAI(api_key=openai.api_key)

# embeddingを取得する関数
def embed(text):
    if isinstance(text, str) and text.strip():
        response = client.embeddings.create(
            input=text,
            model='text-embedding-3-large'
        )
        return response.data[0].embedding
    else:
        return np.zeros(1536)

# ユーザーからの質問（ここを自由に変更）
question_text = "本社はどこ？"

# ベクトル化
embedding_vector = embed(question_text)

# Supabaseで関連データを取得
response = supabase.rpc('match_items', {
    'query_embedding': embedding_vector,
    'match_threshold': 0.8,
    'match_count': 5
}).execute()

matched_data = response.data

# プロンプトを作成（ここを追加）
context = "\n\n".join([
    f"質問: {item['question']}\n回答: {item['answer']}"
    for item in matched_data
])

prompt = f"""
以下の質問と回答を参考に、ユーザーの質問にわかりやすく回答してください。

{context}

質問: {question_text}
"""

# GPTで自然な回答を生成（ここを追加）
gpt_response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{'role': 'user', 'content': prompt}],
    temperature=0
)

# 結果を表示（ここを変更）
print("✅ GPTによる回答：\n")
print(gpt_response.choices[0].message.content)