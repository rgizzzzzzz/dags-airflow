from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.operators import DbtDocsOperator

dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)

with DbtDag(
    dag_id="teste_dag",
    project_config=ProjectConfig(dbt_project_path),
    profile_config=airflow_db,
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
) as simple_dag:

    generate_docs = DbtDocsOperator(
        task_id="generate_dbt_docs",
        project_dir=dbt_project_path,
        profile_config=airflow_db,
        target_dir="/opt/airflow/dags/dbt_tutorial/target2",
)

simple_dag.dbt_task_group >> generate_docs

