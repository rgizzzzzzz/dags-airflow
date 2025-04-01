from cosmos import ExecutionConfig
from pathlib import Path

dbt_executable = Path("/usr/local/bin/dbt")  # Caminho global do dbt

global_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable), #alterando para binário dbt global
)
