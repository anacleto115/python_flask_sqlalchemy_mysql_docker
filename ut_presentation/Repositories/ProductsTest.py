import datetime;
from lib_domain.entities import Products;
from lib_repositories.interfaces import IConnection, IProductsRepository;
from lib_repositories.implementations import Connection, ProductsRepository, AuditsRepository;
from Core import Configuration, EntitiesCore;

class ProductsTest:
    iRepository: IProductsRepository.IProductsRepository = None;
    _list: list  = None;
    _entity: Products.Products = None;

    def __init__(self):
        iConnection = Connection.Connection();
        iConnection.SetStringConnection(Configuration.Configuration.Get("db.string_conexion"));

        self.iRepository = ProductsRepository.ProductsRepository(iConnection, AuditsRepository.AuditsRepository(iConnection));

    def Execute(self):
        assert self.Insert(), "Error";
        assert self.Update(), "Error";
        assert self.Select(), "Error";
        assert self.Delete(), "Error";

    def Insert(self) -> bool:
        self._entity = EntitiesCore.EntitiesCore.Products();
        self._entity = self.iRepository.Insert(self._entity);
        return True;

    def Update(self) -> bool:
        self._entity.SetActive(False);
        self._entity = self.iRepository.Update(self._entity);
        return True;

    def Select(self) -> bool:
        self._list = self.iRepository.Select();
        return len(self._list) > 0;

    def Delete(self) -> bool:
        self._entity = self.iRepository.Delete(self._entity);
        return True;