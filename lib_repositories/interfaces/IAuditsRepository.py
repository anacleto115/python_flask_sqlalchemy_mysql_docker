from abc import ABC, abstractmethod;
from lib_domain.entities import Audits;

class IAuditsRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Insert(self, _entity: Audits.Audits) -> Audits.Audits:
        pass;