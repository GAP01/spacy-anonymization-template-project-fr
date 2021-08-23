<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# :shipit: spaCy Project: template d'anonymisation des données sensibles RGPD dans le texte libre

Ce template de projet contient des patterns d'entité ainsi que des données d'entraînement spécifiquement conçues
pour la détections des entités sensibles du point de vue RGPD. Cela inclut toutes les informations permettant, ou augmentant
fortement le risque de réidentification d'un individu.

## 📋 project.yml

Le fichier [`project.yml`](project.yml) définit les données requises par le
projet, ainsi que les différentes commandes et workflow disponibles.
Pour plus de détails [spaCy projects documentation](https://spacy.io/usage/projects)


### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `download` | Télécharge le modèle fr pré entraîné|
| `convert` | Converti les données d'entraînement et de tests du JSON au format binaire d'entraînement spacy |
| `create-config` | Créé un fichier de configuration pour le modèle à partir du fichier base_config.cfg |
| `train` | Entaîne le modèle|
| `evaluate` | Calcul et exporte au format JSON les métriques de performance du modèle |
| `package` | Package le modèle comme un package pip |
| `visualize-model` | Visualiser les interprétations du modèle de façon interactive dans Streamlit |

### ⏭ Workflows

Les workflows suivants sont définis pour le projet. Ils peuvent être exécutés via la commande
[`spacy project run [name]`](https://spacy.io/api/cli#project-run) et lanceront les commandes
dans l'ordre spécifié. Chaque étape n'est excutée que si un changement est détecté par rapport
à la version précédente.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `create-config` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

Les dépendances suivantes sont définies par le projet. Ils peuvent être synchronisés en
exécutant [`spacy project assets`](https://spacy.io/api/cli#project-assets)
dans le dossier du projet.

| File | Source | Description |
| --- | --- | --- |
| [`assets/train.json`](assets/train.json) | Local | Demo training data converted from the v2 example scripts with `srsly.write_json("train.json", TRAIN_DATA)` |
| [`assets/dev.json`](assets/dev.json) | Local | Demo development data |
| [`assets/patterns.json`](assets/patterns.json) | Local | Demo patterns definition for entity ruler |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
