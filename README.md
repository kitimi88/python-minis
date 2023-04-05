# A collection of python mini projects

* [Fibonacci](./fibonacci.py) - _Generates sequence of numbers, in which every term in the sequence is the sum of terms before it._
* [Birthday Countdown](./birthday_countdown.py) - _Calculate your age and number of days 'till your birthday._
* [Currency Converter](./currency_convert.py) - _Real-time currency conversion tool._
* [Guess the number](./guess_num.py) - _Guess the random number with unlimited attempts._
* [Guess the number v.2](./guess_num_2.py) - _Guess the random number with LIMITED attempts._
* [Hangman](./hangman.py) - _A classic word-guessing game._
* [Password generator](./password_gen.py) - _Generate a random password of the given length, including uppercase and lowercase letters, and optionally numbers and symbols._
* [Password generator v2](./password_gen2.py) - _Generate password with complexity levels._
* [Word and character count](./word_count.py) - _Counts the number of words and characters._
* [Weather](./weather.py) - _Fetch essential weather information for a location._
* [Chatbot (ChatGPT)](./chatbot.py) - _Basic chatbot using OpenAI's ChatGPT._
* [URL Shortener](./shorten_url.py) - _Simple URL shortener._
* [BMI calculator](./bmi_calculator.py) - _Simple Body Mass Index calculator._
* [Encryption Tool](./encryption_tool.py) - _Encrypts plain messages using the Caesar Cipher algorithm._
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
| [OpenWeatherMap API](https://openweathermap.org/api) | Allowing users to obtain essential weather data for a specific location by making only one API call.
|[pyshorteners](https://pyshorteners.readthedocs.io/en/latest/apis.html#implemented-apis)|A simple URL shortening API wrapper Python library. This modules is essential to be able to shorten urls using various URL shortener services available including [tinyurl](https://tinyurl.com/app).

---
## Contributions
_Pending contribution guide._

## License
[MIT License](./LICENSE)

