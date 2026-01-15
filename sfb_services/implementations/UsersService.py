import sys;
import datetime;
from lib_domain.core import JsonHelper;
from lib_domain.entities import Users;
from lib_repositories.interfaces import IUsersRepository, IUsersRepository;
from core import Configuration;

class UsersService:
    iRepository: IUsersRepository.IUsersRepository = None;

    def __init__(self, iRepository: IUsersRepository.IUsersRepository):
        self.iRepository = iRepository;

        stringConnection: str = Configuration.Configuration.Get("db.string_conexion");
        self.iRepository.SetStringConnection(stringConnection);

    def Select(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);

            response["Entities"] = JsonHelper.JsonHelper.ListToString(self.iRepository.Select());
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Insert(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iUsersRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);
            entity: Users.Users = JsonHelper.JsonHelper.ConvertToInstance(Users.Users, data["Entity"]);
            
            response["Entity"] = JsonHelper.JsonHelper.ClassToString(self.iRepository.Insert(entity));
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Update(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iUsersRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);
            entity: Users.Users = JsonHelper.JsonHelper.ConvertToInstance(Users.Users, data["Entity"]);
            
            response["Entity"] = JsonHelper.JsonHelper.ClassToString(self.iRepository.Update(entity));
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Delete(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iUsersRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);
            entity: Users.Users = JsonHelper.JsonHelper.ConvertToInstance(Users.Users, data["Entity"]);
            
            response["Entity"] = JsonHelper.JsonHelper.ClassToString(self.iRepository.Delete(entity));
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);