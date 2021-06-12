# File sorter

![GitHub last commit](https://img.shields.io/github/last-commit/lesskop/file-sorter)
![GitHub repo size](https://img.shields.io/github/repo-size/lesskop/file-sorter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/lesskop/file-sorter)
![Stars](https://img.shields.io/github/stars/lesskop/file-sorter?style=social)

Python script for sorting files into folders with flexible configuration

## Quick start
***
Open **file_sorter.py** and write down the path to the directory where the sort will be performed:

```python
folder_path = 'disk:\\folder\\another-folder'
# folder_path = 'd:\\downloads'
```

Set up a dictionary for your sorting method.

**Key** - folder name, **value** - list of file extensions for this folder.
```python
# key names will be folder names!
extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv'],

    'audio': ['mp3', 'wav', 'ogg'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'svg'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz'],

    # 'folder-name': ['extension-name', 'another-extension']
}
```
***
[YouTube](https://youtu.be/kzVqBtrlr9o)

[Habr](https://habr.com/ru/post/562362/)