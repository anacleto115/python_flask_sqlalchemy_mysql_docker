import sys;
import datetime;
from lib_domain.core import JsonHelper;
from lib_domain.entities import Users;
from lib_repositories.interfaces import IUsersRepository;
from core import Configuration;

class TokenService:
    iRepository: IUsersRepository.IUsersRepository = None;

    def __init__(self, iRepository: IUsersRepository.IUsersRepository):
        self.iRepository = iRepository;

        stringConnection: str = Configuration.Configuration.Get("db.string_conexion");
        self.iRepository.SetStringConnection(stringConnection);

    def Version(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);

            response["Version"] = Configuration.Configuration.Get("app.version");
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Authenticate(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);
            entity: Users.Users = JsonHelper.JsonHelper.ConvertToInstance(Users.Users, data["Entity"]);
            
            _list: list = self.iRepository.Where(entity);
            if len(_list) == 0:
                response["Error"] = "lbMissingInformation";
                return JsonHelper.JsonHelper.ConvertToString(response);

            entity = _list[0];
            response["Token"] = self.iRepository.CreateCode(entity, Configuration.Configuration.Get("app.secret"));
            
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);