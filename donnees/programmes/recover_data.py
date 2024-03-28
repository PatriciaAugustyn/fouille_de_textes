from bs4 import BeautifulSoup
import requests
#import os


with open("../URLs/larecette_url_dessert_test.txt", "r") as urls:
    for i, line in enumerate(urls):
        link = line.strip()
        response = requests.get(link)
        data = response.text
        soup = BeautifulSoup(data, "lxml")

        narrow_contents = soup.find_all(class_="g1-content-narrow")

        for j, content in enumerate(narrow_contents):
            with open(f"../clean-text/test/dessert/larecette_dessert_{i+1}.html", "w", encoding="utf-8") as file:
                file.write(str(content))
