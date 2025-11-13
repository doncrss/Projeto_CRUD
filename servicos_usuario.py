from Projeto_CRUD.models.usuario_model import Usuario
from sqlalchemy.orm import Session
session = Session()

def criar_usuario(usuario):
    usuario_db = Usuario(nome=usuario.nome, email =usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)

    session.add(usuario_db)
    session.commit()
    return usuario_db

def listar_usuario_email(email):
    usuario_db = session.query(Usuario).filter(Usuario.email == email).first()
    return usuario_db

def listar_usuario_id(id):
    usuarios_db = session.query(Usuario).all()
    return usuarios_db


def excluir_usuario(id):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).first()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return False

def editar_usuario(email, Usuario):
    usuario_db = session.query(Usuario).filter(Usuario.email == email).first()

    if not usuario_db:
        return None
    
    usuario_db.nome = Usuario.nome
    usuario_db.email = Usuario.email
    session.commit()
    return Usuario
def usuario_controller()
        usuario = servicos_usuario.listar_usuario_id(id)
        print(f'{'-'*30} Editar o Usuário {usuario}! {'-'*30}')

        novo_nome = input('Digite o novo nome: ').strip().title()

        servicos_usuario.editar_usuario