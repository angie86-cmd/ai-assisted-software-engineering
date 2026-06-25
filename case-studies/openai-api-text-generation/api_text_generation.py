import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


# Local paths used by summarize mode.
BASE_DIR = Path(__file__).resolve().parent
SAMPLE_INPUT_PATH = BASE_DIR / "sample_input.txt"

# Reusable customer service automation prompt for generation mode.
PROMPT = (
    "Write a concise customer service automation recommendation for a small "
    "online shop that wants to reduce repetitive support emails while keeping "
    "the customer experience friendly and personal."
)


def require_api_key() -> str:
    """Validate that the API key is available without hardcoding secrets."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(
            "Error: OPENAI_API_KEY is missing. Add it to your environment or "
            "create a local .env file based on .env.example.",
            file=sys.stderr,
        )
        sys.exit(1)
    return api_key


def generate_text(
    client: OpenAI,
    prompt: str,
    temperature: float,
    top_p: float,
    max_output_tokens: int,
) -> str:
    """Send one Responses API request with configurable parameters."""
    response = client.responses.create(
        # Replace this model if it is unavailable for your account.
        model="gpt-4.1-mini",
        input=prompt,
        temperature=temperature,
        top_p=top_p,
        max_output_tokens=max_output_tokens,
    )
    return response.output_text


def run_generation(client: OpenAI) -> None:
    """Compare temperature and top_p settings."""
    parameter_sets = [
        {"temperature": 0.2, "top_p": 1.0, "max_output_tokens": 120},
        {"temperature": 0.8, "top_p": 1.0, "max_output_tokens": 120},
        {"temperature": 0.7, "top_p": 0.8, "max_output_tokens": 120},
    ]

    print("Mode: generate")
    print("\nPrompt:")
    print(PROMPT)

    for index, params in enumerate(parameter_sets, start=1):
        print("\n" + "=" * 72)
        print(
            f"Run {index}: temperature={params['temperature']}, "
            f"top_p={params['top_p']}, "
            f"max_output_tokens={params['max_output_tokens']}"
        )
        print("=" * 72)

        try:
            output = generate_text(client, PROMPT, **params)
        except OpenAIError as exc:
            print(f"OpenAI API error: {exc}", file=sys.stderr)
            sys.exit(1)

        print(output.strip())


def run_summarization(client: OpenAI) -> None:
    """Read local text and summarize it."""
    try:
        sample_text = SAMPLE_INPUT_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: {SAMPLE_INPUT_PATH.name} was not found.", file=sys.stderr)
        sys.exit(1)

    prompt = (
        "Summarize the following text in 5 concise bullet points:\n\n"
        f"{sample_text}"
    )

    print("Mode: summarize")
    print(f"\nInput file: {SAMPLE_INPUT_PATH.name}")
    print("\nSummary:")
    print("=" * 72)

    try:
        output = generate_text(
            client,
            prompt,
            temperature=0.2,
            top_p=1.0,
            max_output_tokens=180,
        )
    except OpenAIError as exc:
        print(f"OpenAI API error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(output.strip())


def parse_args() -> argparse.Namespace:
    """Provide the command-line mode selector."""
    parser = argparse.ArgumentParser(
        description="Compare OpenAI text generation parameters or summarize text."
    )
    parser.add_argument(
        "--mode",
        choices=["generate", "summarize"],
        default="generate",
        help="Choose generate for parameter comparison or summarize for local text summarization.",
    )
    return parser.parse_args()


def main() -> None:
    """Load environment variables, create the client, and dispatch the mode."""
    args = parse_args()
    load_dotenv()
    api_key = require_api_key()
    client = OpenAI(api_key=api_key)

    if args.mode == "summarize":
        run_summarization(client)
    else:
        run_generation(client)


if __name__ == "__main__":
    main()
