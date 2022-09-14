import re


# FONCTIONS PERMETTANT D'AJOUTER LES BALISES DE TYPE FORMEL


def add_seg(data):
    """
    Ajout de l'élément TEI "seg" pour chaque boxe étiquetée "seg" ou "seg-beginning" et "seg-end" à l'exception
    des "seg" couplés avec l'étiquette "quote-beginning" ou "quote-end"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bseg(?!-)\b", data[i]["comment"]) and not re.search(r"quote-beginning|quote-end",
                                                                                data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<seg>', data[i]['text_ocr'], '</seg>'])
            elif re.search(r"seg-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<seg>', data[i]['text_ocr']])
            elif re.search(r"seg-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</seg>'])
            else:
                pass
    return data


def add_signed(data):
    """
    Ajout de l'élément TEI "signed" pour chaque boxe étiquetée "signed"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"signed", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<signed>', data[i]['text_ocr'], '</signed>'])
            else:
                pass
    return data


def add_page_number(data, zwt, inc):
    """
    Ajout de l'élément TEI "pb" et de l'attribut @n pour chaque boxe étiquetée "page-number" et ajout de l'élément TEI
    "ref" et de l'attribut @target pour chaque boxe étiquetée "page-number-ref"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    :param zwt: variable contenant le numéro de la première page de la séance
    :param inc: incrémentation
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bbody\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<pb n="', data[i]['text_ocr'].split()[-1], '"/>'])
            elif re.search(r"\bpage-number(?!-)\b", data[i]["comment"]) and not re.search(r"body",
                                                                                                  data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<pb n="', str(zwt + inc), '"/>'])
            elif re.search(r"page-number-ref", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<ref target="#', str(zwt + inc), '"/>'])
            else:
                pass
    return data
