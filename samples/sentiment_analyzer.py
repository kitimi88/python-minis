import os
import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# This project requires NLTK Data.
# Enable or uncomment the nltk.download('vader_lexicon') line.
# https://www.nltk.org/data.html#installing-nltk-data


# nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def predict_sentiment(text):
    sentiment_score = sia.polarity_scores(text)

    if sentiment_score['compound'] >= 0.05:
        return 'Postive'
    
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    
    else:
        return 'Neutral'

def user_input():
    while True:
        try:
            text = str(input('Enter phrase you want to analyze: '))
            break
        except ValueError:
            print('Error: Input must be a string.')
            return
    
    sentiment = predict_sentiment(text)
    print("\nThe sentiment is classified as:", sentiment)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Sentiment Analyzer'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    user_input()

    while True:
        response = input('\nDo you want to continue? (Y/N)')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day!\n')
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main()       

