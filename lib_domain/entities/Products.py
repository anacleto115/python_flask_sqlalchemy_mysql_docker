import datetime;
import decimal;
from dataclasses import dataclass;
from lib_domain.entities import Types;
from sqlalchemy.orm import relationship;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import ForeignKey, Column, Integer, String, DATE, DATETIME, Boolean, Enum, TEXT, Float, TIME;
from .base import Base;

@dataclass
class Products(Base):
    __tablename__ = 'products';
    __allow_unmapped__ = True;
    
    id: int = Column(Integer, primary_key=True, autoincrement=True);
    name: str = Column(String(150), nullable=False);
    price: decimal = Column(Float(precision=2), nullable=False);
    expire: datetime = Column(DATE, nullable=False);
    type: int = Column(Integer, ForeignKey('types.id'), nullable=False);
    active: bool = Column(Boolean, nullable=False);
    image: str = Column(String(500), nullable=True);
        
    _type: Types.Types = relationship("Types", back_populates="_products");
    

    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    def GetName(self) -> str:
        return self.name;
    def SetName(self, value: str) -> None:
        self.name = value;
        
    def GetPrice(self) -> decimal:
        return self.price;
    def SetPrice(self, value: decimal) -> None:
        self.price = value;
            
    def GetExpire(self) -> datetime:
        return self.expire;
    def SetExpire(self, value: datetime) -> None:
        self.expire = value;
            
    def GetType(self) -> int:
        return self.type;
    def SetType(self, value: int) -> None:
        self.type = value;
            
    def GetActive(self) -> bool:
        return self.active;
    def SetActive(self, value: bool) -> None:
        self.active = value;
        
    def GetImage(self) -> str:
        return self.image;
    def SetImage(self, value: str) -> None:
        self.image = value;
    

    def Get_Type(self) -> Types.Types:
        return self._type;
    def Set_Type(self, value: Types.Types) -> None:
        self._type = value;