import sys;
import datetime;
from lib_domain.core import JsonHelper;
from lib_domain.entities import Types;
from lib_repositories.interfaces import ITypesRepository, IUsersRepository;
from core import Configuration;

class TypesService:
    iRepository: ITypesRepository.ITypesRepository = None;
    iUsersRepository: IUsersRepository.IUsersRepository = None;

    def __init__(self, iRepository: ITypesRepository.ITypesRepository, iUsersRepository: IUsersRepository.IUsersRepository):
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

            response["Entities"] = JsonHelper.JsonHelper.ListToString(self.iRepository.Select());
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);

    def Where(self, income: str, authorization: str) -> str:
        response: dict = { };
        try:
            if not self.iUsersRepository.CheckCode(authorization, Configuration.Configuration.Get("app.secret")):
                response["Error"] = "lbNotAutentication";
                return JsonHelper.JsonHelper.ConvertToString(response);

            data: dict = JsonHelper.JsonHelper.ConvertToObject(income);
            entity: Types.Types = JsonHelper.JsonHelper.ConvertToInstance(Types.Types, data["Entity"]);
            
            response["Entities"] = JsonHelper.JsonHelper.ListToString(self.iRepository.Where(entity));
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
            entity: Types.Types = JsonHelper.JsonHelper.ConvertToInstance(Types.Types, data["Entity"]);
            
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
            entity: Types.Types = JsonHelper.JsonHelper.ConvertToInstance(Types.Types, data["Entity"]);
            
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
            entity: Types.Types = JsonHelper.JsonHelper.ConvertToInstance(Types.Types, data["Entity"]);
            
            response["Entity"] = JsonHelper.JsonHelper.ClassToString(self.iRepository.Delete(entity));
            response["Response"] = "Ok";
            response["Date"] = str(datetime.datetime.now());
            return JsonHelper.JsonHelper.ConvertToString(response);
        except:
            response["Error"] = str(sys.exc_info());
            return JsonHelper.JsonHelper.ConvertToString(response);