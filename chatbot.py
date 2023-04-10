import os
import sys
import openai
import prompt_toolkit
from dotenv import load_dotenv
load_dotenv('./.env')
import textwrap

openai.api_key = os.environ['OPENAI_API_KEY']


def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1,
        stop=None,
        temperature=0.9,
    )

    message = response.choices[0].text.strip()
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
            #prompt = f"User: {user_input}\nGPT3.5 Turbo:"
            response = generate_response(prompt)
            print("\nChatBOT:",response)
            print('')
            continue

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('---------------------------------------------------')
    print('                 ChatBOT (OpenAI)                  ')
    print()
    print("To END session, type: 'bye, goodbye, end or exit'")
    print('---------------------------------------------------')
    print()
    chat_prompts()

if __name__ == '__main__':
    main() 