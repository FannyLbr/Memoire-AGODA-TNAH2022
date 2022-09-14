import re, os


# FONCTIONS PERMETTANT DE NETTOYER LES DONNÉES

# Fonction qui est appelée dans la fonction "compilation"


def delete(data):
    """
    Supprime les données ayant pour étiquette "useless"
    :param data:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"useless", data[i]["comment"]):
                data[i]['text_ocr'] = "".join("")
            else:
                pass
    return data


# Fonction qui s'applique directement sur les fichiers XML créés


def clean_xml(path_to_xml):
    """
    Supprime les sauts de ligne marqués par le caractères \n et recolle les mots divisés suite à un saut de ligne
    :param path_to_xml:
    """
    for file_name in sorted([file for file in os.listdir(path_to_xml) if file.endswith('.xml')]):
        with open(os.path.join(path_to_xml, file_name)) as xml_file:
            xml = xml_file.read()
            xml = re.sub("(?<!-)\n", " ", xml)
            xml = re.sub("-\n", "", xml)
            xml_file.close()

            xml_cleaned = open(str(os.path.join(path_to_xml, file_name)), mode="w")
            xml_cleaned.write(xml)
    return xml
