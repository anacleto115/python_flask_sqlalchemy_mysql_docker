import os

class Configuration:
    @staticmethod
    def Get(key: str) -> str:
        return os.environ.get(key, '');
    
    @staticmethod
    def Load():
        os.environ['db.string_conexion'] = 'mysql+pymysql://user:password@localhost:3306/db_store';
