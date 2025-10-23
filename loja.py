from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

def Criar_usuario(nome, email, senha):
    opcao = input('Você é um usuário novo? S - Sim | N - Não: ').lower()
    if opcao == 's':
        try:
            conn = get_connet()
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
        listar_usuario()

def Verificar_usuario():
    email1 = input('Digite seu email: ').strip()
    senha1 = input('Digite sua senha: ').strip()

    try:
        conn = get_connet()
        cursor = conn.cursor()
        sha256.verify(senha, senha1)
        if senha == senha1:
        
            cursor.execute('SELECT EMAIL FROM TB_USUARIO')
            usuarios = cursor.fetchall()
            if email1 in usuarios:
                print('Login bem sucedido!')
            
            cadastro_produto()
        else:
            print('Esse login não existe!')
            opcoes = input('Deseja criar um login? S - Sim | N - Não: ').lower()
            if opcoes == 's':
                criar_usuario()
            elif opcoes == 'n':
                print('Saindo do sistema...')
                exit()

def Cadastro_produto():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        produto = input('Digite a descrição do produto: ').strip()
        preco = int(input('Digite o preço: ')).strip().replace(',','.')
        quantidade = int(input('Digite a quantidade: '))

        cursor.execute('INSERT INTO TB_PRODUTO(produto, preco, quantidade) VALUES (?, ?, ?)',
                       (produto, preco, quantidade)
        )
        conn.commit()
        print('Produto cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao cadastrar produto: {e}')

def Editar_produto():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        produto_novo = input('Digite o produto que deseja editar: ').strip()

        cursor.execute('SELECT DESCRICAO FROM TB_PRODUTO')
        produtos = cursor.fetchall()
        if produto_novo in produtos:
            print('Produto encontrado!')
            produto = input('Digite a nova descrição do produto: ').strip()
            preco_novo = int(input('Digite o novo preço: ')).strip().replace(',','.')
            quantidade_nova = int(input('Digite a nova quantidade: '))
            id = input('Digite o ID do produto: ')
            if produto:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (nova_desc, id))
            if preco_novo:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (preco_novo, id))
            if quantidade_nova:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (quantidade_nova, id))
            

            
        else:
            print('Esse produto não existe')
    except Exception as e:
            print('Falha ao editar produto!')


def Listar_produtos():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('SELECT produto, PRECO, QUANTIDADE FROM TB_PRODUTO')
        produtos = cursor.fetchall()
        print(produtos)
            

            
        except Exception as e:
            print('Não há produto registrado!')

def Vender(id,qtd_saida):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        produto = input('Digite o id do produto que deseja vender: ').strip()

        cursor.execute('SELECT ID FROM TB_PRODUTO')
        produtos = cursor.fetchall()
        if produto in produtos:
            if qtd_banco > 0
                if qtd_banco > qtd_saida
                    qtd_restante = qtd_banco - qtd_saida
                else:
                    print('Quantidade do banco insuficiente.')


    