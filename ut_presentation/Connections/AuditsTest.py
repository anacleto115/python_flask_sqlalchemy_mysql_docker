import datetime;
from lib_domain.entities import Audits;
from lib_repositories.interfaces import IConnection;
from lib_repositories.implementations import Connection;
from Core import Configuration, EntitiesCore;

class AuditsTest:
    iConnection: IConnection.IConnection = None;
    _list: list  = None;
    _entity: Audits.Audits = None;

    def __init__(self):
        self.iConnection = Connection.Connection();
        self.iConnection.SetStringConnection(Configuration.Configuration.Get("db.string_conexion"));

    def Execute(self):
        self.Insert();

    def Insert(self) -> bool:
        self._entity = EntitiesCore.EntitiesCore.Audits();
        self.iConnection.Open();
        self._entity = self.iConnection.Insert(self._entity);
        self.iConnection.Close();
        return True;