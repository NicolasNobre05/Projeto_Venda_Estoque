import mysql.connector
from mysql.connector import Error

# Configurações de conexão
HOST = 'localhost'
ROOT_USER = 'root'
ROOT_PASSWORD = 'admin'
DB_NAME = 'projetosvendasestoque'
NEW_USER = 'UserProjetosVendas'
NEW_PASSWORD = 'ProjetosVendas'

try:
    # Conectar como root
    connection = mysql.connector.connect(
        host=HOST,
        user=ROOT_USER,
        password=ROOT_PASSWORD
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Criar o usuário
        cursor.execute(f"CREATE USER IF NOT EXISTS '{NEW_USER}'@'%' IDENTIFIED BY '{NEW_PASSWORD}';")
        
        # Criar o banco de dados
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")

        # Conceder privilégios ao novo usuário
        cursor.execute(f"GRANT ALL PRIVILEGES ON `{DB_NAME}`.* TO '{NEW_USER}'@'%';")
        cursor.execute(f"GRANT PROCESS ON *.* TO '{NEW_USER}'@'%';")

        # Atualizar privilégios
        cursor.execute("FLUSH PRIVILEGES;")

        print("Banco de dados e usuário criados com sucesso!")

except Error as e:
    print(f"Erro: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
