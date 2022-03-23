# docker-kubernetes

Docker task

1. Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
2. Add the given dag into the container and install dependencies.
3. Use docker compose to launch airflow and postgres
4. Schedule the dag
5. Validate entry in postgres

Kubernetes Task

1. Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
2. Deploy airflow and postgres
3. Schedule the dag
4. Validate entry in postgres
