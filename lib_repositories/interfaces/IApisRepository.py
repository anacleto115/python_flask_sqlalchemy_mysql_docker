from abc import ABC, abstractmethod;

class IApisRepository:
    @abstractmethod
    def SetStringConnection(self, value: str):
        pass;

    @abstractmethod
    def Select(self) -> dict:
        pass;