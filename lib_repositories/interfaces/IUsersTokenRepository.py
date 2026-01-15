from abc import ABC, abstractmethod;
from lib_domain.entities import Users;

class IUsersTokenRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def CreateCode(self, _entity: Users.Users, code: str) -> str:
        pass;

    @abstractmethod
    def CheckCode(self, _data: str, code: str) -> bool:
        pass;