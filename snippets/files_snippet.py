import os

# folder_path = 'disk:\\folder\\another-folder'
folder_path = 'd:\\downloads'


def get_file_paths_list() -> list:
    file_paths = [fp.path for fp in os.scandir(folder_path) if not fp.is_dir()]

    return file_paths


def get_file_paths_generator():
    for fp in os.scandir(folder_path):
        if not fp.is_dir():
            yield fp.path


def get_file_names_list() -> list:
    file_names = [os.path.split(fp)[-1] for fp in get_file_paths_generator()]

    return file_names


def get_file_names_generator():
    for fp in get_file_paths_generator():
        yield os.path.split(fp)[-1]


print('File paths list:\n', get_file_paths_list())
print('\nFile names list:\n', get_file_names_list())

# for i in get_file_paths_generator():
#     print(i)
#
# for i in get_file_names_generator():
#     print(i)
