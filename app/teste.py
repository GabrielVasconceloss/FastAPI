import psycopg2

# Configurações do banco de dados PostgreSQL
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "784512"
POSTGRES_DB = "mydatabase"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"

# Tente conectar ao banco de dados
try:
    connection = psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DB
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro na conexão: {e}")
finally:
    # Feche a conexão
    if connection:
        connection.close()