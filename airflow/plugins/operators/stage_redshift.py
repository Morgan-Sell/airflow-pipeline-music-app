from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # redshift_conn_id=your-connection-name
                 redshift_conn_id="redshift",
                 table="",
                 aws_credentials_id="aws_credentials",
                 s3_path=""
                 s3_bucket="",
                 s3_key="",
                 delimiter=",",
                 ignore_headers=1,
                 *args, **kwargs):
               

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id,
        self.table = table,
        self.aws_credentials_id = aws_credentials_id,
        self.s3_path = s3_path,
        self.s3_bucket = s3_bucket,
        self.s3_key = s3_key,
        self.delimiter = delimeter,
        self.ignore_headers = ignore_headers

    stage_sql_template = """
    COPY {table};
    FROM '{s3_path}'
    ACCESS_KEY_ID '{s3_key}'
    SECRET_ACCESS_KEY '{}'
    IGNOREHEADER {}
    DELIMITER '{}'    
    """
        
    def execute(self, context):
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Connected with {}".format(self.redshift_conn_id))
        redshift.run("DELETE FROM {}".format(self.table))
        
        self.log.info("Staging data from S3 to Redshift")
        rendered_key = self.s3_key.format(**context)

        s



