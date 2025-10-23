from connection import get_connect
from passlib.hash import pbkdf2_sha256 as sha256
import pwinput

def criar_usuario(nome, email, senha):
    opcao = input('Você é um usuário novo? S - Sim | N - Não: ').lower()
    if opcao == 's':
        try:
            conn = get_connect()
            cursor = conn.cursor()
            senha = sha256.hash(senha)
            cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                        (nome, email, senha)
            )
            conn.commit()
            print('Usuário cadastrado com sucesso!')

        except Exception as e:
            print(f'Falha ao criar usuario: {e}')
    elif opcao == 'n':
        verificar_usuario()

def verificar_usuario():
    email = input('Digite seu email: ').strip().lower()
    senha_digitada = pwinput.pwinput('Digite sua senha: ').strip()

    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM TB_USUARIO WHERE email = ?", (email,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Usuário não encontrado.")
            return False

        senha_hash = resultado[0]

        if sha256.verify(senha_digitada, senha_hash):
            print("Login bem-sucedido!")
            return True
        else:
            print("Senha incorreta.")
            return False
    except Exception as e:
        print(f'Falha ao verificar login: {e}')
        return False

def excluir_usuario(id):
    try:
        print(f'ID recebido: {id} (tipo: {type(id)})')  # debug
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TB_USUARIO WHERE ID=?", (id,))
        conn.commit()
    except Exception as e:
        print(f'Falha ao excluir usuário: {e}')

def criar_tabela():
    try:
        conn = get_connect()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
