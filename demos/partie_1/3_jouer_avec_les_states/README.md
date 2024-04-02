# Démonstration 3 : Jouer avec les states

Dans cette démonstration, nous allons voir comment fonctionne le stockage de l'état de Pulumi.

## Les commandes

```bash
# Lister les templates disponibles
pulumi list -l
pulumi new google-native-python --force

# Possible de déclarer le bucket (backend) via une variable d'env :
# export PULUMI_STATE_NAME="gs://part1_demo3_states-69b90a8/"
# gcloud auth login <e-mail>
# pulumi login ${PULUMI_STATE_NAME}

# Déployer un bucket
pulumi preview
pulumi update

# Regarder le contenu du bucket (.pulumi/)
gcloud storage ls --recursive ${PULUMI_STATE_NAME}

# TIPS : Voir où est stocké le state
pulumi whoami -v
```

> L'option `--force` est utilisé car le dossier existe déjà et n'est pas vide.
