import shutil 
import os

# create a function that accepts your image, the path of the directory on the server where you want to store the image, and the name of the saved image.
def _save_file_to_server(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file