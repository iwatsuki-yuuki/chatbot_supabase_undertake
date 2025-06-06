chatbot_supabase_undertake

📌 プロジェクト概要

CSVデータをもとに、Supabase（pgvector）とOpenAI（GPT・Embeddings API）を利用した、Q&A形式のAIチャットボットです。
	•	ユーザーが入力した質問をベクトル化し、Supabaseデータベースに登録した類似質問を検索
	•	検索結果をもとにOpenAI GPTを利用し、自然で正確な日本語回答を生成
	•	Streamlitを使用し、シンプルで直感的なWeb UIを提供

🛠 使用技術
	•	データベース: Supabase（pgvector）
	•	埋め込み生成: OpenAI Embeddings API (text-embedding-3-large)
	•	自然言語処理: OpenAI GPTモデル (gpt-4o)
	•	フロントエンド: Streamlit
	•	開発言語: Python 3.x

🌱 環境構築手順

① リポジトリをクローン

git clone <あなたのGitHubリポジトリURL>
cd qanda_undertake

② Python仮想環境を作成（推奨）

python3 -m venv venv
source venv/bin/activate

③ 必要なパッケージをインストール

pip install -r requirements.txt

④ 環境変数の設定（.envファイル）

プロジェクトのルートに.envファイルを作成します。

OPENAI_API_KEY=あなたのAPIキー
SUPABASE_URL=あなたのSupabaseプロジェクトURL
SUPABASE_KEY=あなたのSupabaseプロジェクトAPIキー

⚡️ アプリケーションの実行方法

streamlit run app/app.py

ブラウザが起動し、アプリケーションが利用できます。

🚀 Renderへのデプロイ
	•	GitHubリポジトリと連携し、RenderのダッシュボードでWeb Serviceを作成
	•	Renderの環境変数（Environmentタブ）にAPIキーを設定
	•	ビルドコマンドと起動コマンドを以下のように設定

項目	コマンド
Build Command	pip install -r requirements.txt
Start Command	streamlit run app/app.py --server.port=10000

✅ ライセンス

MIT License
© 2025 Chatbot Project