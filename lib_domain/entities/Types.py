from dataclasses import dataclass;
from sqlalchemy.orm import relationship;
from sqlalchemy import Column, Integer, String, DATE, DATETIME, Boolean, Enum, TEXT, DECIMAL, TIME;
from .base import Base;

@dataclass
class Types(Base):
    __tablename__ = 'types';
    __allow_unmapped__ = True;

    id: int = Column(Integer, primary_key=True, autoincrement=True);
    name: str = Column(String(150), nullable=False);
    
    _products: list = relationship("Products", back_populates="_type");
    
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    def GetName(self) -> str:
        return self.name;
    def SetName(self, value: str) -> None:
        self.name = value;