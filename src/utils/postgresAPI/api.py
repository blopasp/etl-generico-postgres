import psycopg2 as pg
from psycopg2 import connect, extras
import os
from json import load
import logging

class Postgres:
    def __init__(self, host:str, database:str, user:str, password:str) -> None:
        self.__host = host
        self.__database = database
        self.__user = user
        
        self.__conn = self.__connect(password)
        
    def __connect(self, password):
        return pg.connect(
                         host = self.__host,
                         database = self.__database,
                         user = self.__user,
                         password = password
                        )

    def __str__(self) -> str:
        return f"Connection Info\n\tHost: {self.__host}\n\tDatabase: {self.__database}\n\tUser: {self.__user}"


class DBPostgres(Postgres):
    """
    This object was defined to operate a database postgres with some
    operations:
        - execute: run a command sql
        - truncate: trucate the specific table
        - get_results_from_query: run a query and returns a set of
    values in the dict type
        - copy_from_file: copy a file like csv and txt into a table
        - insert: insert a dataset of values of the type list
        - upsert: this method insert a dataset and do update, if needed
        - all_tables_from_schema:
        - table_information:
        - close: terminate the aplication
    Args:
        host (str): _description_
        database (str): _description_
        user (str): _description_
        password (str): _description_
    """
    
    def __init__(self, host: str, database: str, user: str, password: str) -> None:
        super().__init__(host, database, user, password)
        
    def execute(self, command):
        """Method execute
        Args:
            command (string): command sql to operate in db postgres
        Returns:
           Boolean
        """
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(command)
            self.__conn.commit()
            logging.info("Ok - command executed with sucess")
        except Exception as e:
            self.__conn.rollback()
            logging.exception("Exception occurred")
            raise
        
    def truncate(self, table, schema = "public"):
        """Method truncate
        Args:
            table (string): the table name
            schema (string default "public"): the schema name, public default
        Returns:
            boolean
        """
        self.execute(f"TRUNCATE {schema}.{table} CASCADE")
            
    def get_results_from_query(self, query, interval_register = 500):
        """Method get_results_query
        Method used to return data from a postgres database in dictionary form
        Args:
            query (string): the query to execute for returning data
            interval_register (int): interval to returnind data, default: 150
        Returns:
            dict type
        """
        with self.__conn.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute(query)
            colunas = [x[0] for x in cursor.description]
            
            results = []
            for result in cursor.fetchmany(interval_register):
                results.extend(result)
        return {"cols":colunas, 'data':results}
    
    def copy_from_file(self):
        pass
    
    def insert(self):
        pass
    
    def upsert(self):
        pass
    
    def all_tables_from_schema(self, schema:str):
        return self.get_results_from_query("SELECT table_name " + 
                                      "FROM information_schema.tables " +
                                      f"WHERE table_schema = '{schema}'")
    
    def table_information(self, table:str, schema:str = "public"):
        return self.get_results_from_query("SELECT table_name, column_name" + 
                                      "FROM information_schema.columns " +
                                      f"WHERE table_schema = '{schema}' and table_name = {table}")
    
    def close(self):
        self.__conn.close()


