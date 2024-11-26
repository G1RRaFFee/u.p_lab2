from dependency_injector import containers, providers

from src.core.service.hyperlink_service import HyperlinkSearchService
from src.infrastructure.repository.json_file_repository import JsonFileRepository
from src.infrastructure.controller.hyperlink_controller import HyperlinkSearchController

class Container(containers.DeclarativeContainer):
    file_repository = providers.Singleton(JsonFileRepository)
    hyperlink_search_service = providers.Factory(HyperlinkSearchService, file_repository=file_repository)
    hyperlink_search_controller = providers.Factory(HyperlinkSearchController, hyperlink_search_service=hyperlink_search_service)
