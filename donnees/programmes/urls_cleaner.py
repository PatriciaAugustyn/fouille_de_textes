etiquettes=["aperitif", "entree", "plat", "dessert", "boisson"]

for i in range(len(etiquettes)):
    txt = open(f"../URLs/all_url_{etiquettes[i]}_ent.txt", "r")
    urls = txt.readlines()
    txt.close()

    urls_nettoyees = []
    for url in urls:
        if url not in urls_nettoyees:
            urls_nettoyees.append(url)
        else:
            continue

    txt_nettoye = open(f"../URLs/all_url_{etiquettes[i]}_ent_clean.txt", "a")
    txt_nettoye.writelines(urls_nettoyees)
    txt_nettoye.close()