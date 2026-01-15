import datetime;
from lib_domain.entities import Audits, Products, Types, Users;

class EntitiesCore:
    @staticmethod
    def Audits() -> Audits.Audits:
        entity: Audits.Audits = Audits.Audits("Unit.Tests", "Pruebas-" + str(datetime.datetime.now()));
        return entity;

    @staticmethod
    def Types() -> Types.Types:
        entity: Types.Types = Types.Types();
        entity.SetName("Pruebas-" + str(datetime.datetime.now()));
        return entity;

    @staticmethod
    def Users() -> Users.Users:
        entity: Users.Users = Users.Users();
        entity.SetName("Pruebas-" + str(datetime.datetime.now()));
        entity.SetPassword("KGgsdk3dsf464hfksdf");
        entity.SetActive(True);
        return entity;

    @staticmethod
    def Products() -> Products.Products:
        type: Types.Types = Types.Types();
        type.SetId(1);

        entity: Products.Products = Products.Products();
        entity.SetName("Pruebas-" + str(datetime.datetime.now()));
        entity.SetPrice(5.0);
        entity.SetExpire(datetime.datetime.now());
        entity.SetType(type.GetId());
        entity.SetActive(True);
        entity.SetImage("654fgJHGjhdgdhfyi3432d1fg6sd7fg98BFjhdgfsdk5345");
        return entity;