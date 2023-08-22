import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """ 
    Description: drops any table, executing drop table queries.
    params:
    - cur: SQL database cursor (psycopg2).
    - conn: SQL database connection (psycopg2).
    output: no return, drops database tables from AWS Redshift.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """ 
    Description: creates new tables.
    params:
    - cur: SQL database cursor (psycopg2).
    - conn: SQL database connection (psycopg2).
    output: no return, creates new database tables into AWS Redshift.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ 
    Description: main void:
    - connects to AWS Redshift.
    - creates new tables (create_tables function).
    - drops any table (drop_tables function).
    - closes connection.
    params: no params. Reads from dwh.cfg host, dbname, user, password, port, cur, conn.
    output: no return, executes the process in description.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()