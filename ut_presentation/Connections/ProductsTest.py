import datetime;
from lib_domain.entities import Products;
from lib_repositories.interfaces import IConnection;
from lib_repositories.implementations import Connection;
from Core import Configuration, EntitiesCore;

class ProductsTest:
    iConnection: IConnection.IConnection = None;
    _list: list  = None;
    _entity: Products.Products = None;

    def __init__(self):
        self.iConnection = Connection.Connection();
        self.iConnection.SetStringConnection(Configuration.Configuration.Get("db.string_conexion"));

    def Execute(self):
        assert self.Insert(), "Error";
        assert self.Update(), "Error";
        assert self.Select(), "Error";
        assert self.Delete(), "Error";

    def Insert(self) -> bool:
        self._entity = EntitiesCore.EntitiesCore.Products();
        self.iConnection.Open();
        self._entity = self.iConnection.Insert(self._entity);
        self.iConnection.Close();
        return True;

    def Update(self) -> bool:
        self._entity.SetActive(False);
        self.iConnection.Open();
        self._entity = self.iConnection.Update(self._entity);
        self.iConnection.Close();
        return True;

    def Select(self) -> bool:
        self.iConnection.Open();
        self._list = self.iConnection.Select(Products.Products);
        self.iConnection.Close();
        return len(self._list) > 0;

    def Delete(self) -> bool:
        self.iConnection.Open();
        self._entity = self.iConnection.Delete(self._entity);
        self.iConnection.Close();
        return True;