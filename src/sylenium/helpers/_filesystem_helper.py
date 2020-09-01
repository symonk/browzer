import pathlib


def does_file_exist(path_to_file: str) -> bool:
    """
    Performs a simple exists check on a given file path
    """
    path = pathlib.Path(path_to_file)
    return path.exists()
