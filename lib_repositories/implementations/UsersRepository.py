import jwt; 
import datetime;
from lib_repositories.interfaces import IConnection, IAuditsRepository, IUsersRepository, IUsersTokenRepository;
from lib_domain.entities import Audits, Users;

class UsersRepository(IUsersRepository.IUsersRepository, IUsersTokenRepository.IUsersTokenRepository):
    iConnection: IConnection.IConnection = None;
    iAuditsRepository: IAuditsRepository.IAuditsRepository = None;

    def __init__(self, iConnection: IConnection.IConnection, iAuditsRepository: IAuditsRepository.IAuditsRepository):
        self.iConnection = iConnection;
        self.iAuditsRepository = iAuditsRepository;

    def SetStringConnection(self, value: str):
        self.iConnection.SetStringConnection(value);
        
    def Select(self) -> list:
        self.iConnection.Open();
        _list: list = self.iConnection.Select(Users.Users);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Users.Select", ""));
        return _list;
        
    def Where(self, _entity: Users.Users) -> list:
        self.iConnection.Open();
        _list: list = self.iConnection.Where(Users.Users, (Users.Users.name == _entity.GetName()) & (Users.Users.password == _entity.GetPassword()) & (Users.Users.active == True));
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Users.Where", ""));
        return _list;
        
    def Insert(self, _entity: Users.Users) -> Users.Users:
        self.iConnection.Open();
        entity = self.iConnection.Insert(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Users.Insert", ""));
        return entity;
        
    def Update(self, _entity: Users.Users) -> Users.Users:
        self.iConnection.Open();
        entity = self.iConnection.Update(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Users.Update", ""));
        return entity;
        
    def Delete(self, _entity: Users.Users) -> Users.Users:
        self.iConnection.Open();
        entity = self.iConnection.Delete(_entity);
        self.iConnection.Close();
        self.iAuditsRepository.Insert(Audits.Audits("Users.Delete", ""));
        return entity;

    def CreateCode(self, _entity: Users.Users, code: str) -> str:
        payload = {
            "Data": _entity.GetName(),
            "Expire": (datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)).strftime("%Y-%m-%d %H:%M:%S")
        }
        return jwt.encode(payload, code, algorithm="HS256");

    def CheckCode(self, _data: str, code: str) -> bool:
        result = jwt.decode(_data, code, algorithms=["HS256"]);
        name: str = result["Data"];
        expire: datetime.datetime = datetime.datetime.strptime(result["Expire"], "%Y-%m-%d %H:%M:%S");

        if datetime.datetime.utcnow() > expire:
            return False;

        self.iConnection.Open();
        _list: list = self.iConnection.Where(Users.Users, (Users.Users.name == name) & (Users.Users.active == True));
        self.iConnection.Close();
        
        return len(_list) != 0;