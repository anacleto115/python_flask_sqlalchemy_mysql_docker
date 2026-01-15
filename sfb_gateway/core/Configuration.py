import os

class Configuration:
    @staticmethod
    def Get(key: str) -> str:
        return os.environ.get(key, '');
    
    @staticmethod
    def Load():
        os.environ['app.version'] = '0.0.1';
        os.environ['app.secret'] = 'JH4d646d54fg53df1g32654gj764832132';
        os.environ['db.string_conexion'] = 'mysql+pymysql://user:password@localhost:3306/db_store';
