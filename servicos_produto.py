from connection import get_connect

def cadastro_produto():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        produto = input('Digite a descrição do produto: ').strip()
        preco = float(input('Digite o preço: ').strip().replace(',', '.'))
        quantidade = int(input('Digite a quantidade: '))

        cursor.execute('INSERT INTO TB_PRODUTO(descricao, preco, quantidade) VALUES (?, ?, ?)',
                       (produto, preco, quantidade)
        )
        conn.commit()
        print('Produto cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao cadastrar produto: {e}')

def editar_produto():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        produto_novo = input('Digite o produto que deseja editar: ').strip()

        cursor.execute('SELECT DESCRICAO FROM TB_PRODUTO')
        produtos = cursor.fetchall()
        if produto_novo in produtos:
            print('Produto encontrado!')
            nova_desc = input('Digite a nova descrição do produto: ').strip()
            preco_novo = int(input('Digite o novo preço: ')).strip().replace(',','.')
            quantidade_nova = int(input('Digite a nova quantidade: '))
            id = input('Digite o ID do produto: ')
            if nova_desc:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (nova_desc, id))
            if preco_novo:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (preco_novo, id))
            if quantidade_nova:
                cursor.execute('UPDATE SET DESC = ?, WHERE ID = ?',
                                (quantidade_nova, id))
            

            conn.commit()
        else:
            print('Esse produto não existe')
    except Exception as e:
            print('Falha ao editar produto!')



def listar_produtos():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT DESCRICAO, PRECO, QUANTIDADE FROM TB_PRODUTO')
        produtos = cursor.fetchall()
        print(produtos)
            

            
    except Exception as e:
        print('Não há produto registrado!')

def excluir_produto(id):
    try:
        conn = get_connect()
        cursor = conn.cursor()
        produto = input('Digite o id do produto que deseja excluir: ').strip()
        
        
        cursor.execute('DELETE FROM TB_PRODUTO WHERE ID = ?', (produto,))

        conn.commit()

    except Exception as e:
        print('Falha ao encontrar produto')

def vender(qtd_saida):
    try:
        conn = get_connect()
        cursor = conn.cursor()

        produto_id = input('Digite o id do produto que deseja vender: ').strip()

        cursor.execute('SELECT QUANTIDADE FROM TB_PRODUTO WHERE ID = ?', (produto_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print('Produto não encontrado!')
            return

        qtd_banco = resultado[0]

        if qtd_banco <= 0:
            print('Produto esgotado')
            return

        if qtd_banco < qtd_saida:
            print('Quantidade do banco insuficiente.')
            return

        qtd_restante = qtd_banco - qtd_saida

        # Atualiza a quantidade no banco
        cursor.execute('UPDATE TB_PRODUTO SET QUANTIDADE = ? WHERE ID = ?', (qtd_restante, produto_id))
        conn.commit()

        print(f'Venda realizada com sucesso! Quantidade restante: {qtd_restante}')

    except Exception as e:
        print(f'Falha ao vender produto: {e}')
    finally:
        conn.close()


def tabela_produto():
    try:
        conn = get_connect()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_PRODUTO(
            ID INTEGER PRIMARY KEY,
            DESCRICAO VARCHAR(120) NOT NULL,
            PRECO DECIMAL(10,2) UNIQUE,
            QUANTIDADE INTEGER
        );
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
