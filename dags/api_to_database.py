
from airflow.decorators import task, dag

from include.controller import gerar_numero_aleatorio, fetch_pokemon_data, add_pokemon_to_db

from datetime import datetime

@dag(dag_it='api_to_database',
     description='pipeline_para_capturar_pokemon',
     start_date=datetime(2024,9,15),
     schedule='* * * * *',
     catchup=False)
def api_to_database():

    @task(task_id='gerar_numero_aleatorio')
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()

    @task(task_id='fetch_pokemon_data')
    def task_fetch_pokemon_data(numero_aleatorio):
        return fetch_pokemon_data(numero_aleatorio)

    @task(task_id='add_pokemon_to_db')
    def task_add_pokemon_to_db(pokemon_data):
        return add_pokemon_to_db(pokemon_data)

    t1 = task_gerar_numero_aleatorio
    t2 = task_fetch_pokemon_data
    t3 = task_add_pokemon_to_db

    t1 >> t2 >> t3

api_to_database()