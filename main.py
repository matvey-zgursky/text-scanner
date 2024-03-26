import scanner
from app import App

def main():
    try:
        app = App()
        app.start()
        #scanner.print_text('image.jpg')
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == '__main__':
    main()
