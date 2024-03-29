import scanner
from app import App

def main():
    """Основная функция запуска приложения"""
    try:
        app = App()
        app.mainloop()
        #scanner.print_text('image.jpg')
    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == '__main__':
    main()
