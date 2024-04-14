from bs4 import BeautifulSoup
import requests

etiquettes=["entree", "plat", "dessert", "aperitif", "boisson"]

for num_eti in range(len(etiquettes)):
    etiquette = etiquettes[num_eti]

    with open(f"../URLs/all_url_{etiquette}_ent.txt", "r") as urls:
        for i, line in enumerate(urls):
            i+=1 # pour ne pas commencer à 0

            link = line.strip()
            response = requests.get(link)
            data = response.text
            soup = BeautifulSoup(data, "lxml")

            site="" # variable qui prendra le nom du site de chaque ligne/url
            narrow_contents=[]
            content_html=""

            if "750g" in line:
                site="750g"
                narrow_contents = soup.find_all(class_="recipe-section recipe-steps") # instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "chefsimon" in line:
                site="chefsimon"
                narrow_contents = soup.find_all(class_="flex flex-col")
                if narrow_contents == []:
                    i-=1
                    continue
            elif "Elle-a-Table" in line:
                site="elle"
                narrow_contents = soup.find_all(class_="article-body") # ingrédients + instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "marmiton" in line:
                site="marmiton"
                narrow_contents = soup.find_all(class_="recipeV2-container") # ingrédients + instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "mesrecettesfaciles" in line:
                site="mesrecettesfaciles"
                narrow_contents = soup.find_all(class_="recipe-desc") # instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "regal" in line:
                site="regal"
                narrow_contents = soup.find_all(
                    class_="clearfix recipe-block group-description field-group-html-element"
                ) # ingrédients + instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "larecette" in line:
                site = "larecette"
                narrow_contents = soup.find_all(
                    class_="g1-content-narrow g1-typography-x1 entry-content"
                )  # ingrédients + instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "cuisineactuelle" in line:
                site = "cuisineactuelle"
                narrow_contents = soup.find_all(class_="recipe-content")  # ingrédients + instructions
                if narrow_contents == []:
                    i-=1
                    continue
            elif "cuisineaz" in line:
                site = "cuisineaz"
                narrow_contents = soup.find_all(class_="borderSection instructions") # instructions
                if narrow_contents == []:
                    i-=1
                    continue
            else:
                print(line, " : site pas reconnu")


            if narrow_contents != []:
                for j, content in enumerate(narrow_contents):
                    if 0<i<10:
                        k = "00"+str(i)
                    elif 10<=i<=99:
                        k = "0"+str(i)
                    elif i>=100:
                        k=str(i)
                    with open(f"../clean-text/all/{etiquette}/{k}_{etiquette}_{site}.html", "w", encoding="utf-8") as file:
                        file.write(str(content))
    print("Aspiration terminée !")

