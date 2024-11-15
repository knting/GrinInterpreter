def read_lines(path):
    """reads and strips the file"""
    try:
        with open(path, 'r') as file:
            file_lines = file.readlines()
            file_lines = [item.strip() for item in file_lines if item.strip()]
        return file_lines
    except FileNotFoundError:
        print('No such file or directory')
        return None


def contains_bracketed_symbol(symbol):
    if '[' in symbol and ']' in symbol:
        return True
    else:
        return False
