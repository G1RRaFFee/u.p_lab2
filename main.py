import argparse
import os
import logging
from urllib.parse import urlparse
from src.core.service.hyperlink_service import HyperlinkSearchService
from src.infrastructure.container import Container
from requests.exceptions import RequestException

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def validate_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def handle_file_input(file_path: str, hyperlink_search_controller) -> dict:
    if not os.path.exists(file_path):
        logger.error(f"Error: The file {file_path} does not exist.")
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return hyperlink_search_controller.search_in_file(file_path)

def handle_url_input(url: str, hyperlink_search_controller) -> dict:
    if not validate_url(url):
        logger.error(f"Error: The URL {url} is not valid.")
        raise ValueError(f"The URL {url} is not valid.")
    
    try:
        return hyperlink_search_controller.search_in_url(url)
    except RequestException as e:
        logger.error(f"Error: Failed to fetch URL {url}. {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Search hyperlinks in text, file, or URL.")
    parser.add_argument('--input', help="Text to search for hyperlinks.")
    parser.add_argument('--file', help="File path to search for hyperlinks.")
    parser.add_argument('--url', help="URL to search for hyperlinks.")
    parser.add_argument('--output', required=True, help="Output JSON file to save results.")
    
    args = parser.parse_args()

    container = Container()
    hyperlink_search_controller = container.hyperlink_search_controller()

    result = None

    if args.input:
        result = hyperlink_search_controller.search_in_text(args.input)
    elif args.file:
        try:
            result = handle_file_input(args.file, hyperlink_search_controller)
        except FileNotFoundError:
            return
    elif args.url:
        try:
            result = handle_url_input(args.url, hyperlink_search_controller)
        except (ValueError, RequestException):
            return
    else:
        logger.error("Error: You must provide either --input, --file, or --url.")
        return
    
    hyperlink_search_service = HyperlinkSearchService(container.file_repository())
    hyperlink_search_service.save_results(result, args.output)

    logger.info(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
