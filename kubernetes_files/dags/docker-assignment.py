from datetime import datetime, timedelta
from airflow import DAG
# from airflow.operators import BashOperator
from airflow.operators.python_operator import PythonOperator
# from connection import check_connection
# from fetch import fetch_info
import psycopg2

def check_connection():

    try:
        conn = psycopg2.connect(host="postgres-service-db", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()
        print("Check")
        add_data = 'create table docker_Assignment_table as select dag_id, execution_date from dag_run order by ' \
                   'execution_date; '
        cursor.execute(add_data)
        conn.commit()

        print("data added to a new table Successfully")
        conn.close()
    except:
        print("Error in connection")
    finally:
        print("No issues")


def fetch_info():

    try:
        conn = psycopg2.connect(host="postgres-service-db", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        query = 'select * from docker_Assignment_table;'
        cursor.execute(query)
        data = cursor.fetchall()
        print("This is Data Execution time for every DAG runs :- ")
        for i in data:
            print(i)
        print("Data Fetched to the Console Successfully")
        conn.close()


    except:
        print("Error in connection")
    finally:
        print("No issues")

default_args = {
    "owner": "yashwanth",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 29),
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG("Docker-assignment", default_args=default_args, schedule_interval="0 6 * * *")

# t1 = BashOperator(task_id="Welcome", bash_command="Hi, This is Janhawi Shresth", dag=dag)

t2 = PythonOperator(task_id='Adding_info_to_DB_table', python_callable=check_connection, dag=dag)

t3 = PythonOperator(task_id='fetching_info_from_PostgresDB', python_callable=fetch_info, dag=dag)

t2 >> t3
