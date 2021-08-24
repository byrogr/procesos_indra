from app.services.dbservice import DBService
from sys import argv

if __name__ == '__main__':
    
    try:
        tbl_name = argv[2] if len(argv) == 3 else ""
        db_service = DBService(argv[1], tbl_name)
        db_service.run()
    except IndexError as e:
        print("Ejecutar el comando con el siguiente formato: python main.py <dbname> [tablename]")
