import json;
import datetime;
from dataclasses import asdict;
from sqlalchemy import inspect;

class JsonHelper:
    @staticmethod
    def ConvertToString(data: dict) -> str:
        return json.dumps(data);

    @staticmethod
    def ListToString(data: list) -> str:
        response: dict = {};
        count: int = 0;
        for item in data:
            temp = asdict(item);
            for k in temp.keys():
                if "datetime" in str(type(temp[k])):
                    temp[k] = temp[k].strftime("%Y-%m-%d %H:%M:%S");
            response[str(count)] = temp;
            count = count + 1;
        return json.dumps(response);

    @staticmethod
    def ClassToString(data) -> str:
        print(type(data));
        response = asdict(data);
        for k in response.keys():
            if "datetime" in str(type(response[k])):
                response[k] = response[k].strftime("%Y-%m-%d %H:%M:%S");
        return json.dumps(response);

    @staticmethod
    def ConvertToObject(data: str, repeat: int = 0) -> dict:
        response: dict = json.loads(data);
        for count in range(0, repeat, 1):
            response = json.loads(response);
        return response;

    @staticmethod
    def ConvertToInstance(_type, data) -> object:
        instance = _type();
        mapper = inspect(_type);
        column_names = [col.name for col in mapper.columns];
        for key, value in data.items():
            if key.lower() in column_names:
                setter_name = f"Set{key.capitalize()}";
                if hasattr(instance, setter_name):
                    getattr(instance, setter_name)(value);
                else:
                    setattr(instance, key, value);
        return instance;

