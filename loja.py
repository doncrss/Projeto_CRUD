from connection import get_connect
from servicos_produto import vender, cadastro_produto, listar_produtos, excluir_produto, tabela_produto
from servicos_usuario import criar_usuario, criar_tabela, verificar_usuario, excluir_usuario
import pwinput
from app import barra_progresso
from Projeto_CRUD.models.usuario_model import Usuario


print('Seja bem vindo ao mercado dev! ')
def login():
    while True:

        opcao = input('Você é um usuário novo? S - Sim | N - Não: ').lower()
        if opcao == 's':
            nome = input('Digite seu nome: ')
            email = input('Digite seu email: ').strip().lower()
            senha = pwinput.pwinput('Digite sua senha: ').strip()

            usuario_controller.usuario_service.criar_usuario(nome, email, senha)
            usuario = Usuario(nome=nome, email=email, senha=senha)


            print('Usuário criado com sucesso! Faça login para continuar')
            print(f"Usuário salvo com email: '{email}'")

            verificar_usuario()
            break
        elif opcao == 'n':
            verificar_usuario()
            break
        else:
            print('Opção inválida')

def menu():
    while True:
        print('1 - Cadastrar produtos')
        print('2 - Listar produtos')
        print('3 - Vender produtos')
        print('4 - Excluir produtos') 
        print('5 - Excluir usuário')
        print('6 - Editar usuário')
        print('7 - Sair do sistema')

        opcao_menu = input('Digite o numero correspondente à ação desejada')
        match opcao_menu:
            case '1':
                tabela_produto()                
                cadastro_produto()
            case '2':
                listar_produtos()
            case '3':
                ids = int(input('Digite o id do produto desejado'))
                qtd_saida = int(input('Digite a quantidade do produto que você quer'))
                vender(qtd_saida)
            case '4':
                excluir = int(input('Digite o id do usuário que deseja excluir')).strip()
                excluir_produto(id)
            case '5':
                excluir_usuario(id)
                print('Usuário excluído com sucesso!')
            case '6':
                barra_progresso()


def main():
    criar_tabela()
    print('Seja bem vindo ao mercado dev!')
    login()
    tabela_produto()
    menu()

if __name__ == '__main__':
    main()






    