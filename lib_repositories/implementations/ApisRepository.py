from lib_repositories.interfaces import IConnection, IApisRepository;

class ApisRepository(IApisRepository.IApisRepository):
    iConnection: IConnection.IConnection = None;

    def __init__(self, iConnection: IConnection.IConnection):
        self.iConnection = iConnection;

    def SetStringConnection(self, value: str):
        self.iConnection.SetStringConnection(value);
        
    def Select(self) -> dict:
        response: dict = {};
        response["Protocol"] = "http://";
        response["Host"] = "localhost";

        hash_select: dict = {};
        hash_select["Request-Type"] = "Get";
        hash_select["Types"] = ":4041/Types/Select";
        hash_select["Products"] = ":4041/Products/Select";
        hash_select["Users"] = ":4041/Users/Select";
        response["Select"] = hash_select;

        hash_where: dict = {};
        hash_where["Request-Type"] = "Post";
        hash_where["Types"] = ":4041/Types/Where";
        hash_where["Products"] = ":4041/Products/Where";
        hash_where["Users"] = ":4041/Users/Where";
        response["Where"] = hash_where;

        hash_insert: dict = {};
        hash_insert["Request-Type"] = "Post";
        hash_insert["Types"] = ":4041/Types/Insert";
        hash_insert["Products"] = ":4041/Products/Insert";
        hash_insert["Users"] = ":4041/Users/Insert";
        response["Insert"] = hash_insert;

        hash_update: dict = {};
        hash_update["Request-Type"] = "Put";
        hash_update["Types"] = ":4041/Types/Update";
        hash_update["Products"] = ":4041/Products/Update";
        hash_update["Users"] = ":4041/Users/Update";
        response["Update"] = hash_update;

        hash_delete: dict = {};
        hash_delete["Request-Type"] = "Delete";
        hash_delete["Types"] = ":4041/Types/Update";
        hash_delete["Products"] = ":4041/Products/Update";
        hash_delete["Users"] = ":4041/Users/Update";
        response["Delete"] = hash_delete;

        return response;