import sys;
import os;
sys.path.append("../");
import datetime;
from flask import Flask, jsonify, request;
from implementations import ProductsService, TypesService, UsersService;
from core import Configuration, DependencyInjector;
app = Flask(__name__);

Configuration.Configuration.Load();
dependencyInjector: DependencyInjector.DependencyInjector = DependencyInjector.DependencyInjector();
productsService: ProductsService.ProductsService = ProductsService.ProductsService(dependencyInjector.iProductsRepository(), dependencyInjector.iUsersRepository());
typesService: TypesService.TypesService = TypesService.TypesService(dependencyInjector.iTypesRepository(), dependencyInjector.iUsersRepository());
usersService: UsersService.UsersService = UsersService.UsersService(dependencyInjector.iUsersRepository());

@app.route('/Products/Select', methods=["Get"])
def Products_Select() -> str :
    return productsService.Select(request.data, request.headers.get("Authorization"));

@app.route('/Products/Where', methods=["Post"])
def Products_Where() -> str :
    return productsService.Where(request.data, request.headers.get("Authorization"));

@app.route('/Products/Insert', methods=["Post"])
def Products_Insert() -> str :
    return productsService.Insert(request.data, request.headers.get("Authorization"));

@app.route('/Products/Update', methods=["Put"])
def Products_Update() -> str :
    return productsService.Update(request.data, request.headers.get("Authorization"));

@app.route('/Products/Delete', methods=["Delete"])
def Products_Delete() -> str :
    return productsService.Delete(request.data, request.headers.get("Authorization"));

@app.route('/Types/Select', methods=["Get"])
def Types_Select() -> str :
    return typesService.Select(request.data, request.headers.get("Authorization"));

@app.route('/Types/Where', methods=["Post"])
def Types_Where() -> str :
    return typesService.Where(request.data, request.headers.get("Authorization"));

@app.route('/Types/Insert', methods=["Post"])
def Types_Insert() -> str :
    return typesService.Insert(request.data, request.headers.get("Authorization"));

@app.route('/Types/Update', methods=["Put"])
def Types_Update() -> str :
    return typesService.Update(request.data, request.headers.get("Authorization"));

@app.route('/Types/Delete', methods=["Delete"])
def Types_Delete() -> str :
    return typesService.Delete(request.data, request.headers.get("Authorization"));

@app.route('/Users/Select', methods=["Get"])
def Users_Select() -> str :
    return usersService.Select(request.data, request.headers.get("Authorization"));

@app.route('/Users/Insert', methods=["Post"])
def Users_Insert() -> str :
    return usersService.Insert(request.data, request.headers.get("Authorization"));

@app.route('/Users/Update', methods=["Put"])
def Users_Update() -> str :
    return usersService.Update(request.data, request.headers.get("Authorization"));

@app.route('/Users/Delete', methods=["Delete"])
def Users_Delete() -> str :
    return usersService.Delete(request.data, request.headers.get("Authorization"));

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4041);