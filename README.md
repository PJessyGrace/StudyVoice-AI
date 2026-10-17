# StudyVoice AI 🎧

StudyVoice AI turns study notes into spoken audio using the Sarvam AI Text-to-Speech API. The demo supports English (India), Telugu, and Hindi.

## Features

- Paste study notes into a simple web interface.
- Choose a supported language.
- Generate and play speech.
- Download the generated WAV audio.

## Requirements

- Python 3.9 or newer
- A Sarvam AI API key with Text-to-Speech access

## Run locally

### 1. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Add your API key

Copy `.env.example` to `.env`, then replace the placeholder with your real key:

```text
SARVAM_API_KEY=your_real_key_here
```

**Never commit `.env` or paste your real key into `app.py`, README, screenshots, or GitHub.** The `.gitignore` file excludes `.env`.

### 4. Start the app

```powershell
streamlit run app.py
```

Your browser should open the StudyVoice AI interface.

## Push to GitHub

Create an empty repository on GitHub, then run these commands in this project folder:

```bash
git init
git add app.py requirements.txt README.md .gitignore .env.example
git commit -m "Build StudyVoice AI text-to-speech app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL. Do not run `git add .env`.

If you accidentally committed a real API key, deleting the file in a later commit is not enough. Revoke/rotate the key in the provider dashboard immediately, then remove the exposed secret from repository history if required.

## API details

This demo uses the official `sarvamai` Python SDK and the Sarvam Text-to-Speech API. API availability and usage limits depend on your account.

## Limitations

This is a small demo, not a medical device. Do not use generated audio as medical advice.
