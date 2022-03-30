
def func_task_Description():
    print()
    print('choose the task you want to perform for Data Description process')

    print()
    task_Description = [
        '1. describe all column',
        '2. describe a specific column ',
        '3. show dataset',
        '0. go to tasks selection'
    ]
    for tasks in task_Description:
        print(tasks)
    print()
    while True:

        task_selected_description = int(input('select the task u want to perform(press 0 to exit):'))
        if task_selected_description == 0:
            tasksmenu.func_task()
        elif task_selected_description == 1:
            function.column_info(dataset)
            # function column_describe(dataset)
            continue

        elif task_selected_description == 2:
            # function spec_col_describe(dataset,column_name)
            continue
        elif task_selected_description == 3:
            # function display_dataset(dataset):
            continue
        else:
            print('please enter a valid input')



