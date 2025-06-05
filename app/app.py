import streamlit as st
import openai, os
from supabase import create_client
from dotenv import load_dotenv
import numpy as np

# 環境変数の読み込み
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
client = openai.OpenAI(api_key=openai.api_key)

# Session stateを初期化（質問履歴）
if 'history' not in st.session_state:
    st.session_state.history = []

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

st.title("葬儀屋AIチャットボット")

user_input = st.text_input("質問を入力してください:")

if st.button("回答を表示"):
    embedding_vector = embed(user_input)

    response = supabase.rpc('match_items', {
        'query_embedding': embedding_vector,
        'match_threshold': 0.4,
        'match_count': 5
    }).execute()

    matched_data = response.data

    context = "\n\n".join([
        f"質問: {item['question']}\n回答: {item['answer']}"
        for item in matched_data
    ])

    prompt = f"""
    以下の質問と回答を参考に、ユーザーの質問にわかりやすく回答してください。
    質問が短縮や省略されている場合でも、参考質問の中からもっとも意味が近いものを推測し、その回答を使って答えてください。
    関連性が全くない場合のみ、「申し訳ありませんが、その質問に該当する回答が見つかりませんでした。」と返してください。

    {context}

    質問: {user_input}
    """

    gpt_response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0
    )

    answer = gpt_response.choices[0].message.content
    st.markdown(f"**回答:** {answer}")

    # 質問と回答を履歴に追加
    st.session_state.history.insert(0, {'question': user_input, 'answer': answer})

# サイドバーに質問の履歴を表示
st.sidebar.title("📜 質問履歴")
for i, item in enumerate(st.session_state.history):
    with st.sidebar.expander(f"{i+1}. {item['question'][:20]}...", expanded=False):
        st.sidebar.markdown(f"**質問:** {item['question']}")
        st.sidebar.markdown(f"**回答:** {item['answer']}")