# Structure du dossier GlobalMarketInsights

```bash
project/
│
├── dags/                        # DAGs Airflow pour l'orchestration
│   └── your_project_dag.py       # Fichier de définition des workflows Airflow
│
├── data/                        # Dossier de stockage des données temporaires (si nécessaire)
│   └── raw/                     # Données brutes récupérées via API (avant ingestion)
│   └── processed/               # Données transformées (facultatif si tout passe par BigQuery)
│
├── docker/                      # Configurations Docker spécifiques
│   └── Dockerfile               # Dockerfile pour conteneuriser les composants du projet
│   └── docker-compose.yml       # Fichier Docker Compose pour gérer plusieurs conteneurs
│
├── config/                      # Pour les fichiers de configuration
│
├── notebooks/                   # Notebooks Jupyter pour analyses ad hoc
│   └── analysis_notebook.ipynb  # Exemple d'un notebook pour tester les analyses
│
├── src/                         # Code source du projet
│   ├── api/                     # Scripts pour l'appel d'API et la récupération des données
│   │   └── fetch_data.py        
│   ├── db/                      # Scripts pour interagir avec BigQuery (ou autres bases de données)
│   │   └── load_to_bigquery.py  # Script pour charger les données dans BigQuery
│   ├── models/                  # Modèles de machine learning pour projections
│   │   └── ml_model.py          # Exemple de modèle ML pour prédire les tendances boursières
│   ├── transformation/          # Scripts pour transformer/normaliser les données
│   │   └── data_transformation.py # Script de transformation des données avant stockage
│   ├── data_collection/         # Scripts pour collecter les données
│   │   └── fetch_index_composition.py # Script pour appeler l'API (ex. yfinance, Alpha Vantage)
│   └── visualisation/           # Tableau de bord et visualisation des données
│       └── app.py               # Application Dash pour visualiser les données
│
├── airflow/                     # Configuration d'Airflow
│   ├── airflow.cfg              # Fichier de configuration d'Airflow
│   ├── docker-compose.yaml      # Docker Compose spécifique pour Airflow
│   └── requirements.txt         # Dépendances spécifiques pour Airflow
│
├── requirements.txt             # Liste des dépendances du projet (hors Airflow)
├── README.md                    # Documentation du projet
└── .env                         # Variables d'environnement (API keys, accès BigQuery, etc.)
```

