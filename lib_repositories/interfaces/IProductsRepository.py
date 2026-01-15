from abc import ABC, abstractmethod;
from lib_domain.entities import Products;

class IProductsRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Select(self) -> list:
        pass;

    @abstractmethod
    def Where(self, _entity: Products.Products) -> list:
        pass;

    @abstractmethod
    def Insert(self, _entity: Products.Products) -> Products.Products:
        pass;

    @abstractmethod
    def Update(self, _entity: Products.Products) -> Products.Products:
        pass;

    @abstractmethod
    def Delete(self, _entity: Products.Products) -> Products.Products:
        pass;