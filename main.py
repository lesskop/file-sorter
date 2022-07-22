from typing import Iterable, Union
import time
import os

from config import *


class Folder:
    def __init__(self, path: Union[Path, str]) -> None:
        self.path = path

    def _get_subfolder_paths(self) -> Iterable:
        return (folder.path for folder in os.scandir(self.path) if folder.is_dir())

    def _get_file_paths(self) -> Iterable:
        return (file.path for file in os.scandir(self.path) if not file.is_dir())

    def _create_subfolder(self, subfolder_name: str) -> None:
        subfolder_path = self.path / subfolder_name
        if not subfolder_path.exists():
            subfolder_path.mkdir()

    def sort_files_by_extensions(self) -> None:
        for filepath in self._get_file_paths():
            path = Path(filepath)
            extension = filepath.split('.')[-1]

            if extension in EXTENSIONS:
                subfolder_name = get_subfolder_name_by_extension(extension)
                self._create_subfolder(subfolder_name)

                # Move file to subfolder
                path.rename(Path(self.path, subfolder_name, path.name))


def main() -> None:
    folder = Folder(FOLDER_PATH)
    print('Sorting files by extensions in', FOLDER_PATH)
    folder.sort_files_by_extensions()


if __name__ == "__main__":
    start_time = time.monotonic()
    main()
    print(f'Script execution time: {time.monotonic() - start_time} seconds')
