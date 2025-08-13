import requests
from bs4 import BeautifulSoup

def scrape_hindustantimes_news():
    URL = 'https://www.hindustantimes.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        news_cards = soup.find_all('div', class_='cartHolder listView track timeAgo')

        for news_card in news_cards:
            headline = news_card.get('data-vars-story-title')
            print(f"Headline: {headline}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")

if __name__ == '__main__':
    scrape_hindustantimes_news()
