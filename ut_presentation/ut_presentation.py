import sys;
import os;
sys.path.append("../");
import datetime;
from lib_domain.entities import Audits, Products, Types, Users;
from lib_repositories.interfaces import IConnection, IApisRepository, IAuditsRepository, IProductsRepository, IUsersRepository, ITypesRepository, IUsersTokenRepository;
from lib_repositories.implementations import Connection, ApisRepository, AuditsRepository, ProductsRepository, UsersRepository, TypesRepository;
from Core import Configuration, EntitiesCore;
from Connections.AuditsTest import AuditsTest as Connections_AuditsTest;
from Connections.UsersTest import UsersTest as Connections_UsersTest;
from Connections.ProductsTest import ProductsTest as Connections_ProductsTest;
from Repositories.AuditsTest import AuditsTest as Repositories_AuditsTest;
from Repositories.UsersTest import UsersTest as Repositories_UsersTest;
from Repositories.ProductsTest import ProductsTest as Repositories_ProductsTest;

Configuration.Configuration.Load();

def Run():
    Connections();
    Repositories();

def Connections():
    try:
        (Connections_AuditsTest()).Execute();
        (Connections_UsersTest()).Execute();
        (Connections_ProductsTest()).Execute();
        print("Passed Connections");
    except:
        print("Error Connections:" + str(sys.exc_info()));

def Repositories():
    try:
        (Repositories_AuditsTest()).Execute();
        (Repositories_UsersTest()).Execute();
        (Repositories_ProductsTest()).Execute();   
        print("Passed Repositories");   
    except:
        print("Error Repositories:" + str(sys.exc_info()));

print("Testing");
Run();