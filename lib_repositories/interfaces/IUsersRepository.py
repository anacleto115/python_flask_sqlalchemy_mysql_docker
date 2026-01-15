from abc import ABC, abstractmethod;
from lib_domain.entities import Users;

class IUsersRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Select(self) -> list:
        pass;

    @abstractmethod
    def Where(self, _entity: Users.Users) -> list:
        pass;

    @abstractmethod
    def Insert(self, _entity: Users.Users) -> Users.Users:
        pass;

    @abstractmethod
    def Update(self, _entity: Users.Users) -> Users.Users:
        pass;

    @abstractmethod
    def Delete(self, _entity: Users.Users) -> Users.Users:
        pass;