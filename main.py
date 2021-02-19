from app.services.dbservice import DBService
from sys import argv

if __name__ == '__main__':
    # print(argv[1])
    if len(argv) == 1:
        db_service = DBService(argv[1])
        db_service.run()
    else:
        print("Ejecutar el comando con el siguiente formato: python main.py <dbbname>")