"""

supported_extension=['.csv']

def data_Input(data):
    filename, file_extension = os.path.splitext(data)

    if file_extension != supported_extension:
        print('provide file name with pathand extension')
    else:
        try:
            df=pd.read_csv(filename+file_extension)
            return df
        except:
            return print("dataset not found please provide valid file")



def show_columns(data):
    column_name=data.columns
    for columns in column_name:
        print (columns+'\t')
        return column_name



def target_column(column_name):
    target_columns = input('please select the target column:')
    i = 0
    for column in column_name:
        if target_columns == column:
            return column

        else:
            i = 2
            continue
    if i == 2:
        i = 0
        print('please enter valid column')
        return target_column(column_name)



def column_info(dataset):
    return dataset.info()



def column_describe(dataset):
    return dataset.describe()



def spec_col_describe(dataset,column_name):
    return dataset[column_name].describe()



def display_dataset(dataset):
    return dataset



def to_lower_case(col):

    for i in range(len(col)):
        col[i] = col[i].lower()
    return col

"""



