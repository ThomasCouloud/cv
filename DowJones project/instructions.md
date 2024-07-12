Ce README fournit des instructions pour configurer et exécuter le projet de prédiction de prix d'actions.
Dans le répertoire de docker-compose.yml:

Configuration
Entraînement du modèle

!!!!WARNING!!!!
Assurez-vous de vous trouver dans le répertoire du script pour cette étape.

python model_training.py

Lancement de l'API

!!!!WARNING!!!!
Assurez-vous d'être dans le répertoire racine du projet pour cette étape.

Exécutez la commande suivante pour lancer l'API :

uvicorn api.app:app --host 0.0.0.0 --port 8000

Utilisation
Faire une prédiction

Pour faire une prédiction, utilisez une des méthodes suivantes :

    Utilisation de PowerShell :

    Invoke-RestMethod -Uri 'http://127.0.0.1:8000/api/predict/' -Method Post -Headers @{"Content-Type" = "application/json"} -Body '{"ticker": "AAPL", "days": 1}'

    Utilisation de Curl :

    curl -X 'POST' \
  'http://localhost:8000/api/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "ticker": "AAPL",
  "days": 2
}'

Faire une boucle de prédictions pour un ticker spécifique

Utilisez le script PowerShell suivant :

$baseUri = 'http://127.0.0.1:8000/api/predict/'
$headers = @{"Content-Type" = "application/json"}
$ticker = "AAPL"
$results = @()

for ($days = 1; $days -le 100; $days++) {
    $body = @{ "ticker" = $ticker; "days" = $days } | ConvertTo-Json
    $response = Invoke-RestMethod -Uri $baseUri -Method Post -Headers $headers -Body $body
    $results += $response
}

$results

Tests

!!!!WARNING!!!!
Assurez-vous de vous trouver dans le répertoire \tests pour cette étape.

Exécutez les tests unitaires en utilisant pytest :

    Pour tester l'API :

    pytest test_api.py

    Pour tester le modèle :

    pytest test_models.py

    Ou pour exécuter tous les tests à partir du répertoire racine du projet :

    pytest tests\







docker-compose up
=======
# MLOPS_OPA_JUN2023
DataScientest MLOps Project Jun2023 cohort

