from time import sleep

from airflow.decorators import dag, task

@dag(
         dag_id="dag_inicial",
         schedule_interval='@daily', 
         start_date='2023-10-01', 
         catchup=False, 
         tags=['Iniciando'])
def pipeline():
     

    @task

    def primeira_atividade():
        print("minha primeira atividade! - Executado Ok ")
        sleep(2)
    @task

    def segunda_atividade():
        print("minha segunda atividade! - Executado Ok")
        sleep(2)
    @task

    def terceira_atividade():
        print("minha terceira atividade - Executado Ok")
        sleep(2)

    def pipeline():
        t1 =primeira_atividade()
        t2 =segunda_atividade()
        t3 =terceira_atividade()

        t1 >> t2 >> t3
    pipeline()
    

