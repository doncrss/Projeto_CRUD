import servicos_usuario

def gerenciar_usuario(id):
    print('1 - Editar perfil')
    print('2 - Excluir conta')
    opcao = input ('Digite uma opção').strip()

    usuario = servicos_usuario.listar_usuario_id(id)
    print(f'{'-'*30} Editar o Usuário {usuario}! {'-'*30}')

    novo_nome = input('Digite o novo nome: ').strip().title()

    servicos_usuario.editar_usuario