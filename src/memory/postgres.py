from langgraph.checkpoint.postgres import PostgresSaver
from psycopg import Connection


class PostgresMemory:
    def __init__(self, db_uri: str):
        """
        
        """
        self.db_uri = db_uri
        self.checkpointer = PostgresSaver(self._get_connection())

    def _get_connection(self):
        """
        
        """
        connection_kwargs = {
            "autocommit": True,
            "prepare_threshold": 0
        }
        try:
            conn = Connection.connect(self.db_uri, **connection_kwargs)
        except Exception as e:
            raise e
        return conn

    def setup(self):
        """
        
        """
        self.checkpointer.setup()

    def get_checkpointer(self):
        """
        
        """
        return self.checkpointer

