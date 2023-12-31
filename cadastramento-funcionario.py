import textwrap
from tabulate import tabulate

departamento = {
    'funcionarios': []
}
def procurarFuncionario():
    try:
        mensagem = '''
        Buscar Funcionario por:
        
        [1] - ID Funcionario
        [2] - Nome do Funcionario
        [3] - CPF do Funcionario
        '''
        mensagem_dedent = textwrap.dedent(mensagem)
        opcao = int(input(mensagem_dedent))

        if opcao == 1:
            print('Procurar po ID')
        elif opcao == 2:
            print('Procurar por Nome')
        elif opcao == 3:
            print('Procurar por CPF')
        else:
            print('Opção inválida. Escolha uma opção válida (1, 2 ou 3).')

    except ValueError:
        print('Digite uma Opção Valida.')

class Funcionario:
    contador_id = 1

    def __init__(self, nome, sobrenome, cargo, salario):
        self.id = str(Funcionario.contador_id).zfill(5)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        Funcionario.contador_id += 1

def novo_funcionario():
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    cargo = input('Digite o cargo: ')
    salario = float(input('qual o valor do salario? '))
    funcionario = Funcionario(nome, sobrenome, cargo, salario)
    departamento['funcionarios'].append(funcionario.__dict__)

def excluir_funcionario():
    id_funcionario = str(input('Digite o ID do funcionário a ser excluído: '))
    funcionarios = departamento['funcionarios']
    for funcionario in funcionarios:
        if funcionario['id'] == id_funcionario:
            funcionarios.remove(funcionario)
            print('Funcionário excluído com sucesso.')
            return
    print('Funcionário não encontrado.')

def main():
    while True:
        menu = '''
        1 - Visualizar lista de funcionários
        2 - Adicionar funcionário
        3 - Excluir funcionário
        4 - Buscar Funcionario
        '''
        menu_dedent = textwrap.dedent(menu)
        opcao = int(input(menu_dedent))

        if opcao == 1:
            tabela = tabulate(departamento['funcionarios'], headers='keys', tablefmt='grid')
            print(tabela)
        elif opcao == 2:
            novo_funcionario()
        elif opcao == 3:
            excluir_funcionario()
        elif opcao == 4:
            procurarFuncionario()

main()
