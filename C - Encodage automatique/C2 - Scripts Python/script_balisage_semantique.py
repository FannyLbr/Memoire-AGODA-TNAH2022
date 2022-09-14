import re


# FONCTIONS PERMETTANT D'AJOUTER LES BALISES DE TYPE SÉMANTIQUE


def add_utterance(data):
    """
    Ajout de l'élément TEI "u" pour chaque boxe étiquetée "u" ou "u-beginning" et "u-end"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bu(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<u>', data[i]['text_ocr'], '</u>'])
            elif re.search(r"u-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<u>', data[i]['text_ocr']])
            elif re.search(r"u-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</u>'])
            else:
                pass
    return data


def add_comment(data):
    """
    Ajout de l'élément TEI "note" avec un attribut @type ayant pour valeur : soit "comment" pour chaque boxe étiquetée
    "comment" ou "comment-beginning", "comment-end", soit "result" pour chaque boxe étiquetée "result",
    soit "opening" pour chaque boxe étiquetée "opening", soit "closing" pour chaque boxe étiquetée "closing"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bcomment(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="comment">', data[i]['text_ocr'], '</note>'])
            elif re.search(r"comment-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="comment">', data[i]['text_ocr']])
            elif re.search(r"comment-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</note>'])
            elif re.search(r"result", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="result">', data[i]['text_ocr'], '</note>'])
            elif re.search(r"opening", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="opening">', data[i]['text_ocr'], '</note>'])
            elif re.search(r"closing", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="closing">', data[i]['text_ocr'], "</note>"])
            else:
                pass
    return data


def add_incident(data):
    """
    Ajout des éléments TEI "incident" et "desc" au niveau des parenthèses ouvrantes et fermantes pour chaque boxe
    étiquetée "incident" ou "incident-beginning" et "incident-end"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bincident(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('(', '<incident><desc>(').replace(')',
                                                                                                    ')</desc></incident>')
            elif re.search(r"incident-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('(', '<incident><desc>(')
            elif re.search(r"incident-end", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace(')', ')</desc></incident>')
            else:
                pass
    return data


def add_quote(data):
    """
    Ajout de l'élément TEI "quote" au niveau des guillemets ouvrants et fermants pour chaque boxe étiquetée "quote" ou
    "quote-beginning" et "quote-end"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bquote(?!-)\b", data[i]["comment"]):
                # data[i]['text_ocr'] = "".join(re.sub(r'«', r'<quote>«', data[i]['text_ocr']))
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('«', '<quote>«').replace('»', '»</quote>')
            elif re.search(r"quote-beginning", data[i]["comment"]):
                # changer sens seg quote ?
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('«', '<quote><seg>«')
            elif re.search(r"quote-end", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('»', '»</seg></quote>')

            else:
                pass
    return data
