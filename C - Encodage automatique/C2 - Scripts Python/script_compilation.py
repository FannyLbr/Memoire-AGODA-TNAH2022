from script_balisage_formel import add_seg, add_signed, add_page_number
from script_balisage_semantique import add_utterance, add_comment, add_incident, add_quote
from script_balisage_logique import add_structure, add_division, add_structural_comment, add_item, add_title, add_table
from script_nettoyage import delete


# FONCTION PRINCIPALE PERMETTANT D'APPELER UN ENSEMBLE DE FONCTIONS


def compilation(x, zwt, inc):
    """
    Appel des fonctions dans un ordre bien précis afin d'ajouter l'ensemble des balises enfants de "text" sur les données
    :param x: variable contenant les données à baliser
    :param zwt: variable contenant le numéro de la première page de la séance
    :param inc: incrémentation
    """
    # 1
    add_quote(x)

    # 2
    add_incident(x)

    # 3
    add_seg(x)

    # 4
    add_utterance(x)

    # 5
    add_comment(x)

    # 6
    add_signed(x)

    # 7
    add_table(x)

    # 8
    add_structural_comment(x)

    # 9
    add_item(x)

    # 10
    add_title(x)

    # 11
    add_division(x)

    # 12
    add_page_number(x, zwt, inc)

    # 13
    add_structure(x)

    # 14
    delete(x)

    return
