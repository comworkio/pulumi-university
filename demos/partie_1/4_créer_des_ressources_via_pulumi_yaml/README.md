# Démonstration 4 : Créer des ressources via Pulumi YAML

## Les commandes

```bash
# Déployer un bucket
export PULUMI_CONFIG_PASSPHRASE=""
export PULUMI_STATE_NAME="gs://part1_demo1_bis_states-6d0b7a1/"
gcloud auth login <e-mail>
pulumi login ${PULUMI_STATE_NAME}
pulumi preview
pulumi update
```
