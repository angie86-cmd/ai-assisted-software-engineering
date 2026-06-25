import os
import sys

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


PROMPT = (
    "Write a concise customer service automation recommendation for a small "
    "online shop that wants to reduce repetitive support emails while keeping "
    "the customer experience friendly and personal."
)


def require_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(
            "Error: OPENAI_API_KEY is missing. Add it to your environment or "
            "create a local .env file based on .env.example.",
            file=sys.stderr,
        )
        sys.exit(1)
    return api_key


def generate_text(client: OpenAI, temperature: float, max_output_tokens: int) -> str:
    response = client.responses.create(
        # Replace the model if it is unavailable for your account.
        model="gpt-4.1-mini",
        input=PROMPT,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    return response.output_text


def main() -> None:
    load_dotenv()
    api_key = require_api_key()
    client = OpenAI(api_key=api_key)

    parameter_sets = [
        {"temperature": 0.2, "max_output_tokens": 120},
        {"temperature": 0.8, "max_output_tokens": 120},
    ]

    print("Prompt:")
    print(PROMPT)

    for index, params in enumerate(parameter_sets, start=1):
        print("\n" + "=" * 72)
        print(
            f"Run {index}: temperature={params['temperature']}, "
            f"max_output_tokens={params['max_output_tokens']}"
        )
        print("=" * 72)

        try:
            output = generate_text(client, **params)
        except OpenAIError as exc:
            print(f"OpenAI API error: {exc}", file=sys.stderr)
            sys.exit(1)

        print(output.strip())


if __name__ == "__main__":
    main()
