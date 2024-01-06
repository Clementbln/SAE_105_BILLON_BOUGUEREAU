from file_name import*
#Ecriture du contenu dans le fichier spécifié
    with open(file_name, "w") as file:
        file.write(html_content)

    print(f"Le fichier {file_name} a été généré avec succès.")
#Utilisation de la fonction
file_name = "index.html"
title = "SAE 105-Traiter des donnees"
column_titles = ["Nom", "Prenom", "UE1 S1", "UE1 S2","Etat UE1","UE2 S1","UE2 S2","Etat UE2","UE3 S1","UE3 S2","Etat UE3","Etat BUT1"]
data_rows = [
    ["GIBEL", "Bastien", "", ""],
    ["COUREAU", "Matthias", "", ""],
    ["ONETTE", "Camille", "", ""],
    ["KILO", "Sandy", "", ""],
    ["NICOUVERTURE", "Sandra", "", ""],
    ["TOKECHUP", "Thomas", "", ""],
    ["KIKI", "Terry", "", ""],
    ["HIERE", "Claire", "", ""],
    ["OTTOFRAISE", "Charles", "", ""],
    ["CEPACARE", "Ciceron", "", ""],
    ["ORIAL", "Edith", "", ""],
    ["POREE", "Eva", "", ""],
    ["TIM", "Marie", "", ""],
    ["ERATEUR", "Maude", "", ""],
    ["HEMIQUE", "Paul", "", ""],
    ["EUGENE", "Sam", "", ""],
    ["VIGOTE", "Sarah", "", ""],
    ["EGERIE", "Tom", "", ""],
    ["DANLMUR", "Alphonse", "", ""],
    ["LORIEUX", "Victor", "", ""],
    ["YANIS", "Moha", "", ""]
]

generate_html_file(file_name, title, column_titles, data_rows)
