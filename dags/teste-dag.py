from datetime import datetime
from airflow import DAG
from airflow.models.baseoperator import chain
from cosmos import ProjectConfig, ProfileConfig, DbtTaskGroup
from cosmos.operators import DbtDocsOperator
from cosmos.profiles import PostgresUserPasswordProfileMapping

# Caminho para o seu projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

# Configuração do perfil DBT
airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)

# DAG padrão do Airflow
with DAG(
    dag_id="teste_dag_com_taskgroup_e_docs",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["dbt", "docs"],
) as dag:

    # Task group do Cosmos (executa run, test, seed, etc. automaticamente)
    dbt_tasks = DbtTaskGroup(
        group_id="dbt_task_group",
        project_config=ProjectConfig(dbt_project_path),
        profile_config=airflow_db,
    )

    # Task para gerar a documentação
    generate_docs = DbtDocsOperator(
        task_id="generate_dbt_docs",
        project_dir=dbt_project_path,
        profile_config=airflow_db,
    )

    # Define a ordem de execução: após o grupo de tarefas do DBT, gera a documentação
    chain(dbt_tasks, generate_docs)
