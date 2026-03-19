''' Change all .jpg and .jpeg files in a folder to .png (rename only) '''

import os

# Setup folder location, currently blank
folderLocation = r''

jpegCounter = 0
jpgCounter = 0

print('Searching for files to convert')
print("Checking in ", folderLocation)

# List dir prints out the contents of the folder location
for file in os.listdir(folderLocation):
    # For each file in the folder location, set it to the lower_file - Moving it to lower so we dont have to check twice
    lower_file = file.lower()

    # Combine the folder location and the file
    old_path = os.path.join(folderLocation, file)

    # If the lower file ends with jpeg
    if lower_file.endswith('.jpeg'):
        print('Found JPEG:', file)
        jpegCounter += 1

        # Split the string and find where it contains the . 
        # and change the string it has grabbed and set it too .png instead
        new_name = file[:file.rfind('.')] + '.png'
        # Combine the new path with the new location
        new_path = os.path.join(folderLocation, new_name)

        # Rename the old path to the new path
        os.rename(old_path, new_path)

    elif lower_file.endswith('.jpg'):
        print('Found JPG:', file)
        jpgCounter += 1

        new_name = file[:file.rfind('.')] + '.png'
        new_path = os.path.join(folderLocation, new_name)

        os.rename(old_path, new_path)

print(f"Converted {jpegCounter} JPEGs and {jpgCounter} JPGs.")