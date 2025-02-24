import pypdf
import os
from docx import Document

# Chemin du fichier PDF
pdf_path = r"C:\TestPy\exemple.pdf"

# Déterminer le répertoire du PDF pour enregistrer le fichier Word au même endroit
pdf_directory = os.path.dirname(pdf_path)
output_path = os.path.join(pdf_directory, "exemple.docx")

# Création du lecteur PDF
reader = pypdf.PdfReader(pdf_path)

# Création d'un document Word
doc = Document()

# Extraction et sauvegarde du texte
num_lines = 0  # Compteur de lignes

for page in reader.pages:
    text = page.extract_text()
    if text:  # Vérifier si du texte a été extrait
        lines = text.split("\n")  # Découper en lignes
        num_lines += len(lines)  # Compter le nombre de lignes
        doc.add_paragraph(text)  # Ajouter le texte dans le document Word
        doc.add_page_break()  # Insérer un saut de page entre les pages du PDF

# Sauvegarde du fichier Word
doc.save(output_path)

# Affichage des résultats
print(f"Fichier Word enregistré ici : {output_path}")
print(f"Nombre de pages extraites : {len(reader.pages)}")
print(f"Nombre de lignes enregistrées : {num_lines}")
