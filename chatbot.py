import openai
import prompt_toolkit
import os
from dotenv import load_dotenv
load_dotenv('./.env')

openai.api_key = os.environ['OPENAI_API_KEY']


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )

    message = response.choices[0].text.strip()
    return message

def app_header():
    print('------------------------------------------------')
    print('             Welcome to ChatGPT!                ')
    print('------------------------------------------------')
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_header()
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