import re
from datetime import date


# FONCTIONS PERMETTANT D'INCLURE LES MÉTADONNÉES (teiHeader)


def var_metadata(data):
    """
    Création de variables permettant de stocker certaines parties du texte relatives aux métadonnées à l'aide des
    étiquettes "date-pub", "meeting-legislature", "meeting-session", "meeting-sitting", "date-sitting"
    :param data: dictionnaire contenant l'ensemble des données issues des JSON
    """
    # Pour appeler les variables dans le return
    global date_pub
    global meetings
    global meeting_sitting
    global date_sitting

    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"date-pub", data[i]["comment"]):
                date_pub = "".join(['<date>', str(" ".join(data[i]['text_ocr'].split()[3:6])), '</date>'])

            elif re.search(r"meeting-legislature", data[i]["comment"]) and re.search(r"meeting-session",
                                                                                     data[i]["comment"]):
                meetings = "".join(['<meeting n="', str(data[i]['text_ocr'].split()[0]),
                                    'L" ana="#parla.lower #parla.legislature">',
                                    str(" ".join(data[i]['text_ocr'].split()[:2])), '</meeting>',
                                    '<meeting n="E1" ana="#parla.lower #parla.session">',
                                    str(" ".join(data[i]['text_ocr'].split()[-4:])), '</meeting>'])
            elif re.search(r"meeting-sitting", data[i]["comment"]):
                meeting_sitting = "".join(['<meeting n="', str(data[i]['text_ocr'].split()[-2]),
                                           '" ana="#parla.lower #parla.sitting">',
                                           str(" ".join(data[i]['text_ocr'].split()[-2:])), '</meeting>'])
            elif re.search(r"date-sitting", data[i]["comment"]):
                date_sitting = "".join(['<date>', str(" ".join(data[i]['text_ocr'].split()[-3:])), '</date>'])
            else:
                pass

    return date_pub, meetings, meeting_sitting, date_sitting


def build_teiheader(date_pub, meetings, meeting_sitting, date_sitting):
    """
    Création de l'ensemble du teiHeader avec l'insertion des variables définies dans "var_meta"
    :param date_pub: variable contenant la date de publication, information issue des données contenues dans data
    :param meetings: variable contenant la date de la législature et le type de session, informations issues des données
    contenues dans data
    :param meeting_sitting: variable contenant le numéro de la séance, information issue des données contenues dans data
    :param date_sitting: variable contenant la date de la séance, information issue des données contenues dans data
    """
    return "".join(['<teiHeader>',
                    '<fileDesc>'
                    '<titleStmt>',
                    '<title type="main" xml:lang="fr">Journal officiel de la République française. Débats '
                    'parlementaires</title>',
                    '<title type="main" xml:lang="en">Official Journal of the French Republic. Parliamentary '
                    'debates</title>',
                    '<title type="sub" xml:lang="fr">Chambre des députés : compte rendu in-extenso</title>',
                    '<title type="sub" xml:lang="en">Chamber of Deputies: verbatim report</title>',
                    str(meetings),
                    str(meeting_sitting),
                    '<respStmt>',
                    '<persName>',
                    '<forename>Fanny</forename>',
                    '<surname>Lebreton</surname>',
                    '<ptr type="id-hal" target="fanny-lebreton"/>',
                    '</persName>',
                    '<resp xml:lang="fr">Transformation du JSON en XML-TEI et ajout automatique des balises TEI par '
                    'des scripts Python</resp>',
                    '<resp xml:lang="en">Transformation from JSON to XML-TEI and automatic addition of TEI tags by '
                    'Python scripts</resp>',
                    '</respStmt>',
                    '<respStmt>',
                    '<persName>',
                    '<forename>Marie</forename>',
                    '<surname>Puren</surname>',
                    '<ptr type="id-hal" target="marie-puren"/>',
                    '<ptr type="orcid" target="0000-0001-5452-3913"/>',
                    '</persName>',
                    '<resp xml:lang="fr">TEI Header</resp>',
                    '<resp xml:lang="en">TEI Header</resp>',
                    '</respStmt>',
                    '<funder>',
                    '<orgName xml:lang="fr">Bibliothèque nationale de France</orgName>',
                    '<orgName xml:lang="en">National Library of France</orgName>',
                    '</funder>',
                    '</titleStmt>',
                    '<publicationStmt>',
                    '<publisher>AGODA</publisher>',
                    '<authority>Bnf DataLab</authority>',
                    '<availability status="restricted" n="cc-by">',
                    '<licence target="https://creativecommons.org/licenses/by/4.0/"/>',
                    '</availability>',
                    '<date when="', str(date.today().strftime("%Y-%m-%d")), '"/>',
                    '</publicationStmt>',
                    '<sourceDesc>',
                    '<biblFull>',
                    '<titleStmt>',
                    '<title>Journal officiel de la République française. Débats parlementaires. Chambre des députés : '
                    'compte rendu in-extenso</title>',
                    '</titleStmt>',
                    '<publicationStmt>',
                    '<publisher xml:lang="fr">Pas d\'information disponible</publisher>',
                    '<publisher xml:lang="en">No information available</publisher>',
                    '<pubPlace>',
                    '<location>',
                    '<country key="FR"/>',
                    '<settlement type="city">Paris</settlement>',
                    '</location>',
                    '</pubPlace>',
                    str(date_pub),
                    '<distributor facs="https://gallica.bnf.fr/ark:/12148/bpt6k477552f/f1">Source gallica.bnf.fr / '
                    'Bibliothèque nationale de France</distributor>',
                    '<availability>', '<licence xml:lang="fr" target="https://gallica.bnf.fr/edit/und/conditions'
                                      '-dutilisation-des-contenus-de-gallica">',
                    '<p>Les contenus accessibles sur le site Gallica sont pour la plupart des reproductions numériques '
                    'd\'œuvres tombées dans le domaine public provenant des collections de la BnF.</p>',
                    '<p>Ces contenus sont considérés, en vertu du code des relations entre le public et '
                    'l\'administration, comme étant des informations publiques et leur réutilisation s\'inscrit dans '
                    'le cadre des dispositions prévues aux articles L. 321-1 à L. 327-1 de ce code.</p>',
                    '</licence>',
                    '</availability>',
                    '</publicationStmt>',
                    '<seriesStmt>',
                    '<title>Journal Officiel de la République française</title>',
                    '<biblScope unit="series">Débats parlementaires</biblScope>',
                    '<biblScope unit="volume">Chambre des députés</biblScope>',
                    '<idno type="ISSN">1270-5942</idno>',
                    '</seriesStmt>',
                    '</biblFull>',
                    '</sourceDesc>',
                    '</fileDesc>',
                    '<encodingDesc>',
                    '<projectDesc>',
                    '<p xml:lang="fr"><ref target="https://www.bnf.fr/fr/les-projets-de-recherche#bnf-agoda">AGODA'
                    '</ref> est un projet qui a pour objectif de rendre disponible au format XML-TEI les textes de '
                    'débats parlementaires à la Chambre des députés au cours de la TroisièmeRépublique, '
                    'suivant l\'<ref target="https://github.com/mpuren/agoda/blob/ODD/documentation'
                    '/agoda_documentation.xml">ODD</ref> défini pour le projet à partir des <ref '
                    'target="https://github.com/clarin-eric/parla-clarin">recommandations produites par '
                    'Parla-CLARIN</ref>. Dans une optique de preuve de concept, la phase 1 du projet AGODA se '
                    'concentre plus particulièrement sur la 5ème législature (1889-1893). Les textes encodés sont '
                    'd\'abord extraits des documents numérisés disponibles sur <ref '
                    'target="https://gallica.bnf.fr/ark:/12148/cb328020951/date.item">Gallica</ref>, la bibliothèque '
                    'numérique de la Biliothèque nationale de France, puis ils sont convertis en XML-TEI au moyen de '
                    'scripts Python.</p>',
                    '<p xml:lang="en">is a project that aims to make available in XML-TEI format the texts of '
                    'parliamentary debates in the Chamber of Deputies during the Third Republic, following the <ref '
                    'target="https://github.com/mpuren/agoda/blob/ODD/documentation/agoda_documentation.xml">ODD</ref'
                    '> defined for the project from the <ref '
                    'target="https://github.com/clarin-eric/parla-clarin">Parla-CLARIN recommendations</ref>. From a '
                    'proof-of-concept perspective, phase 1 of the AGODA project focuses more specifically on the 5th '
                    'legislature (1889-1893). The encoded texts are first extracted from the digitised documents '
                    'available on <ref target="https://gallica.bnf.fr/ark:/12148/cb328020951/date.item">Gallica</ref'
                    '>, the digital library of the Biliothèque nationale de France, then they are converted into '
                    'XML-TEI using Python scripts.</p>',
                    '</projectDesc>',
                    '</encodingDesc>',
                    '<profileDesc>',
                    '<langUsage>',
                    '<language ident="fr">Français</language>',
                    '</langUsage>',
                    '<settingDesc>',
                    '<setting>',
                    '<name type="place">Palais Bourbon</name>',
                    '<name type="city">Paris</name>',
                    '<name type="country" key="FR">France</name>',
                    str(date_sitting),
                    '</setting>',
                    '</settingDesc>',
                    '</profileDesc>',
                    '</teiHeader>'])
