import sys;
import os;
sys.path.append("../");
import datetime;
from flask import Flask, jsonify, request;
from implementations import ApisService, TokenService;
from core import Configuration, DependencyInjector;
app = Flask(__name__);

Configuration.Configuration.Load();
dependencyInjector: DependencyInjector.DependencyInjector = DependencyInjector.DependencyInjector();
tokenService: TokenService.TokenService = TokenService.TokenService(dependencyInjector.iUsersRepository());
apisService: ApisService.ApisService = ApisService.ApisService(dependencyInjector.iApisRepository(), dependencyInjector.iUsersRepository());

@app.route('/Token/Version', methods=["Post"])
def Token_Version() -> str :
    return tokenService.Version(request.data, request.headers.get("Authorization"));

@app.route('/Token/Authenticate', methods=["Post"])
def Token_Authenticate() -> str :
    return tokenService.Authenticate(request.data, request.headers.get("Authorization"));

@app.route('/Apis/Select', methods=["Get"])
def Apis_Select() -> str :
    return apisService.Select(request.data, request.headers.get("Authorization"));

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4040);