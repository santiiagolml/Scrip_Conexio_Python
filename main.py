import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sicagolf'
        )

        self.cursor = self.connection.cursor()
        print("Conexion establecida exitosamente!")

    def select_user(self, id):
        sql = 'SELECT id_usuario, nombre, apellidos, correo from usuarios WHERE id_usuario = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("nombre:", user[1])
            print("apellidos:", user[2])
            print("correo:", user[3])
        except Exception as e:
            raise
    
    def close (self):
        self.connection.close()
database = Database()
database.select_user(1)
database.close()