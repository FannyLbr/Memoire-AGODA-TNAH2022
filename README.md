## Rendu Mémoire de stage TNAH - projet AGODA  
Ce dépôt contient :
- le mémoire de stage :
  - au format PDF : `memoire_TNAH2022_Fanny_LEBRETON.pdf`;
  - au format LaTeX : `memoire_TNAH2022_Fanny_LEBRETON_latex.zip`.

- les livrables techniques mentionnés dans les annexes du mémoire et répartis en trois dossiers principaux : `A - Sources primaires`, `B - Modélisation XML-TEI` et `C - Encodage automatique`. Ces derniers sont constitués de la manière suivante : 
  - Le dossier `/A - /A1 - Numérisations Gallica/` contient les numérisations de deux comptes rendus des débats parlementaires, celui de la séance du 26 novembre 1889 et celui de la séance du 14 janvier 1890 :
    - FR_3L_5L_1889-11-26_digitisation.pdf
    - FR_3L_5L_1890-01-14_digitisation.pdf
  - Le dossier `/A - /A2 - Images Archives nationales/` contient des photographies prises lors d’une visite aux Archives nationales du compte rendu in extenso et du procès-verbal de la séance du 26 novembre 1889 :
    - Dans le dossier `/CR`, voir :
      - 20220505_110636.jpg
      - 20220505_111410.jpg
      - 20220505_111418.jpg
      - 20220505_111438.jpg
      - 20220505_111448.jpg
      - 20220505_111450.jpg
    - Dans le dossier `/PV`, voir :
      - 20220505_102611.jpg
      - 20220505_102621.jpg
      - 20220505_102631.jpg
      - 20220505_102641.jpg
      - 20220505_102648.jpg
      - 20220505_102657.jpg
      - 20220505_102748.jpg
      - 20220505_102752.jpg
      - 20220505_102858.jpg
   - Le dossier `/B - /B1 - Documents de travail/` contient trois anciennes versions de l’encodage XML-TEI effectuées lors de la modélisation du modèle, ainsi qu’un document en markdown relatant les étapes de la construction du schéma :
     - FR_3R_5L_1889-11-26_v1.xml
     - FR_3R_5L_1889-11-26_v2.xml
     - FR_3R_5L_1889-11-26_v3.xml
     - schema_working_document.md
   - Le dossier `/B - /B2 - Encodage test/` contient les modèles d’encodage idéaux du fichier XML-TEI corpus et du fichier XML-TEI composant, ainsi que le schéma d’encodage au format Relax NG qui est relié aux deux fichiers XML-TEI :
     - FR_3R_5L.xml
     - FR_3R_5L_1889-11-26_ideal_encoding_model.xml
     - agoda_schema.rng
   - Le dossier `/B - /B3 - Schéma et documentation/` contient l’ODD aux formats XML et HTML, le schéma d’encodage au format Relax NG et les spécifications du modèle au format XML :
     - agoda_odd.html
     - agoda_odd.xml
     - agoda_schema.rng
     - agoda_schemaSpec.xml
   - Le dossier `/C - /C1 - Guides/` contient le guide d’annotation et celui de l’encodage automatique :
     - guide_annotations_agoda.pdf
     - guide_modelisation_encodage_automatique.pdf
   - Le dossier `/C - /C2 - Scripts Python/` contient l’ensemble des scripts Python utilisés pour l’encodage automatique des données :
     - main.py
     - script_balisage_formel.py
     - script_balisage_logique.py
     - script_balisage_semantique.py
     - script_compilation.py
     - script_metadonnees.py
     - script_nettoyage.py
   - Le dossier `/C - /C3 - Données tests/` contient l’ensemble des fichiers JSON annotés de la séance du 26 novembre 1889, ainsi que le résultat XML-TEI obtenu suite à l’application du processus d’encodage automatique :
     - Dans le dossier `/json_data`, voir :
       - FR_3R_5L_1889-11-26_p0175.json
       - FR_3R_5L_1889-11-26_p0176.json
       - FR_3R_5L_1889-11-26_p0177.json
       - FR_3R_5L_1889-11-26_p0178.json
       - FR_3R_5L_1889-11-26_p0179.json
       - FR_3R_5L_1889-11-26_p0180.json
       - FR_3R_5L_1889-11-26_p0181.json
       - FR_3R_5L_1889-11-26_p0182.json
       - FR_3R_5L_1889-11-26_p0183.json
       - FR_3R_5L_1889-11-26_p0184.json
       - FR_3R_5L_1889-11-26_p0185.json
       - FR_3R_5L_1889-11-26_p0186.json
       - FR_3R_5L_1889-11-26_p0187.json
       - FR_3R_5L_1889-11-26_p0188.json
       - FR_3R_5L_1889-11-26_p0189.json
       - FR_3R_5L_1889-11-26_p0190.json
       - FR_3R_5L_1889-11-26_p0191.json
       - FR_3R_5L_1889-11-26_p0192.json
       - FR_3R_5L_1889-11-26_p0193.json
     - Dans le dossier `/xml_data`, voir :
       - FR_3R_5L.xml
       - FR_3R_5L_1889-11-26.xml
       - agoda_schema.rng




  
