import dagster as dg
from dagster_duckdb import DuckDBResource

database_resource = DuckDBResource(database="dbt_abacate/abacate.duckdb")

@dg.definitions
def resources():
    return dg.Definitions(
        resources={
            "duckdb": database_resource,
        }
    )
