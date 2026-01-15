from dataclasses import dataclass;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, Integer, String, DATE, DATETIME, Boolean, Enum, TEXT, DECIMAL, TIME;
from .base import Base;

@dataclass
class Users(Base):
    __tablename__ = 'users';

    id: int = Column(Integer, primary_key=True, autoincrement=True);
    name: str = Column(String(150), nullable=False);
    password: str = Column(String(150), nullable=False);
    active: bool = Column(Boolean, nullable=False);
    
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    def GetName(self) -> str:
        return self.name;
    def SetName(self, value: str) -> None:
        self.name = value;
        
    def GetPassword(self) -> str:
        return self.password;
    def SetPassword(self, value: str) -> None:
        self.password = value;
    
    def GetActive(self) -> bool:
        return self.active;
    def SetActive(self, value: bool) -> None:
        self.active = value;