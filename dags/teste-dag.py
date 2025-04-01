from datetime import datetime
from cosmos import DbtDag, ProjectConfig
from cosmos.operators import DbtDocsOperator
from include.profiles import airflow_db

# Caminho para o seu projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

# Usando a configuração de perfil importada
profile_config = airflow_db  

# Criando a DAG
simple_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_path),
    profile_config=profile_config,
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="teste_dag",
    tags=["simple"],
)
