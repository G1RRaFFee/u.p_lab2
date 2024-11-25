import argparse
from core.service.hyperlink_service import HyperlinkSearchService
import requests
from bs4 import BeautifulSoup
import argparse
import os
from infrastructure.container import Container

def main():
    parser = argparse.ArgumentParser(description="Search hyperlinks in text, file, or URL.")
    parser.add_argument('--input', help="Text to search for hyperlinks.")
    parser.add_argument('--file', help="File path to search for hyperlinks.")
    parser.add_argument('--url', help="URL to search for hyperlinks.")
    parser.add_argument('--output', required=True, help="Output JSON file to save results.")
    
    args = parser.parse_args()

    # Инициализируем DI контейнер
    container = Container()

    # Получаем контроллер из контейнера
    hyperlink_search_controller = container.hyperlink_search_controller()

    if args.input:
        # Поиск по тексту
        result = hyperlink_search_controller.search_in_text(args.input)
    elif args.file:
        # Поиск по файлу
        if not os.path.exists(args.file):
            print(f"Error: The file {args.file} does not exist.")
            return
        result = hyperlink_search_controller.search_in_file(args.file)
    elif args.url:
        result = hyperlink_search_controller.search_in_url(args.url)
    else:
        print("Error: You must provide either --input, --file, or --url.")
        return
    
    # Сохраняем результаты в файл
    hyperlink_search_service = HyperlinkSearchService(container.file_repository())
    hyperlink_search_service.save_results(result, args.output)

    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
