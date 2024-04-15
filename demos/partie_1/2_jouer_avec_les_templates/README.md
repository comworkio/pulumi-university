# Démonstration 2 : Jouer avec les templates

Dans cette démonstration, nous allons démontrer comment utiliser les templates prédéfinis de Pulumi.

## Les commandes

```bash
# Lister les templates disponibles
pulumi new -l # (via https://github.com/pulumi/templates)
pulumi new openstack-python --force

# Custom template (via dépôt Git)
pulumi new https://github.com/juhnny5/pulumi-template-gcloud/tree/main --force
```

> L'option `--force` est utilisé car le dossier existe déjà et n'est pas vide.
