# Triple Translator (Google/DeepL/ChatGPT)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

3大翻訳サービス（Google翻訳・DeepL・ChatGPT）を比較できるマルチ翻訳Webアプリ

## 🌟 特徴

- **3大翻訳エンジンの同時比較**
  - Google Cloud Translation
  - DeepL API
  - OpenAI ChatGPT（GPT-3.5-turbo）
  
-   **リアルタイム翻訳比較:** 入力と同時に翻訳結果を比較表示。
-   **多言語対応:** 日本語、英語、ドイツ語、フランス語に対応。
-   **文字数制限通知:** 最大1,500文字までの入力制限を設け、API制限に対応。
-   **選択式インターフェース:** 必要な翻訳エンジンのみを選択可能。
-   **マルチリンガルUI:** ブラウザの言語設定に応じてUIを自動切替（日本語/英語）。

## 📋 必要条件

- Python 3.8+
- Streamlit
- 各サービスのAPIキー：
  - Google Cloud Translation API
  - DeepL API（無料版可）
  - OpenAI API

## 🚀 インストール

# リポジトリのクローン
```bash
git clone https://github.com/kenken-trpg/combined_machine_translater.git
cd combined_machine_translater
```

# 依存関係のインストール
   以下のコマンドをターミナルで実行して、必要なライブラリをインストールしてください。
```bash
pip install streamlit requests python-dotenv
```

⚙️ 設定
1. .env ファイルを作成：

```ini
GOOGLE_API_KEY="your-google-api-key"
DEEPL_API_KEY="your-deepl-api-key"
OPENAI_API_KEY="your-openai-api-key"
```
2. APIキーの取得：
- Google Cloud Console https://console.cloud.google.com/
- DeepL API https://www.deepl.com/pro-api
- OpenAI Platform https://platform.openai.com/

3.  **APIキーの設定:**
    *   プロジェクトのルートディレクトリに`.env`ファイルを作成します。
    *   Google翻訳、DeepL、OpenAIのAPIキーを`.env`ファイルに追加します。

    ```
    GOOGLE_API_KEY=your_google_api_key
    DEEPL_API_KEY=your_deepl_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```
    *   **重要**: `.env`ファイルは、絶対にバージョン管理システム(gitなど)にコミットしないでください(`.gitignore`に追加してください)。

🖥️ 使い方
1.  **Streamlitアプリを起動:**

    ```bash
    streamlit run google_deepl_chatgpt_translator.py
    ```

2.  **ブラウザでアプリを開く:**

アプリは自動的にデフォルトのブラウザで開きます。開かない場合は、ターミナルに表示されるローカルURL (通常は `http://localhost:8501`) をブラウザに入力してください。
    
1. 翻訳したいテキストを入力
2. 対象言語を選択（日本語/英語/ドイツ語/フランス語）
3. 使用する翻訳サービスをチェック
4. 「翻訳」ボタンをクリック

⚠️ 注意事項
- APIキーの管理には十分注意してください
- DeepL無料版は月500,000文字まで
- OpenAI APIは使用量に応じて課金が発生します
- 入力テキストは1,500文字までに制限されています（DeepL APIの制限に準拠）。
- 翻訳精度は各サービスの特性に依存し、常に正確とは限りません。

⚠️ 料金情報
| サービス | 無料枠 | 課金単位 | 注意点 |
| --- | --- | --- | --- |
| Google | 500,000文字/月 | $20/100万文字 | プロジェクト課金を有効化する必要あり |
| DeepL | 500,000文字/月 | €4.99/100万文字 | 無料版は速度制限あり |
| OpenAI | $5無料クレジット | $0.002/1,000トークン | 文字数≠トークン数 |
