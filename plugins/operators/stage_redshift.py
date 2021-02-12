from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook

class StageToRedshiftOperator(BaseOperator):
    stage_sql_template = """
    COPY {}
    FROM {}
    ACCESS_KEY_ID {}
    SECRET_ACCESS_KEY {}
    IGNOREHEADER {}
    DELIMITER {}    
    """
    
    ui_color = '#358140'
    templated_fields = ("s3_key", )
    
    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # redshift_conn_id=your-connection-name
                 redshift_conn_id="redshift",
                 table = "",
                 table_delete = "",
                 sql_query = "",
                 aws_credentials_id="aws_credentials",
                 s3_path="s3://udacity-dend",
                 s3_bucket="",
                 s3_key="/{ execution_date.year }/{ execution_date.month } / { ds }-events.json",
                 delimiter=",",
                 ignore_headers=1,
                 *args, **kwargs):
               

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.table_delete = table_delete
        self.sql_query = sql_query
        self.aws_credentials_id = aws_credentials_id
        self.s3_path = s3_path
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.delimiter = delimiter
        self.ignore_headers = ignore_headers

    
        
    def execute(self, context):
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Connected with {}".format(self.redshift_conn_id))
        redshift_hook.run("DELETE FROM {}".format(self.table_delete))
        
        self.log.info("Staging data from S3 to Redshift")
        rendered_key = self.s3_key.format(**context)

        staged_sql = StageToRedshiftOperator.stage_sql_template.format(
            self.table,
            self.s3_path,
            credentials.access_key,
            credentials.secret_key,
            self.ignore_headers,
            self.delimiter
        )
        redshift_hook.run(staged_sql)


