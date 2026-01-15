from lib_repositories.interfaces import IConnection, IAuditsRepository, IProductsRepository;
from lib_domain.entities import Audits, Products;

class ProductsRepository(IProductsRepository.IProductsRepository):
    iConnection: IConnection.IConnection = None;
    iAuditsRepository: IAuditsRepository.IAuditsRepository = None;

    def __init__(self, iConnection: IConnection.IConnection, iAuditsRepository: IAuditsRepository.IAuditsRepository):
        self.iConnection = iConnection;
        self.iAuditsRepository = iAuditsRepository;

    def SetStringConnection(self, value: str):
        self.iConnection.SetStringConnection(value);
        
    def Select(self) -> list:
        self.iConnection.Open();
        _list: list = self.iConnection.Join(Products.Products, [Products.Products._type]);
        for item in _list:
            item._type._products = None;
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Products.Select", ""));
        return _list;
        
    def Where(self, _entity: Products.Products) -> list:
        self.iConnection.Open();
        _list: list = self.iConnection.Where(Products.Products, Products.Products.name.like(f"%{_entity.GetName()}%"));
        for item in _list:
            item._type._products = None;
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Products.Where", ""));
        return _list;
        
    def Insert(self, _entity: Products.Products) -> Products.Products:
        self.iConnection.Open();
        entity = self.iConnection.Insert(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Products.Insert", ""));
        return entity;
        
    def Update(self, _entity: Products.Products) -> Products.Products:
        self.iConnection.Open();
        entity = self.iConnection.Update(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Products.Update", ""));
        return entity;
        
    def Delete(self, _entity: Products.Products) -> Products.Products:
        self.iConnection.Open();
        entity = self.iConnection.Delete(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Products.Delete", ""));
        return entity;