from lib_repositories.interfaces import IConnection;
from sqlalchemy import create_engine, Column, Integer, String;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import sessionmaker, joinedload, relationship;
from sqlalchemy import ForeignKey, Column, Integer, String, DATE, DATETIME, Boolean, Enum, TEXT, DECIMAL, TIME;

class Connection(IConnection.IConnection):
    engine = None;
    session = None;
    stringConnection: str = None;

    def SetStringConnection(self, value: str):
        self.stringConnection = value;
        
    def Select(self, _type) -> list:
        if self.session == None or self.stringConnection == None:
            return [];
        return self.session.query(_type).all();
        
    def Join(self, _type, _related: list) -> list:
        if self.session == None or self.stringConnection == None:
            return [];
        query = self.session.query(_type);
        for field in _related:
            query.options(joinedload(field));
        return query.all();
        
    def Where(self, _type, _filter) -> list:
        if self.session == None or self.stringConnection == None:
            return [];
        return self.session.query(_type).filter(_filter).all();
        
    def Insert(self, entity) -> object:
        if self.session == None or self.stringConnection == None:
            return None;
        self.session.add(entity);
        self.session.commit();
        return entity;
        
    def Update(self, entity) -> object:
        if self.session == None or self.stringConnection == None:
            return None;
        attached_entity = self.session.merge(entity);
        self.session.commit();
        return entity;
        
    def Delete(self, entity) -> object:
        if self.session == None or self.stringConnection == None:
            return None;
        attached_entity = self.session.merge(entity);
        self.session.delete(attached_entity);
        self.session.commit();
        return entity;

    def Open(self) -> None:
        if self.stringConnection == None:
            return;
        if self.engine == None:
            engine = create_engine(self.stringConnection, echo=False); 
            Base = declarative_base();
            Base.metadata.create_all(engine);
        Session = sessionmaker(bind=engine);
        self.session = Session();

    def Close(self) -> None:
        if self.session == None or self.stringConnection == None:
            return;
        self.session.close();