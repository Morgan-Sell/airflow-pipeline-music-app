from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class LoadDimensionOperator(BaseOperator):
    truncate_sql = """
    TRUNCATE TABLE {};
    """
    insert_sql = """
    INSERT INTO {} {};
    """
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id = "redshift",
                 table_name = "",
                 truncate_data = True,
                 sql_query = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table_name = destination_table
        self.truncate_data = truncate_data
        self.sql_query = sql_query
        

    def execute(self, context):
        self.log.info(f"Started execution of LoadDimensionsOperator on {self.table_name}. \
                      Delete existing data: {self.truncate_data}.")
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
     
        if self.truncate_data:
            redshift_hook.run(LoadDimensionOperator.truncate_sql.format(self.table_name))
        
        redshift_hook.run(LoadDimensionOperator.insert_sql.format(self.table_name, self.sql_query))
        
        self.log.info(f"Completed implemenation of LoadDimensionOperator on {self.table_name}")
    
       