def read_file_in_binary(file_path):
    """Function for reading a file in Binary Format"""
    with open(file_path, "rb") as f:
        data = f.read()
        f.close()
    return data
