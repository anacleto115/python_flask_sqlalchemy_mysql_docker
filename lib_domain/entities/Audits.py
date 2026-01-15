import datetime;
from dataclasses import dataclass;
from sqlalchemy import Column, Integer, String, DATE, DATETIME, Boolean, Enum, TEXT, DECIMAL, TIME;
from .base import Base;

@dataclass
class Audits(Base):
    __tablename__ = 'audits';

    id: int = Column(Integer, primary_key=True, autoincrement=True);
    action: str = Column(String(150), nullable=False);
    description: str = Column(String(500), nullable=False);    
    date: datetime = Column(DATE, nullable=False);

    def __init__(self, action: str, description: str):
        self.action = action;
        self.description = description;
        self.date = datetime.datetime.now();

    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    def GetAction(self) -> str:
        return self.action;
    def SetAction(self, value: str) -> None:
        self.action = value;
        
    def GetDescription(self) -> str:
        return self.description;
    def SetDescription(self, value: str) -> None:
        self.description = value;
        
    def GetDate(self) -> datetime:
        return self.date;
    def SetDate(self, value: datetime) -> None:
        self.date = value;