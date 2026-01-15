from abc import ABC, abstractmethod;
from lib_domain.entities import Types;

class ITypesRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Select(self) -> list:
        pass;

    @abstractmethod
    def Insert(self, _entity: Types.Types) -> Types.Types:
        pass;

    @abstractmethod
    def Update(self, _entity: Types.Types) -> Types.Types:
        pass;

    @abstractmethod
    def Delete(self, _entity: Types.Types) -> Types.Types:
        pass;