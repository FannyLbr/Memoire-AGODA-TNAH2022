import re

# FONCTIONS PERMETTANT D'AJOUTER LES BALISES DE TYPE LOGIQUE


def add_structure(data):
    """
    Ajout des éléments TEI "text" "body" et "back" pour chaque boxe étiquetée "body", "text", "back", "text-back"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bbody\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<text><body>', data[i]['text_ocr']])
            # elif re.search(r"body1", data[i]["comment"]):
            # data[i]['text_ocr'] = "".join('<text><body><pb n="1"/>')
            elif re.search(r"\btext(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('</div></body></text>')
            elif re.search(r"\b(?<!-)back\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</div></div></body><back>'])
            elif re.search(r"text-back", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('</div></div></back></text>')
            else:
                pass
    return data


def add_division(data):
    """
    Ajout de l'élément TEI "div" pouvant avoir un attribut @type auant pour valeur soit "part", soit "agenda",
    soit "appendices", soit "erratum", soit "lists", soit "offices", soit "sitting", soit "other-sitting",
    soit "contents", soit "voting", soit "rectification", soit "petition" pour chaque boxe étiquetée "part", "part1",
    "agenda", "appendices", "part1-appendices", "erratum", "part1-erratum", "lists", "part1-lists", "offices",
    "part1-offices", "sitting", "other-sitting", "contents", "voting1", "voting", "div-end", "rectification",
    "petition" ou "part1-petition"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bpart\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="part">', data[i]['text_ocr']])
            elif re.search(r"part1(?!-)", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="part">', data[i]['text_ocr']])
            elif re.search(r"agenda", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="agenda"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\b(?<!-)appendices\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="appendices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"part1-appendices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="appendices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\b(?<!-)erratum\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="erratum"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-erratum", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="erratum"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"\b(?<!-)lists\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="lists"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-lists", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="lists"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"\b(?<!-)offices\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="offices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"part1-offices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="offices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\b(?<!-)sitting\b", data[i]["comment"]) and re.search(r"contents", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="sitting"><div type="contents"><head>', data[i]['text_ocr'], '</head><list>'])
            elif re.search(r"other-sitting", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="other-sitting"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"voting1", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"\bvoting\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"div-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</div>'])
            elif re.search(r"rectification", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div></div><div type="rectification"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\b(?<!-)petition\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="petition"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-petition", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="petition"><head><label>', data[i]['text_ocr'], '</label>'])
            else:
                pass
    return data


def add_structural_comment(data):
    """
    Ajout de l'élément TEI "note" pour chaque boxe étiquetée "note" et "note-end", et pouvant avoir aussi un attribut
    @type ayant pour valeur soit "voterslist", soit "numbersannounced" pour chaque boxe étiquetée "voterslist-beginning"
    ou "note-beginning"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bnote(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note>'])
            elif re.search(r"voterslist-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="voterslist"><desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"note-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="numbersannounced">', data[i]['text_ocr']])
            elif re.search(r"note-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</note>'])
            else:
                pass
    return data


def add_item(data):
    """
    Ajout de l'élément TEI "item" pour chaque boxe étiquetée "item" ou "item-list"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bitem(?!-)\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item>'])
            elif re.search(r"item-list", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item></list>'])
            else:
                pass
    return data


def add_title(data):
    """
    Ajout des éléments TEI "head", "desc" et "note" pour chaque boxe étiquetée "head", "desc" ou "note-head"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\b(?<!-)head\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"desc", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"note-head", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note></head>'])
            else:
                pass
    return data


def add_table(data):
    """
    Ajout des éléments TEI "table" "row" et "cell" pour chaque boxe étiquetée "table"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"table", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<table><row><cell>', data[i]['text_ocr'], '</cell></row></table>'])
            else:
                pass
    return data
