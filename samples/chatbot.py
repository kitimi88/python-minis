import os
import sys
import openai
import prompt_toolkit
from dotenv import load_dotenv
load_dotenv('./.env')
import textwrap

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        n=1,
        stop=None,
        temperature=0.9,
    )

    message = response.choices[0].text.strip() # type: ignore
    message = textwrap.fill(message, width=60)
    numbered_response = ""
    lines = message.split("\n")
    for i, line in enumerate(lines):
        numbered_response += str(i+1) + ". " + line + "\n"
    return message

def chat_prompts():
    while True:
        endmsg = 'Goodbye! See you next time.'
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "end", "stop", "exit"]:
            print("ChatBOT: ",(endmsg))
            sys.exit()
        else:
            prompt = (f"User: {user_input} \nChatBOT: ")
            response = generate_response(prompt)
            print("\nChatBOT:",response)
            print('')
            continue

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = "ChatBOT (OpenAI)\n\nTo END session, type: 'bye, goodbye, end or exit"
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')

    if not openai.api_key:
        print("ERROR: No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit()
        
    chat_prompts()

if __name__ == '__main__':
    main() 