import pandas as pd
import numpy as np
import openai, os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
client = openai.OpenAI(api_key=openai.api_key)

# CSV読み込み（欠損値を削除）
df_master = pd.read_csv('data/master.csv').dropna(subset=['カテゴリ', '質問', '回答'])
df_segment = pd.read_csv('data/segment.csv').dropna(subset=['カテゴリ', '情報'])

# segmentテーブルの重複を避けるために、最初にクリア（オプション）
supabase.table('segment').delete().neq('id', 0).execute()

# セグメント挿入（情報も含めて）
for _, row in df_segment.iterrows():
    supabase.table('segment').insert({
        'name': row['カテゴリ'],
        'information': row['情報']
    }).execute()

# セグメントのID取得（マッピング用）
segment_records = supabase.table('segment').select('id,name').execute().data
segment_map = {record['name']: record['id'] for record in segment_records}

# 安全なembed関数
def embed(text):
    if isinstance(text, str) and text.strip():
        response = client.embeddings.create(
            input=text,
            model='text-embedding-3-large'
        )
        return response.data[0].embedding
    else:
        return np.zeros(3072)

# masterデータ挿入（embedding含む）
for _, row in df_master.iterrows():
    embedding = embed(row['質問'])
    #print(embedding)  # これを追加して出力結果を確認
    supabase.table('master').insert({
        'category': row['カテゴリ'],
        'question': row['質問'],
        'answer': row['回答'],
        'embedding': embedding
    }).execute()