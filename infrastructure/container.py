from dependency_injector import containers, providers
from core.service.hyperlink_service import HyperlinkSearchService
from infrastructure.repository.file_repository import FileRepository
from infrastructure.controller.hyperlink_controller import HyperlinkSearchController

class Container(containers.DeclarativeContainer):
    # Репозиторий для работы с файлами
    file_repository = providers.Singleton(FileRepository)
    
    # Сервис для поиска ссылок
    hyperlink_search_service = providers.Factory(
        HyperlinkSearchService, file_repository=file_repository
    )
    
    # Контроллер для обработки запросов
    hyperlink_search_controller = providers.Factory(
        HyperlinkSearchController, 
        hyperlink_search_service=hyperlink_search_service
    )
