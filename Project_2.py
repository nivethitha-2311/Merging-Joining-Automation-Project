import pandas as pd

def merging():

    filename1 = input('Enter the First File :')
    filename2 = input('Enter the Second File :')

    try:
        df1 = pd.read_csv(filename1)
        df2 = pd.read_csv(filename2)

    except FileNotFoundError:
        print('File Doesnot Exist')
        return
    except Exception as e:
        print('Error',e)
        return

    common_columns = list(set(df1.columns) & set(df2.columns))

    if len(common_columns) == 0:
        print("No Common Columns Found.")
        return

    print("\nCommon Columns Available:")
    for i, col in enumerate(common_columns, start=1):
        print(f"{i}. {col}")

    column = input("\nEnter the Common Column Name : ")

    if column not in common_columns:
        print("Invalid Column Name")
        return

    merge_type = input("Enter Merge Type (inner/outer/left/right) : ").lower()

    if merge_type not in ["inner", "outer", "left", "right"]:
        print("Invalid Merge Type")
        return

    result = pd.merge(df1,df2,on=column,how=merge_type)

    file = f"{merge_type.capitalize()}_Merged_{filename1}_And_{filename2}.csv"

    result.to_csv(file, index=False)

    print(f"{merge_type.capitalize()} Merging Completed...")
    print("File Saved as :", file)


def joining():
    
    filename1 = input('Enter the first File Name :')
    filename2 = input('Enter the Second File Name :')
    try:
        df1 = pd.read_csv(filename1)
        df2 = pd.read_csv(filename2)
    except FileNotFoundError:
        print('File Doesnot Exist')
        return
    except Exception as e:
        print('Error',e)
        return

    common_columns = list(set(df1.columns) & set(df2.columns))

    if len(common_columns) == 0:
        print("No Common Columns Found.")
        return

    print("\nCommon Columns Available:")
    for i, col in enumerate(common_columns, start=1):
        print(f"{i}. {col}")

    column = input("\nEnter the Common Column Name : ")

    if column not in common_columns:
        print("Invalid Column Name")
        return

    join_type = input("Enter Join Type (inner/outer/left/right) : ").lower()

    if join_type not in ["inner", "outer", "left", "right"]:
        print("Invalid Join Type")
        return

    df1_index = df1.set_index(column)
    df2_index = df2.set_index(column)

    result = df1_index.join(df2_index,how=join_type)

    file = f"{join_type.capitalize()}_Joined_{filename1}_And_{filename2}.csv"

    result.reset_index().to_csv(file, index=False)

    print(f"{join_type.capitalize()} Join Completed...")
    print("File Saved as :", file)

while True:

    print ('===========================')
    print('Data Cleaning and Merging Task')
    print ('===========================')

    print('1. Merging')
    print('2. Joining')
    print('3. Exit')

    try:

        num = int(input('Enter Your Choice :'))

        if num == 1:
            merging()

        elif num == 2:
            joining()

        elif num == 3:
            print('============ Thank You Visit Again ==============')
            break

        else:
            print('Invalid Choice ............. Please Try Again ..............')
    except ValueError:
        print(' Please Enter Numbers Only')