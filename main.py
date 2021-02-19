from app.services.dbservice import DBService
from sys import argv

if __name__ == '__main__':
    # print(argv[1])
    try:
        db_service = DBService(argv[1])
        db_service.run()
    except IndexError as e:
        print("Ejecutar el comando con el siguiente formato: python main.py <dbbname>")