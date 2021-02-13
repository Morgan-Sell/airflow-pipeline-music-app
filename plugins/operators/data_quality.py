from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):
    data_quality_checks = [
        {'check_sql' : "SELEC COUNT(*) FROM users WHERE userid IS NULL",
         'expected_result' : 0},
        {'check_sql' : "SELECT COUNT(*) FROM songs WHERE songid IS NULL",
         'expected_result' : 0},
        {'check_sql' : "SELECT COUNT(*) FROM artists WHERE artistid IS NULL",
         'expected_result' : 0},
        {'check_sql' : "SELECT COUNT(*) FROM time WHERE start_time IS NULL",
         'expected_result' : 0},
        {'check_sql' : "SELECT COUNT(*) FROM users WHERE userid IS NULL",
         'expected_result' : 0}]
   
        
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id="redshift",
                 table="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table = table

    def execute(self, context):
        self.log.info('DataQualityOperator not implemented yet')