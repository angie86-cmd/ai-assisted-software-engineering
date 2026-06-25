# OpenAI API Text Generation

## Goal

This case study is a small, portfolio-ready Python demo for VelpTEC exercise 07.Ue.01. It shows how to call the OpenAI API for text generation with the official Python SDK and compare how output parameters affect generated responses.

## Project structure

```text
openai-api-text-generation/
|-- api_text_generation.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
`-- README.md
```

## Setup

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
code .env
python api_text_generation.py
```

In `.env`, replace the placeholder with your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file must never be committed to version control.

### Optional: macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
code .env
python api_text_generation.py
```

## How to run

```powershell
python api_text_generation.py
```

The script prints two generated answers for the same customer service automation prompt.

If the configured model is unavailable in your account, replace it in `api_text_generation.py` with another text generation model that your account can access.

## Parameters tested

Both runs use the same prompt and `max_output_tokens` value, while changing `temperature`:

| Run | Temperature | Max output tokens | Purpose |
| --- | --- | --- | --- |
| 1 | `0.2` | `120` | More focused and predictable wording |
| 2 | `0.8` | `120` | More varied and creative wording |

## Security notes

- The API key is read from the `OPENAI_API_KEY` environment variable.
- A local `.env` file is supported through `python-dotenv`.
- No real API key is included in this repository.
- `.env` is ignored by Git to avoid accidentally committing secrets.
- `.env` must never be committed because it can contain private credentials.

## Reflection

The comparison shows how generation parameters influence text style. Lower temperature is useful for consistent business communication, while higher temperature can help produce more varied wording for brainstorming or marketing-oriented drafts.

## Portfolio relevance

This project demonstrates practical API integration, environment-based secret handling, SDK usage, parameter comparison, and clear command-line output. It is intentionally small so the core implementation can be reviewed quickly.
