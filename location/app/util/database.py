import os
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

class Db:
    def __init__(self):
        self.pool = self.create_connection_pool()

    def create_connection_pool(self):
        return SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            database=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            host=os.getenv('DATABASE_HOST'),
            password=os.getenv('DATABASE_PASSWORD'),
            port=int(os.getenv('DATABASE_PORT'))
        )

    def execute_query(self, query, args=None, convert_func=None, fetch_all=True):
        with self.pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as curr:
                curr.execute(query, args)
                if fetch_all:
                    result_set = curr.fetchall()
                    return [convert_func(row) for row in result_set] if convert_func else result_set
                else:
                    row = curr.fetchone()
                    return convert_func(row) if row and convert_func else row

    async def query(self, query, convert_func, args=None):
        """Queries a database and converts the result set using a convert function"""
        try:
            return self.execute_query(query, args, convert_func)
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error occurred:', error)

    async def query_one(self, query, convert_func, args=None):
        """Queries a database, but only gets the first value. It then converts the result set to an object using the convert function"""
        try:
            return self.execute_query(query, args, convert_func, fetch_all=False)
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error occurred:', error)

    async def update(self, query, args=None):
        """Will update, insert, or delete values from the database. Returns the number of rows affected"""
        try:
            with self.pool.getconn() as conn:
                with conn.cursor() as curr:
                    curr.execute(query, args)
                    row_count = curr.rowcount
                    conn.commit()
                    return row_count
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error occurred:', error)