# Démonstrations : Backends des Pulumi States

Ici est présent le code permettant de stocker les états des différentes démonstration Pulumi avec du code Pulumi sur GCP.
Les états seront stockés dans des buckets GCS.

## Commandes

```bash
export PULUMI_CONFIG_PASSPHRASE=""
pulumi stack select -s dev
pulumi preview --non-interactive
pulumi update --non-interactive --yes

# Lister les buckets
export PROJECT_NAME="qualified-sum-417111"
gcloud config set project ${PROJECT_NAME}
gcloud storage ls
```
