import os
import json
import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

# 環境変数からAPIキーを取得
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_API_URL = 'https://translation.googleapis.com/language/translate/v2'
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'

MAX_CHAR_LIMIT = 1500
DEFAULT_TARGET_LANG = 'ja'

def translate_with_google(text, target_lang):
    try:
        payload = {
            'q': text,
            'target': target_lang,
            'format': 'text',
            'source': 'en'
        }

        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(f"{GOOGLE_API_URL}?key={GOOGLE_API_KEY}", headers=headers, data=json.dumps(payload))
        result = response.json()

        if 'data' in result and 'translations' in result['data']:
            return result['data']['translations'][0]['translatedText']
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f'Google翻訳でエラーが発生しました: {str(e)}')
        return None

def translate_with_deepl(text, target_lang):
    try:
        payload = {
            'auth_key': DEEPL_API_KEY,
            'text': text,
            'target_lang': target_lang.upper()  # DeepLでは大文字で指定
        }

        response = requests.post(DEEPL_API_URL, data=payload)
        result = response.json()

        if 'translations' in result:
            return result['translations'][0]['text']
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f'DeepL翻訳でエラーが発生しました: {str(e)}')
        return None

def translate_with_chatgpt(text):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENAI_API_KEY}'
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that translates text."},
                {"role": "user", "content": f"Please translate the following English text into Japanese: {text}"}
            ],
            "max_tokens": 1000,
            "temperature": 0.7
        }

        response = requests.post(OPENAI_API_URL, headers=headers, data=json.dumps(data))
        result = response.json()

        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f'ChatGPT翻訳でエラーが発生しました: {str(e)}')
        return None

st.set_page_config(page_title="Triple Translator (Google, DeepL, ChatGPT)")

st.title("Triple Translator (Google, DeepL, ChatGPT)")

input_text = st.text_area("翻訳したいテキストを入力してください/Enter text to translate", max_chars=MAX_CHAR_LIMIT)

target_lang = st.selectbox(
    "翻訳先の言語を選択してください/Select target language",
    options=[
        ("ja", "日本語/Japanese"),
        ("en", "English/英語"),
        ("de", "Germany/ドイツ語"),
        ("fr", "French/フランス語")
    ],
    format_func=lambda x: x[1],
    index=0
)

use_google = st.checkbox("Google翻訳を使用する/Use Google Translate", value=True)
use_deepl = st.checkbox("DeepL翻訳を使用する/Use DeepL Translate", value=True)
use_chatgpt = st.checkbox("ChatGPT翻訳を使用する/Use ChatGPT Translate", value=True)

if st.button("翻訳/Translate"):
    if input_text:
        if len(input_text) > MAX_CHAR_LIMIT:
            st.error(f'入力テキストが{MAX_CHAR_LIMIT}文字を超えています。現在の文字数: {len(input_text)}文字')
        else:
            with st.spinner('翻訳中/Translating...'):
                if use_google:
                    google_translation = translate_with_google(input_text, target_lang[0])
                    if google_translation:
                        st.subheader("Google Translation/Google翻訳結果:")
                        st.write(google_translation)
                    else:
                        st.error("Google翻訳に失敗しました/Google translation failed")

                if use_deepl:
                    deepl_translation = translate_with_deepl(input_text, target_lang[0])
                    if deepl_translation:
                        st.subheader("DeepL Translation/DeepL翻訳結果:")
                        st.write(deepl_translation)
                    else:
                        st.error("DeepL翻訳に失敗しました/DeepL translation failed")

                if use_chatgpt:
                    chatgpt_translation = translate_with_chatgpt(input_text)
                    if chatgpt_translation:
                        st.subheader("ChatGPT Translation/ChatGPT翻訳結果:")
                        st.write(chatgpt_translation)
                    else:
                        st.error("ChatGPT翻訳に失敗しました/ChatGPT translation failed")

    else:
        st.warning("テキストを入力してください/Please enter some text")

st.write(f"文字数/Character count: {len(input_text)} / {MAX_CHAR_LIMIT}")
