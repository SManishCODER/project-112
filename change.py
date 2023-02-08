import os
import shutil

# .exe , .msi,  .gif, .png 

from_dir = "C:/Users/Manish/Downloads/C102_assets-main" 
to_dir = "C:/Users/Manish/Desktop/project112"
list_of_files = os.listdir(from_dir)


# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                      
        path2 = to_dir + '/' + "Image_Files"                     
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name  
        #print("path1 " , path1)
        #print("path3 ", path3)

      
        if os.path.exists(path2):
          print("Moving " + file_name + "........")

          # Move from path1 to path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + "........")
          shutil.move(path1, path3)