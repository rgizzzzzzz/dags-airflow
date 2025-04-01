"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping


airflow_db = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_local",
        profile_args={"schema": "dbt"},
    ),
)
