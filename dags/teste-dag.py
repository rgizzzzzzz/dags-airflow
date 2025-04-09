from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.operators import DbtDocsOperator
from cosmos.profiles import PostgresUserPasswordProfileMapping
from airflow.models.baseoperator import chain

# Caminho do projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

# Configuração do profile
airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)

with DbtDag(
    dag_id="dbt_com_docs_dag",
    project_config=ProjectConfig(dbt_project_path),
    profile_config=airflow_db,
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["dbt", "docs"],
) as dag:

    generate_docs = DbtDocsOperator(
        task_id="generate_dbt_docs",
        project_dir=dbt_project_path,
        profile_config=airflow_db,
    )

    # Correto: conecta o task_group principal com o generate_docs
    chain(dag.task_group, generate_docs)
