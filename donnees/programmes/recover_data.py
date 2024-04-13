from bs4 import BeautifulSoup
import requests
from lxml import html
#import os

etiquettes=["entree", "plat", "dessert", "aperitif", "boisson"]

for num_eti in range(len(etiquettes)):
    etiquette = etiquettes[num_eti]

    with open(f"../URLs/url_{etiquette}_ent.txt", "r") as urls:
        for i, line in enumerate(urls):
            link = line.strip()
            response = requests.get(link)

            #pour ceux qui utilisent lxml avec xpath (div qui n'ont pas de nom)
            #tree = html.fromstring(response.content)

            # pour ceux qui utilisent beautifusoup
            data = response.text
            soup = BeautifulSoup(data, "lxml")

            site="" # variable qui prendra le nom du site de chaque ligne/url
            narrow_contents=[]
            content_html=""

            if "750g" in line:
                site="750g"
                narrow_contents = soup.find_all(class_="recipe-section recipe-steps") # instructions
            elif "chefsimon" in line:
                site="chefsimon"
                narrow_contents = soup.find_all(class_="flex flex-col")
                #narrow_contents = soup.find_all(class_="text-sm text-black-200 link_cs") # instructions
                #content_html = tree.xpath('/html/body/div[2]/div/div[1]/div[4]/div/text')
            elif "Elle-a-Table" in line:
                site="elle"
                narrow_contents = soup.find_all(class_="article-body") # ingrédients + instructions
            elif "marmiton" in line:
                site="marmiton"
                narrow_contents = soup.find_all(class_="recipeV2-container") # ingrédients + instructions
            elif "mesrecettesfaciles" in line:
                site="mesrecettesfaciles"
                narrow_contents = soup.find_all(class_="recipe-desc") # instructions
            elif "regal" in line:
                site="regal"
                narrow_contents = soup.find_all(
                    class_="clearfix recipe-block group-description field-group-html-element"
                ) # ingrédients + instructions
            elif "larecette" in line:
                site = "larecette"
                narrow_contents = soup.find_all(
                    class_="g1-content-narrow g1-typography-x1 entry-content"
                )  # ingrédients + instructions
            elif "cuisineactuelle" in line:
                site = "cuisineactuelle"
                narrow_contents = soup.find_all(
                    class_="recipe-content"
                )  # ingrédients + instructions

            else:
                print(line, " : site pas reconnu")

            if narrow_contents:
                for j, content in enumerate(narrow_contents):
                    with open(f"../clean-text/train/{etiquette}/{i+1}_{site}_{etiquette}.html", "w", encoding="utf-8") as file:
                        file.write(str(content))
            #elif content_html:
                #with open(f"../clean-text/train/{etiquette}/{i + 1}_{site}_{etiquette}.html", "w", encoding="utf-8") as file:
                    #file.write(str(content_html))
