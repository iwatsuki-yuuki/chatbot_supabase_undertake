chatbot_supabase_undertake

📌 プロジェクト概要

CSVデータをもとに、Supabase（pgvector）とOpenAI（GPT・Embeddings API）を利用した、Q&A形式のAIチャットボットです。ユーザーが入力した質問をベクトル化し、Supabaseデータベースに登録した類似質問を検索・検索結果をもとにOpenAI GPTを利用し、自然で正確な日本語回答を生成します。フロントエンドはStreamlitを使用し、シンプルで直感的なWeb UIを提供します。

🛠 使用技術・データベース
	•	データベース: Supabase (pgvector)
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

④ 環境変数の設定 (.envファイル)

プロジェクトのルートに.envファイルを作成し、以下を記入します。

OPENAI_API_KEY=<あなたのOpenAI APIキー>
SUPABASE_URL=<あなたのSupabaseプロジェクトURL>
SUPABASE_KEY=<あなたのSupabaseプロジェクトAPIキー>

⚡️ アプリケーションの実行方法

streamlit run app/app.py

ブラウザで http://localhost:8501 にアクセスするとアプリケーションが表示されます。

🌐 デプロイについて（Render利用の場合）
	•	.envファイルをGitHubにプッシュしないように注意し、.gitignoreで明示的に除外してください。
	•	Renderで環境変数を設定し、必要な環境を整えます。
	•	GitHubリポジトリと連携後、デプロイを実施すると、公開URLが提供されます。

💡 注意事項
	•	データベースの埋め込みベクトルの次元（dimension）がモデルと一致することを確認してください（text-embedding-3-largeは3072次元）。
	•	APIキーの管理は厳重に行い、絶対に公開しないでください。