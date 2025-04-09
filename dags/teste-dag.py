from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.operators import DbtDocsOperator
from cosmos.profiles import PostgresUserPasswordProfileMapping

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

    # Pega todas as tasks dentro do task_group
    dbt_tasks = list(dag.task_group.get_tasks())

    # Conecta a última task do grupo ao generate_docs
    dbt_tasks[-1] >> generate_docs
