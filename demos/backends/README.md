# Démonstrations : Backends des Pulumi States

Ici est présent le code permettant de stocker les états des différentes démonstration Pulumi avec du code Pulumi sur GCP.
Les états seront stockés dans des buckets GCS.

## Ajouter un nouveau bucket

Pour ajouter un nouveau bucket (pour une nouvelle démonstration), il suffit d'ajouter le nom du bucket souhaité dans le fichier `buckets.yaml`.

## Commandes

```bash
pulumi login --local
export PULUMI_CONFIG_PASSPHRASE=""
pulumi stack select -s dev
pulumi preview --non-interactive
pulumi update --non-interactive --yes

# Lister les buckets
export PROJECT_NAME="qualified-sum-417111"
gcloud config set project ${PROJECT_NAME}
gcloud storage ls
```
