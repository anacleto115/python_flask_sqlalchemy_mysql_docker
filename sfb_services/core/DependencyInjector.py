from lib_repositories.interfaces import IConnection, IApisRepository, IAuditsRepository, IProductsRepository, IUsersRepository, ITypesRepository, IUsersTokenRepository;
from lib_repositories.implementations import Connection, ApisRepository, AuditsRepository, ProductsRepository, UsersRepository, TypesRepository;
from dependency_injector import containers, providers;

class DependencyInjector(containers.DeclarativeContainer):
    iConnection = providers.Factory(Connection.Connection);
    iApisRepository = providers.Factory(ApisRepository.ApisRepository, iConnection=iConnection);
    iAuditsRepository = providers.Factory(AuditsRepository.AuditsRepository, iConnection=iConnection);
    iTypesRepository = providers.Factory(TypesRepository.TypesRepository, iAuditsRepository=iAuditsRepository, iConnection=iConnection);
    iProductsRepository = providers.Factory(ProductsRepository.ProductsRepository, iAuditsRepository=iAuditsRepository, iConnection=iConnection);
    iUsersRepository = providers.Factory(UsersRepository.UsersRepository, iAuditsRepository=iAuditsRepository, iConnection=iConnection);
