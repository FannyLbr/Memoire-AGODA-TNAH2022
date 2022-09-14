import json, os, re
from lxml import etree
from script_compilation import compilation
from script_nettoyage import clean_xml
from script_metadonnees import var_metadata, build_teiheader

# Variables stockant les chemins vers les fichiers JSON et les fichiers XML
path = os.path.dirname(__file__)
path_to_json = os.path.join(os.path.abspath(os.path.join(path, os.pardir)), "json_data")
path_to_xml = os.path.join(os.path.abspath(os.path.join(path, os.pardir)), "xml_data")

# Variables stockant l'élément racine TEI
beginning_elements = '<?xml version="1.0" encoding="UTF-8"?> <?xml-model ' \
                     'href="agoda_schema.rng" ' \
                     'type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?> <?xml-model ' \
                     'href="agoda_schema.rng" ' \
                     'type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?> <TEI ' \
                     'xmlns="http://www.tei-c.org/ns/1.0" xml:lang="fr"> '
end_elements = '</TEI>'

# OUVERTURE DES FICHIERS JSON : boucle permettant de lire chaque fichier JSON dont le nom finit par ".json" contenu dans
# un dossier dont le chemin est donné

for file_name in sorted([file for file in os.listdir(path_to_json) if file.endswith('.json')]):
    with open(os.path.join(path_to_json, file_name), encoding='utf-8') as json_file:
        data = json.load(json_file)

        # CHANGEMENTS DE PAGE : gestion de l'incrémentation à partir du numéro de la première page de la séance
        for i in range(len(data)):
            if "comment" in data[i]:
                if re.search(r"\bbody\b", data[i]["comment"]):
                    inc = 0
                    zwt = int(data[i]['text_ocr'].split()[-1])
                elif re.search(r"page-number", data[i]["comment"]) and not re.search(r"body", data[i]["comment"]):
                    data[i]['text_ocr'] = "".join(['<pb n="', str(zwt + inc), '"/>'])
                    inc += 1
                elif re.search(r"page-number-ref", data[i]["comment"]):
                    data[i]['text_ocr'] = "".join(['<ref target="#', str(zwt + inc), '"/>'])
                    inc += 1

        # MÉTADONNÉES : appel des variables des métadonnées et application de la fonction build_teiheader
        date_pub, meetings, meeting_sitting, date_sitting = var_metadata(data)
        header = build_teiheader(date_pub, meetings, meeting_sitting, date_sitting)

        # ÉLÉMENTS TEI POUR LE TEXTE : application de la fonction compilation
        compilation(data, zwt, inc)

        # CRÉATION DES FICHIERS XML
        for i in range(len(data)):
            if "comment" in data[i]:
                # Création d'un fichier XML pour chaque début de séance, l'étiquette "body" marque le début de la séance
                if "body" in data[i]["comment"]:
                    # Nommage des fichiers XML
                    name = json_file
                    file_name1 = re.split(r"_p", file_name)[0]
                    output_xml = open(str(os.path.join(path_to_xml, file_name1 + ".xml")), mode="w")
                    # Écriture de l'élément racine et des métadonnées
                    output_xml.write(beginning_elements)
                    output_xml.write(header)

            # Boucle permettant d'écrire dans le fichier XML tout ce qui est contenu dans la clef "text_ocr" de data
            if "text_ocr" in data[i]:
                if len(data[i]["text_ocr"]) > 0:
                    output_xml.write(data[i]['text_ocr'])

                    # Ajouter un espace entre le texte de deux boxes
                    output_xml.write(" ")

            # Écriture de la balise fermante de l'élément racine, l'étiquette "text" marque la fin de la séance
            if "comment" in data[i]:
                if "text" in data[i]["comment"]:
                    output_xml.write(end_elements)
output_xml.close()

# Appliquer la fonction clean_xml permettant de gérer les espaces au sein des boxes
clean_xml(path_to_xml)

# ---------------------------------------------------------------------------------------------------------------------

# GESTION DU FICHIER CORPUS : ajout des xi:include dans le teiCorpus

# Variables
my_tree = etree.parse(os.path.join(path_to_xml, 'FR_3R_5L.xml'))
my_root = my_tree.getroot()
namespace = 'http://www.w3.org/2001/XInclude'

# Boucle permettant de récupérer l'ensemble des noms de fichiers composants
for file_name in sorted([file for file in os.listdir(path_to_xml) if file.endswith('.xml')]):
    if len(str(file_name)) > 12:
        # Ouverture du fichier XML corpus
        f = open(os.path.join(path_to_xml, 'FR_3R_5L.xml'), mode="r")
        text = f.read()
        # Condition permettant d'éviter de dupliquer l'inclusion d'un même fichier composant
        if re.search(file_name, text):
            continue

        # Création des éléments xi:include avec pour attributs @xmlns:xi contenant l'espace de nom
        # et @href contenant les noms des fichiers composants

        my_root.append(etree.Element(etree.QName(namespace, 'include'), nsmap={'xi': namespace},
                                     attrib={'href': str(file_name)}))

# Écriture dans le fichier XML corpus des inclusions effectuées
file_to_save = os.path.join(path_to_xml, 'FR_3R_5L.xml')
my_tree.write(file_to_save, pretty_print=True, encoding='utf-8', xml_declaration=True)

# ---------------------------------------------------------------------------------------------------------------------
# # CODE À REPRENDRE
# # Vérification du respect du schéma relaxNG
#
# # Ouverture du fichier rng
# relaxng_doc = etree.parse(os.path.join(path_to_xml, 'agoda_schema.rng'))
#
# # Association comme étant un schéma relaxNG
# relaxng = etree.RelaxNG(relaxng_doc)
#
# # Vérification des erreurs sur l'ensemble des fichiers XML
# relaxng.assertValid(my_tree)

# ---------------------------------------------------------------------------------------------------------------------
