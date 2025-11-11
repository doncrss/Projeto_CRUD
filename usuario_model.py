from sqlalchemy import Column, Integer, String
from passlib.hash import pbkdf2_sha256 as sha256



class Usuario():
    __tablename__ = 'USUARIO'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)

    def gen_senha(self, senha):
        return sha256.hash(senha)
    
    def verifica_senha(self, senha):
        return sha256.hash(self.senha, senha)  
    
    