import psycopg2
import os


class Db:
    def __init__(self):
        database = os.getenv('DATABASE_NAME')
        user = os.getenv('DATABASE_USER')
        host = os.getenv('DATABASE_HOST')
        password = os.getenv('DATABASE_PASSWORD')
        port = int(os.getenv('DATABASE_PORT'))

        conn = psycopg2.connect(database=database,
                                user=user,
                                host=host,
                                password=password,
                                port=port)
        self.conn = conn

    async def query(self,
                    query: str,
                    convert_func,
                    args=None,
                    ):
        curr = None
        try:
            curr = self.conn.cursor()
            curr.execute(query, args)
            rs = curr.fetchall()
            return [convert_func(row) for row in rs]
        except (Exception, psycopg2.DatabaseError) as error:
            print('error occured', error)
        finally:
            if self.conn:
                if curr:
                    curr.close()

    async def query_one(self,
                        query: str,
                        convert_func,
                        args=None
    ):
        curr = None
        try:
            curr = self.conn.cursor()
            curr.execute(query, args)
            row = curr.fetch_one()
            if row:
                return convert_func(row)
            else:
                return None
        except (Exception, psycopg2.DatabaseError) as error:
            print('error occured', error)
        finally:
            if self.conn:
                if curr:
                    curr.close()

