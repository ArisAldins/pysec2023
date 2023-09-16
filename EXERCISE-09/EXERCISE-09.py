import os
import datetime

def list_files_recursive(directory):
    for root, _, files in os.walk(directory):
        # atstarpes
        depth = root.count(os.sep)
        indent = '----' * depth

        # izvada direktoriju
        print(f"{indent}{os.path.basename(root)} (Direktorija)")

        # izvada info par failiem direktorijā
        for filename in files:
            file_path = os.path.join(root, filename)
            file_stat = os.stat(file_path)

            # formatē laiku
            creation_time = datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

            # izvada failu detaļas
            print(f"{indent}---- Faila nosaukums: {filename} ")
            print(f"{indent}--------Izmērs: {file_stat.st_size} bytes")
            print(f"{indent}--------Izveidošanas laiks: {creation_time}")
            print(f"{indent}--------Piekļuve: {oct(file_stat.st_mode)[-3:]}")

# definē mājas direktoriju
start_directory = '/Users/Lektors/Desktop/var/log/messages/'

# izsauc funkciju, lai rekursīvi listētu failus un info
list_files_recursive(start_directory)
