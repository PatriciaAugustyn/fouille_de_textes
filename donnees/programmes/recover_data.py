from bs4 import BeautifulSoup
import requests
#import os


with open("../URLs/url_plat_ent.txt", "r") as urls:
    for i, line in enumerate(urls):
        link = line.strip()
        response = requests.get(link)
        data = response.text
        soup = BeautifulSoup(data, "lxml")

        site="" # variable qui prendra le nom du site pour chaque ligne

        if "750g" in line:
            site="750g"
            narrow_contents = soup.find_all(class_="is-12 is-8-desk u-overflow-hidden-desk")
        elif "chefsimon" in line:
            site="chefsimon"
            narrow_contents_1 = soup.find_all("div", {"data-controller": "recipe-show"}) # <div data-controller="recipe-show" data-recipe-show-target="ingredientsBloc" data-recipe-show-nb-persons-value="0" data-recipe-show-initial-values-value=""> : ingrédients
            narrow_contents_2 = soup.find_all(class_="flex flex-col") # instructions
            narrow_contents = narrow_contents_1 + narrow_contents_2
        elif "elle" in line:
            site="elle"
            narrow_contents = soup.find_all(class_="layout-grid__main")
        elif "marmiton" in line:
            site="marmiton"
            narrow_contents = soup.find_all(class_="recipeV2-container")
        elif "mesrecettesfaciles" in line:
            site="mesrecettesfaciles"
            narrow_contents_1 = soup.find_all(class_="tab-content mb-3") # ingrédients
            narrow_contents_2 = soup.find_all(class_="recipe-desc") # instructions
            narrow_contents = narrow_contents_1 + narrow_contents_2
        elif "regal" in line:
            site="regal"
            narrow_contents = soup.find_all(class_="content")
        else:
            continue

        for j, content in enumerate(narrow_contents):
            with open(f"../clean-text/train/plat/{site}_plat_{i+1}.html", "w", encoding="utf-8") as file:
                file.write(str(content))
