from abc import ABC, abstractmethod;

class IConnection:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Select(self, _type) -> list:
        pass;

    @abstractmethod
    def Join(self, _type, _related: list) -> list:
        pass;

    @abstractmethod
    def Where(self, _type, _filter) -> list:
        pass;

    @abstractmethod
    def Insert(self, _entity) -> object:
        pass;

    @abstractmethod
    def Update(self, _entity) -> object:
        pass;

    @abstractmethod
    def Delete(self, _entity) -> object:
        pass;

    @abstractmethod
    def Open(self) -> None:
        pass;

    @abstractmethod
    def Close(self) -> None:
        pass;