import os

main_path = 'd:\\downloads'

folder_names = ['folder', 'another-folder', 'and-another-one']


# also creates folders from dictionary keys
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def create_folders(folder_path, *folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# create_folders_from_list(main_path, folder_names)
# create_folders(main_path, 'folder', 'another-folder', 'and-another-one')
