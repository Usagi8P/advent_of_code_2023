from os import path

def read_file(filename:str) -> str:
    filepath = path.join('data',filename)
    with open(filepath, 'r') as f:
        data = f.read()
    
    return data
