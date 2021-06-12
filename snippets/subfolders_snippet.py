import os

# folder_path = 'disk:\\folder\\another-folder'
folder_path = 'd:\\downloads'


def get_subfolder_paths_list() -> list:
    subfolder_paths = [sp.path for sp in os.scandir(folder_path) if sp.is_dir()]

    return subfolder_paths


def get_subfolder_paths_generator():
    for sp in os.scandir(folder_path):
        if sp.is_dir():
            yield sp.path


def get_subfolder_names_list() -> list:
    subfolder_names = [os.path.split(sp)[-1] for sp in get_subfolder_paths_generator()]

    return subfolder_names


def get_subfolder_names_generator():
    for sp in get_subfolder_paths_generator():
        yield os.path.split(sp)[-1]


print('Subfolder paths list:\n', get_subfolder_paths_list())
print('\nSubfolder names list:\n', get_subfolder_names_list())

# for i in get_subfolder_paths_generator():
#     print(i)
#
# for i in get_subfolder_names_generator():
#     print(i)
