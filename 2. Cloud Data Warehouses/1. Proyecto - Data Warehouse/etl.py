import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """ 
    Description: loads log_data and song_data from S3 and inserts into staging tables.
    params:
    - cur: SQL database cursor (psycopg2).
    - conn: SQL database connection (psycopg2).
    output:no return, staging tables (staging_events and staging_songs).
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """ 
    Description: inserts data from staging tables into star schema.
    params:
    - cur: SQL database cursor (psycopg2).
    - conn: SQL database connection (psycopg2).
    output: no return, fact table (songplays) and dimension tables (users, songs, artists, time).
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ 
    Description: main void:
    - connects to database.
    - creates staging tables (load_staging_tables function).
    - creates star schema (insert_tables function).
    - closes connection.
    params: no params. Reads from dwh.cfg host, dbname, user, password, port, cur, conn.
    output: no return, executes the process in description.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()