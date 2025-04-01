from datetime import datetime
from cosmos import DbtDag, ProjectConfig
from cosmos.operators import DbtDocsOperator
from include.constants import global_execution_config  # Alterado para o novo config
from include.profiles import airflow_db

# Caminho para o seu projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"

# Usando a configuração de perfil importada
profile_config = airflow_db  

# Criando a DAG
with DbtDag(
    project_config=ProjectConfig(dbt_project_path),
    profile_config=profile_config,
    execution_config=global_execution_config,  # Alterado para o novo config #alterando para binário dbt global
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="teste_dag",
    tags=["simple"],
) as simple_dag:

    # Tarefa para gerar a documentação dbt
    generate_docs = DbtDocsOperator(
        task_id="generate_dbt_docs",
        project_dir=dbt_project_path,
        profile_config=profile_config,
        target_dir="/opt/airflow/dags/target",
    )
