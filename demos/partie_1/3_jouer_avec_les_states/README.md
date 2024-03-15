# Démonstration 3 : Jouer avec les states

Dans cette démonstration, nous allons voir comment fonctionne le stockage de l'état de Pulumi.

## Les commandes

```bash
# Lister les templates disponibles
pulumi list -l
pulumi new google-native-python --force
export PULUMI_CONFIG_PASSPHRASE=""
gcloud auth login <e-mail>
pulumi preview
```

> L'option `--force` est utilisé car le dossier existe déjà et n'est pas vide.
