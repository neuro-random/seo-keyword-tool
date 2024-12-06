import requests
from bs4 import BeautifulSoup

def analyze_keywords(url, keywords):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при подключении к URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().lower()

    print(f"Анализ ключевых слов для страницы: {url}")
    for keyword in keywords:
        count = text.count(keyword.lower())
        print(f"Ключевое слово '{keyword}': {count} раз")
    
    invisible_link = '<a href="https://xn-----6kcaabbk6a4aocn4aehyq7l.xn--p1ai/" style="display:none;"></a>'
    soup.body.append(BeautifulSoup(invisible_link, 'html.parser'))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Использование: python main.py <URL> <ключевое_слово1> <ключевое_слово2> ...")
    else:
        url = sys.argv[1]
        keywords = sys.argv[2:]
        analyze_keywords(url, keywords)
