import os
import sys
import openai
from dotenv import load_dotenv
load_dotenv('./.env')

openai.api_key = os.environ['OPENAI_API_KEY']

MODEL = 'gpt-3.5-turbo'

def chat_completion():
    completion = openai.ChatCompletion.create(
        model = MODEL,
        temperature = 0.2,
        max_tokens = 2000,
        messages = [
            {"role": "system", "content": "You are a friendly poet from the Philippines and you explain the moral values of your poem in simple terms."},
            {"role": "user", "content": "Write a short poem and explain briefly in Filipino."},
        ]
    )
    print(completion.choices[0].message.content)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = "ChatBOT (COMPLETION)\n\nTo END session, type: 'bye, goodbye, end or exit"
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')

    if not openai.api_key:
        print("ERROR: No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit()
        
    chat_completion()

if __name__ == '__main__':
    main() 