# A collection of python mini projects

1. [Fibonacci](./fibonacci.py) - _The classic Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers._
2. [Birthday Countdown](./birthday_countdown.py) - _Calculate your age and number of days 'till your birthday._
3. [Currency Converter](./currency_convert.py) - _Covert your currency in real-time._
4. [Guess the number](./guess_num.py) - _A game where the computer generates a random number and the user has to guess what it is._
5. [Guess the number v.2](./guess_num_2.py) - _A game where the computer generates a random number and the user has to guess what it is with limited attempts._
6. [Hangman](./hangman.py) - _The classic Hangman game where users have to guess a word by guessing one letter at a time._
7. [Password generator](./password_gen.py) - _Generate a random password of the given length, including uppercase and lowercase letters, and optionally digits and symbols._
8. [Word and character count](./word_count.py) - _Count the number of words and characters._
9. [Weather](./weather.py) - _A program that uses an API to fetch the weather information of a location entered by the user._
10. [Chatbot (ChatGPT)](./chatbot.py) - _Simple chatbot using ChatGPT._
11. [URL Shortener](./shorten_url.py) - _URL shortener using ``pyshorteners`` module. This will help you shorten urls using various URL shortener services available including [tinyurl](https://tinyurl.com/app)._ 
---

## Requirements
- [Python 3.10.8 or later](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---
## Installation
1. Clone reporsitory.

```bash
$ git clone https://github.com/kitimi88/python-minis.git
```

2. Setup virtual environment.

```bash
$ py -m venv .venv
$ .venv\scripts\activate
```

3. Install required dependecies.

```bash
$ py -m pip install -r requirements.txt
```

---
## Note

The [Currency Converter](./currency_convert.py), [Weather](./weather.py), [Chatbot](./chatbot.py) requires the following packages:

| Package | Description |
| ------- | ----------- |
|[python-dotenv](https://pypi.org/project/python-dotenv/) |Read key-value pairs from .env file and set them as environment variables. In this sample app, those variables describe how to connect API. This package is used in the applications to load environment variables.|
| [OpenAI API](https://pypi.org/project/openai/) | Chatbot application requires integrating with an external API for natural language processing.
| [OpenWeatherMap API](https://openweathermap.org/api) | _Allowing users to obtain essential weather data for a specific location by making only one API call._
|[pyshorteners](https://pyshorteners.readthedocs.io/en/latest/apis.html#implemented-apis)|A simple URL shortening API wrapper Python library.

---
## Contributions
_Pending contribution guide._

## License
[MIT License](./LICENSE)

