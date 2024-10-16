from database import add_task, get_tasks, complete_task, edit_task, delete_task

def show_menu():
    print("\nLista de Tarefas - Menu:")
    print("1. Exibir tarefas")
    print("2. Adicionar nova tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Editar uma tarefa")
    print("5. Excluir uma tarefa")
    print("6. Sair")

def display_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    print("\nTarefas:")
    for task in tasks:
        status = "✅" if task[3] == "Concluída" else "❌"
        print(f"{task[0]}. {task[1]} - {task[2]} [{status}]")

def add_new_task():
    title = input("Digite o título da tarefa: ")
    description = input("Digite a descrição da tarefa: ")
    add_task(title, description)
    print("Tarefa adicionada com sucesso!")

def mark_task_completed():
    task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
    complete_task(task_id)
    print("Tarefa marcada como concluída!")

def edit_existing_task():
    task_id = int(input("Digite o ID da tarefa a ser editada: "))
    title = input("Digite o novo título da tarefa: ")
    description = input("Digite a nova descrição da tarefa: ")
    edit_task(task_id, title, description)
    print("Tarefa editada com sucesso!")

def delete_existing_task():
    task_id = int(input("Digite o ID da tarefa a ser excluída: "))
    delete_task(task_id)
    print("Tarefa excluída com sucesso!")

def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")
        if choice == '1':
            tasks = get_tasks()
            display_tasks(tasks)
        elif choice == '2':
            add_new_task()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            edit_existing_task()
        elif choice == '5':
            delete_existing_task()
        elif choice == '6':
            print("Saindo do aplicativo. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
