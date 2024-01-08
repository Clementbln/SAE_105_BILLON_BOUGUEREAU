def generate_html_file(file_name, title, column_titles, data_rows):
    #Contenu HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="global.css" />
    </head>
    <body>
        <h1>{title}</h1>
        <table>
            <tr>
                {''.join(f'<th>{col}</th>' for col in column_titles)}
            </tr>
            {''.join(f'<tr>{"".join(f"<td>{data}</td>" for data in row)}</tr>' for row in data_rows)}
        </table>
    </body>
    </html>
    """

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
