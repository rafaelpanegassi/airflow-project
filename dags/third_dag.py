import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(start_date=datetime.datetime(2024, 3, 23), schedule="@daily", catchup=False)
def gerar_dag():
    EmptyOperator(task_id="tarefa")

gerar_dag()