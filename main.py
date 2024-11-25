from infrastructure.controller.hyperlink_controller import HyperlinkController

def main():
    option = input("Choose input source (url/file/text): ").strip().lower()
    
    if option == "url":
        url = input("Enter URL: ")
        links = HyperlinkController.get_links_from_url(url)
    elif option == "file":
        file_path = input("Enter file path: ")
        links = HyperlinkController.get_links_from_file(file_path)
    elif option == "text":
        text = input("Enter text: ")
        links = HyperlinkController.get_links_from_text(text)
    else:
        print("Invalid option.")
        return

    print("Found links:")
    for link in links:
        print(link.url)

if __name__ == "__main__":
    main()
