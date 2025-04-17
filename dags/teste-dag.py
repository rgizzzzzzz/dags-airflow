from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.operators import DbtDocsOperator
import shutil
import os

# Caminho para o seu projeto DBT
dbt_project_path = "/opt/airflow/dags/dbt_tutorial"
docs_output_dir = "/opt/docs"

# Definindo a configuração do perfil antes de usá-la
airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)

# Função para copiar os arquivos gerados para o diretório de docs
def copy_docs_to_local(project_dir: str, context: dict = None):
    target_dir = os.path.join(project_dir, "target")
    
    # Verificar se a pasta de saída do DBT existe
    if os.path.exists(target_dir):
        # Copiar os arquivos necessários para o diretório /opt/docs
        for file_name in ["index.html", "manifest.json", "graph.gpickle", "catalog.json"]:
            src_path = os.path.join(target_dir, file_name)
            if os.path.exists(src_path):
                dest_path = os.path.join(docs_output_dir, file_name)
                shutil.copy(src_path, dest_path)
                print(f"Arquivo copiado para: {dest_path}")
    else:
        print(f"A pasta de saída do DBT não foi encontrada: {target_dir}")

# Criando a DAG com o DBT
with DbtDag(
    dag_id="teste_dag",  # dag_id sempre deve vir primeiro
    project_config=ProjectConfig(dbt_project_path),
    profile_config=airflow_db,
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["simple"],
) as simple_dag:  # Usando o contexto 'with' para garantir que a DAG seja criada corretamente

    # Definindo a tarefa para gerar a documentação DBT e copiar os arquivos para /opt/docs
    generate_dbt_docs = DbtDocsOperator(
        task_id="generate_dbt_docs",
        project_dir=dbt_project_path,
        profile_config=airflow_db,
        callback=lambda project_dir, **kwargs: copy_docs_to_local(project_dir, context=kwargs),  # Alterado para usar **kwargs
    )
