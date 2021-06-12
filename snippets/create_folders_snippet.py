import os

# folder_path = 'disk:\\folder\\another-folder'
folder_path = 'd:\\downloads'

folder_names = ['folder', 'another-folder', 'and-another-one']


# also creates folders from dictionary keys
def create_folders_from_list(folder_names):
    for fn in folder_names:
        if not os.path.exists(os.path.join(folder_path, fn)):
            print("Creating", fn, 'folder\n')
            os.mkdir(os.path.join(folder_path, fn))


def create_folders(*folder_names):
    for fn in folder_names:
        if not os.path.exists(os.path.join(folder_path, fn)):
            print("Creating", fn, 'folder\n')
            os.mkdir(os.path.join(folder_path, fn))

# create_folders_from_list(folder_names)
# create_folders('folder', 'another-folder', 'and-another-one')
