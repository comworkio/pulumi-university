# DaaS: deployment as a service

Dans cette partie nous allons voir un exemple d'API qui permet d'invoquer une api d'IaaS de façon générique en utilisant le pattern adapter (ou driver).

Cela pour illustrer qu'il deviens très facile d'embarquer Pulumi comme dépendance dans des applications plus évoluées.

Pour l'exécuter en local :

```shell
cp .env.dist .env
# Remplacer les changeit dans le fichier .env
docker-compose up --build --force-recreate
```

Ensuite vous pourrez accéder à la documentation OpenAPI ici: http://localhost:8000
