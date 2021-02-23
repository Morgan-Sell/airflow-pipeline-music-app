from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):
    data_quality_checks = [
        {'check_sql' : "SELECT COUNT(*) FROM users WHERE userid IS NULL",
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
                 tables=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables

    def execute(self, context):
        
        
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info('Start assessment of the data quality of the dimension and facts tables.')
        
        error_count = 0
        
        for check in DataQualityOperator.data_quality_checks:
            sql_query = check.get('check_sql')
            exp_result = check.get('expected_result')
            records = redshift_hook.get_records(sql_query)[0]
            
            if records != records[0]:
                error_count += 1
                failing_tests.append(sql_query)
            
            if error_cout > 0:
                self.log.info("Failed data quality tests")
                self.log.info("No. of failed tests: {}".format(error_count))
                self.log.info(failing_tests)
                raise ValueError("Data quality check fail")
                
            if error_count == 0:
                self.log.info("Passed data quality tests")
        