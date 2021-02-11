from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from airflow.plugins.helpers import sql_queries

class LoadDimensionOperator(BaseOperator):
    truncate_sql = """
    TRUNCATE TABLE {destination_table};
    """
    insert_sql = """
    INSERT INTO {destination_table};
    """
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id = "redshift",
                 destination_table = "",
                 append_data = False,
                 sql_query = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.destination_table = destination_table
        self.append_data = append_data
        self.sql_query = sql_query
        

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info('Creating dimensions tables')
        # If append_data is True, then only apply INSERT. Do not delete table.
        if self.append_date:
            dimensions_sql = LoadDimensionOperator.insert_sql + LoadDimensionOperator.sql_query
        
        else:
            dimensions_sql = LoadDimensionOperator.truncate_sql + LoadDimensionOperator.insert_sql + LoadDimensionOperator.sql_query
        
        
        redshift.run(dimensions_sql)