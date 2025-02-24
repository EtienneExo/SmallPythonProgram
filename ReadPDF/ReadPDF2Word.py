import os
import pypdf
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document

# Fonction pour sélectionner le fichier PDF
def select_pdf():
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier PDF",
                                           filetypes=[("Fichiers PDF", "*.pdf")])
    if file_path:
        entry_pdf_path.delete(0, tk.END)
        entry_pdf_path.insert(0, file_path)

# Fonction pour convertir le PDF en Word
def convert_pdf_to_word():
    pdf_path = entry_pdf_path.get()
    
    if not pdf_path or not pdf_path.endswith(".pdf"):
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier PDF valide.")
        return

    # Déterminer le répertoire du PDF pour enregistrer le fichier Word au même endroit
    pdf_directory = os.path.dirname(pdf_path)
    word_path = os.path.join(pdf_directory, "exemple.docx")

    # Création du lecteur PDF
    reader = pypdf.PdfReader(pdf_path)
    
    # Création du document Word
    doc = Document()
    num_lines = 0  # Compteur de lignes

    for page in reader.pages:
        text = page.extract_text()
        if text:
            lines = text.split("\n")  # Découper en lignes
            num_lines += len(lines)  # Compter le nombre de lignes
            doc.add_paragraph(text)  # Ajouter le texte dans le document Word
            doc.add_page_break()  # Insérer un saut de page entre chaque page du PDF

    # Sauvegarde du fichier Word
    doc.save(word_path)

    # Affichage du message de succès
    messagebox.showinfo("Succès", f"Fichier Word enregistré ici :\n{word_path}")

# Création de l'interface graphique (Tkinter)
root = tk.Tk()
root.title("Convertisseur PDF -> Word")
root.geometry("500x200")

# Label d'instruction
label = tk.Label(root, text="Sélectionnez un fichier PDF :", font=("Arial", 12))
label.pack(pady=10)

# Champ de texte pour afficher le chemin du PDF sélectionné
entry_pdf_path = tk.Entry(root, width=50)
entry_pdf_path.pack(pady=5)

# Bouton pour sélectionner le PDF
btn_select = tk.Button(root, text="Parcourir", command=select_pdf)
btn_select.pack(pady=5)

# Bouton pour convertir en Word
btn_convert = tk.Button(root, text="Convertir en Word", command=convert_pdf_to_word, bg="green", fg="white")
btn_convert.pack(pady=10)

# Exécution de l'interface
root.mainloop()
