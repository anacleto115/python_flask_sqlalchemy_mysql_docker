import sys;
from lib_repositories.interfaces import IConnection, IAuditsRepository;
from lib_domain.entities import Audits;

class AuditsRepository(IAuditsRepository.IAuditsRepository):
    iConnection: IConnection.IConnection = None;

    def __init__(self, iConnection: IConnection.IConnection):
        self.iConnection = iConnection;

    def SetStringConnection(self, value: str):
        self.iConnection.SetStringConnection(value);
        
    def Insert(self, _entity: Audits.Audits) -> Audits.Audits:
        self.iConnection.Open();
        entity = self.iConnection.Insert(_entity);
        self.iConnection.Close();
        return entity;