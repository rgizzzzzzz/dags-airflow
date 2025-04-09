from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

# Caminho para o seu projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

# Definindo a configuração do perfil antes de usá-la
airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)

# Criando a DAG (dag_id deve ser o primeiro argumento)
simple_dag = DbtDag(
    dag_id="teste_dag",  # dag_id sempre deve vir primeiro
    project_config=ProjectConfig(dbt_project_path),
    profile_config=airflow_db,
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
)
