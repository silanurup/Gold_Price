from bs4 import BeautifulSoup as Soup
import requests

def fetch_gold_price(search_url):
    response = requests.get(search_url)
    html_content = Soup(response.text, 'html.parser')
    price_element = html_content.find("div", class_="BNeawe iBp4i AP7Wnd").text
    return price_element

search_query_url = "https://www.google.com/search?q=gold+price"
current_price = fetch_gold_price(search_query_url)
print("Current Gold Price:", current_price)
