import os
import zipfile

# Get the current working directory
current_directory = os.getcwd()

# Define the name of the zip file
zip_file_name = "project_folder.zip"

# Create a zip file
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Walk through all files and directories in the current directory
    for foldername, subfolders, filenames in os.walk(current_directory):
        for filename in filenames:
            # Add each file to the zip file
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, current_directory))

# Print a success message
print(f"The current project folder has been zipped and saved as {zip_file_name}.")
