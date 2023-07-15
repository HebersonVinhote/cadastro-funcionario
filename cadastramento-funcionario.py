import textwrap

departamento = {
    'funcionarios': []
}

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
        1 - Para ver os funcionários
        2 - Adicionar funcionário
        3 - Excluir funcionário
        '''
        menu_dedent = textwrap.dedent(menu)
        opcao = int(input(menu_dedent))

        if opcao == 2:
            novo_funcionario()
        elif opcao == 3:
            excluir_funcionario()
        elif opcao == 1:
            print(departamento)

main()
