from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


dag = DAG(
    'tutorial',
    default_args=default_args,
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)
