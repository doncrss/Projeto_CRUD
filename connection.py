from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///controle_usuario.db'

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print('Banco conectado com sucesso')

except Exception as e:
    print('Erro ao conectar com o banco de dados!')
Base = declarative_base()



if __name__ == '__main__':
    engine.connect()
    
