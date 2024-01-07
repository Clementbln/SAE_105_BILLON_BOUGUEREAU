from moyenne_UE1_S1 import calcul_moyennes_notes_UE1_S1
from moyenne_UE1_S1 import generate_html_file

# Appel de la fonction pour calculer les moyennes et générer le fichier HTML
donnees_UE1, donnees_UE1_S2, resultat, data_rows = calcul_moyennes_notes_UE1_S1()
generate_html_file("moyenne_UE1.html", "Moyenne UE1", ["Nom", "Prénom", "Moyenne UE1 S1", "Moyenne UE1 S2", "Résultat"], data_rows)