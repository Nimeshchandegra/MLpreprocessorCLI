import task_Description
def func_task():
    print()
    print('please enter the task you want to perform')
    print()
    task = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]
    for tasks in task:
        print(tasks)
    print()
    while 1:
        task_selected = int(
            input('select the task u want to perform(press 0 to exit):'))
        if task_selected == 0:
            print('exit')
            break


        elif task_selected == 1:
            print()
            # function for Data Description
            task_Description.func_task_Description()

        elif task_selected == 2:
            print('function for Handling NULL Values')
            # function for Handling NULL Values
            continue

        # function for Encoding Categorical Data
        elif task_selected == 3:
            print(' function for Encoding Categorical Data')
            # function for Encoding Categorical Data
            continue


        elif task_selected == 4:
            print('function for Feature Scaling ')
            # function for Feature Scaling
            continue


        elif task_selected == 5:
            print('function for Download the modified dataset')
            # function for Download the modified dataset
            continue
        else:
            print('please enter a valid input')

