from lib_repositories.interfaces import IConnection, IAuditsRepository, ITypesRepository;
from lib_domain.entities import Audits, Types;

class TypesRepository(ITypesRepository.ITypesRepository):
    iConnection: IConnection.IConnection = None;
    iAuditsRepository: IAuditsRepository.IAuditsRepository = None;

    def __init__(self, iConnection: IConnection.IConnection, iAuditsRepository: IAuditsRepository.IAuditsRepository):
        self.iConnection = iConnection;
        self.iAuditsRepository = iAuditsRepository;

    def SetStringConnection(self, value: str):
        self.iConnection.SetStringConnection(value);
        
    def Select(self) -> list:
        self.iConnection.Open();
        _list: list = self.iConnection.Select(Types.Types);
        for item in _list:
            item._products = None;
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Types.Types", ""));
        return _list;
        
    def Insert(self, _entity: Types.Types) -> Types.Types:
        self.iConnection.Open();
        entity = self.iConnection.Insert(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Types.Insert", ""));
        return entity;
        
    def Update(self, _entity: Types.Types) -> Types.Types:
        self.iConnection.Open();
        entity = self.iConnection.Update(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Types.Update", ""));
        return entity;
        
    def Delete(self, _entity: Types.Types) -> Types.Types:
        self.iConnection.Open();
        entity = self.iConnection.Delete(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Types.Delete", ""));
        return entity;