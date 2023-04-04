import openai
import prompt_toolkit
import os
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
    wrapped_text = textwrap.fill(message, width=60)
    numbered_response = ""
    lines = message.split("\n")
    for i, line in enumerate(lines):
        numbered_response += str(i+1) + ". " + line + "\n"
    return message


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('------------------------------------------------')
    print('             Welcome to ChatGPT!                ')
    print('------------------------------------------------')
    print("Type 'bye' to exit.\n")

    while True:
        qmsg = 'Goodbye! See you again next time!'
        prompt = input("\nYou: ")
        if prompt == 'bye' or prompt == 'Bye' or prompt == 'exit' or prompt == 'Exit':
            print('ChatGPT:', qmsg)
        # if prompt.lower() == "bye":
            break
        message = generate_response(prompt)
        print("ChatGPT:", message)

if __name__ == "__main__":
    main()