# OpenAI API Text Generation

## Goal

This case study is a small, portfolio-ready Python demo for VelpTEC exercise 07.Ue.01. It shows how to call the OpenAI API for text generation with the official Python SDK and compare how output parameters affect generated responses.

## Project structure

```text
openai-api-text-generation/
|-- api_text_generation.py
|-- sample_input.txt
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
python api_text_generation.py --mode generate
python api_text_generation.py --mode summarize
```

The default `generate` mode prints three generated answers for the same customer service automation prompt.

If the configured model is unavailable in your account, replace it in `api_text_generation.py` with another text generation model that your account can access.

## Parameters tested

The generation runs use the same prompt and output length while comparing `temperature` and `top_p`:

| Run | Temperature | top_p | Max output tokens | Purpose |
| --- | --- | --- | --- | --- |
| 1 | `0.2` | `1.0` | `120` | More focused and predictable wording |
| 2 | `0.8` | `1.0` | `120` | More varied and creative wording |
| 3 | `0.7` | `0.8` | `120` | Balanced creativity with a narrower token selection |

`temperature` controls how deterministic or varied the wording is. `top_p` controls nucleus sampling by limiting token choices to a probability mass. In practice, changing one parameter at a time is usually easiest to evaluate.

## Summarization mode

The script can also summarize a local input text from `sample_input.txt`. This mode asks the model to transform the source text into 5 concise bullet points using lower temperature for a stable summary.

```powershell
python api_text_generation.py --mode summarize
```

## Security notes

- The API key is read from the `OPENAI_API_KEY` environment variable.
- A local `.env` file is supported through `python-dotenv`.
- No real API key is included in this repository.
- `.env` is ignored by Git to avoid accidentally committing secrets.
- `.env` must never be committed because it can contain private credentials.

## Reflection

The comparison shows how generation parameters influence text style. Lower temperature is useful for consistent business communication, while higher temperature can help produce more varied wording for brainstorming or marketing-oriented drafts. Adjusting `top_p` provides another way to shape variation by narrowing or widening the model's token choices.

## Skills demonstrated

- OpenAI Responses API usage
- Environment-based secret handling
- Parameter tuning with temperature and top_p
- Summarization
- Text transformation workflows
- Simple command-line interface design

## Portfolio relevance

This project demonstrates practical API integration, environment-based secret handling, SDK usage, parameter comparison, summarization, and clear command-line output. It is intentionally small so the core implementation can be reviewed quickly.

## Output example

The script compares three API calls using the same prompt and output length, but different temperature and top_p values.

```text
Run 1: temperature=0.2, top_p=1.0, max_output_tokens=120

The first response is more stable, concise and predictable.

Run 2: temperature=0.8, top_p=1.0, max_output_tokens=120

The second response is more varied and slightly more creative in wording.

Run 3: temperature=0.7, top_p=0.8, max_output_tokens=120

The third response balances variation with a narrower sampling range.
```
