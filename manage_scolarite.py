import os
import xml.etree.ElementTree as ET

CLASSES_FILE = "scolarite.xml"

def init_file():
    if not os.path.exists(CLASSES_FILE):
        root = ET.Element("scolarite")
        ET.SubElement(root, "fillieres")
        ET.SubElement(root, "etudiants")
        tree = ET.ElementTree(root)
        tree.write(CLASSES_FILE)

def load_data():
    tree = ET.parse(CLASSES_FILE)
    root = tree.getroot()
    return tree, root

def create_classe(name):
    tree, root = load_data()
    fillieres = root.find("fillieres")
    next_id = len(fillieres) + 1
    filiere = ET.SubElement(fillieres, "filiere")
    ET.SubElement(filiere, "idF").text = str(next_id)
    ET.SubElement(filiere, "nameF").text = name
    tree.write(CLASSES_FILE)
    print("Filière ajoutée avec succès!")

def read_classes():
    tree, root = load_data()
    print("Liste des filières :")
    for filiere in root.find("fillieres"):
        print(f"ID: {filiere.find('idF').text}, Nom: {filiere.find('nameF').text}")

def create_etudiant(name, email, classe_id):
    tree, root = load_data()
    etudiants = root.find("etudiants")
    next_id = len(etudiants) + 1
    etudiant = ET.SubElement(etudiants, "etudiant")
    ET.SubElement(etudiant, "idE").text = str(next_id)
    ET.SubElement(etudiant, "nameE").text = name
    ET.SubElement(etudiant, "email").text = email
    ET.SubElement(etudiant, "classe_id").text = classe_id
    tree.write(CLASSES_FILE)
    print("Étudiant ajouté avec succès!")

def read_etudiants():
    tree, root = load_data()
    print("Liste des étudiants :")
    for etudiant in root.find("etudiants"):
        classe_name = get_classe_name(etudiant.find("classe_id").text)
        print(f"ID: {etudiant.find('idE').text}, Nom: {etudiant.find('nameE').text}, Email: {etudiant.find('email').text}, Classe: {classe_name}")

def update_etudiant(etudiant_id, name, email, classe_id):
    tree, root = load_data()
    etudiants = root.find("etudiants")
    for etudiant in etudiants:
        if etudiant.find("idE").text == etudiant_id:
            etudiant.find("nameE").text = name
            etudiant.find("email").text = email
            etudiant.find("classe_id").text = classe_id
            tree.write(CLASSES_FILE)
            print("Étudiant mis à jour avec succès!")
            return
    print("Étudiant introuvable.")

def delete_etudiant(etudiant_id):
    tree, root = load_data()
    etudiants = root.find("etudiants")
    for etudiant in etudiants:
        if etudiant.find("idE").text == etudiant_id:
            etudiants.remove(etudiant)
            tree.write(CLASSES_FILE)
            print("Étudiant supprimé avec succès!")
            return
    print("Étudiant introuvable.")

def get_classe_name(classe_id):
    tree, root = load_data()
    for filiere in root.find("fillieres"):
        if filiere.find("idF").text == classe_id:
            return filiere.find("nameF").text
    return "Filière inconnue"

def main():
    init_file()
    while True:
        print("\n*** Gestion de la Scolarité ***")
        print("1. Ajouter une filière")
        print("2. Afficher les filières")
        print("3. Ajouter un étudiant")
        print("4. Afficher les étudiants")
        print("5. Mettre à jour un étudiant")
        print("6. Supprimer un étudiant")
        print("7. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            name = input("Nom de la filière : ")
            create_classe(name)
        elif choice == "2":
            read_classes()
        elif choice == "3":
            name = input("Nom de l'étudiant : ")
            email = input("Email de l'étudiant : ")
            classe_id = input("ID de la classe : ")
            create_etudiant(name, email, classe_id)
        elif choice == "4":
            read_etudiants()
        elif choice == "5":
            student_id = input("ID de l'étudiant à mettre à jour : ")
            name = input("Nouveau nom : ")
            email = input("Nouvel email : ")
            classe_id = input("Nouvelle filière (ID) : ")
            update_etudiant(student_id, name, email, classe_id)
        elif choice == "6":
            student_id = input("ID de l'étudiant à supprimer : ")
            delete_etudiant(student_id)
        elif choice == "7":
            print("Bye !")
            break
        else:
            print("Option invalide.")

main()
