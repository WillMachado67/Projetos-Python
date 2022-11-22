"""
Faça uma lista de tarefas com as seguintes opções:
    adicioar tarefa
    lista de tarefas
    opção desfazer (a cada vez que chamamos, desfazer a ultima ação)
    opção refazer (a cada vez que chamamos, refazer a ultima opção)
"""


def fake_clear():
    print('\n' * 50)


def new_task():
    option = True
    while option:
        task = input('Digite uma nova tarefa:\n')
        if task == '':
            print('Você não digitou nada.')
        else:
            option = False
            fake_clear()
            return task_list.append(task)


def undo():
    option = True
    if not task_list:
        print('Você não tem nada para desfazer.\n')
    else:
        while option:
            fake_clear()
            select = input('Deseja realmente desfazer a ultima alteração?\n[1] Sim [2] Não\n')
            if select == '1':
                option = False
                removed = task_list.pop()
                undo_list.append(removed)
                fake_clear()
            elif select == '2':
                option = False
                fake_clear()
            else:
                print('Comando inválido.\n')


def redo():
    option = True
    if not undo_list:
        print('Você não tem nada para refazer.\n')
    else:
        while option:
            fake_clear()
            select = input('Deseja refazer a ultima alteração?\n[1] Sim [2] Nâo\n')
            if select == '1':
                option = False
                remake = undo_list.pop()
                task_list.append(remake)
                fake_clear()
            elif select == '2':
                option = False
                fake_clear()
            else:
                print('Comando inválido.')


def see_list():
    if not task_list:
        print('Você ainda não tem nenhuma lista de tarefas.\n')
    else:
        print(task_list)


def menu():
    start = True
    print('Bem vindo ao Lista de tarefas')
    while start:
        print('Escolha uma opção:')
        option = input('[1] Nova tarefa\n[2] Lista de tarefas\n[3] Desfazer \n[4] Refazer\n[5] Sair\n')
        if option == '1':
            fake_clear()
            new_task()
        elif option == '2':
            fake_clear()
            see_list()
        elif option == '3':
            fake_clear()
            undo()
        elif option == '4':
            fake_clear()
            redo()
        elif option == '5':
            fake_clear()
            start = False
            print('Obrigado por ultilizar Lista de tarefas.\nAté mais.')


undo_list = []
task_list = []
fake_clear()
menu()
