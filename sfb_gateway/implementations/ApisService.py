import sys;
import datetime;
from lib_domain.core import JsonHelper;
from lib_domain.entities import Users;
from lib_repositories.interfaces import IApisRepository, IUsersRepository;
from core import Configuration;

class ApisService:
    iRepository: IApisRepository.IApisRepository = None;
    iUsersRepository: IUsersRepository.IUsersRepository = None;

    def __init__(self, iRepository: IApisRepository.IApisRepository, iUsersRepository: IUsersRepository.IUsersRepository):
        self.iRepository = iRepository;
        self.iUsersRepository = iUsersRepository;

        stringConnection: str = Configuration.Configuration.Get("db.string_conexion");
        self.iRepository.SetStringConnection(stringConnection);
        self.iUsersRepository.SetStringConnection(stringConnection);

    def Select(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iUsersRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);

            response["Entities"] = self.iRepository.Select();
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);