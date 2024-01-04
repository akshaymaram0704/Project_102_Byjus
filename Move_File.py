import os
import shutil


from_dir = "/Users/akshaymaram/Downloads" 
to_dir = "/Users/akshaymaram/Documents/Document_Files"  


list_of_files = os.listdir(from_dir)


print("List of Files in Downloads Folder:")
print(list_of_files)


for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if not extension:
        continue


    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", file_name)

        if os.path.exists(path2):
            print(f"Moving {file_name} to Document_Files folder.")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Moving {file_name} to Document_Files folder.")
            shutil.move(path1, path3)

print("File segregation completed.")
