import psycopg2

def check_connection():

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
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

