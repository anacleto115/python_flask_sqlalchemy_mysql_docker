import datetime;
from lib_domain.entities import Audits;
from lib_repositories.interfaces import IConnection, IAuditsRepository;
from lib_repositories.implementations import Connection, AuditsRepository;
from Core import Configuration, EntitiesCore;

class AuditsTest:
    iRepository: IAuditsRepository.IAuditsRepository = None;
    _list: list  = None;
    _entity: Audits.Audits = None;

    def __init__(self):
        iConnection = Connection.Connection();
        iConnection.SetStringConnection(Configuration.Configuration.Get("db.string_conexion"));

        self.iRepository = AuditsRepository.AuditsRepository(iConnection);

    def Execute(self):
        self.Insert();

    def Insert(self) -> bool:
        self._entity = EntitiesCore.EntitiesCore.Audits();
        self._entity = self.iRepository.Insert(self._entity);
        return True;