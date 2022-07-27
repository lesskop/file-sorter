# File sorter

![GitHub last commit](https://img.shields.io/github/last-commit/lesskop/file-sorter)
![GitHub repo size](https://img.shields.io/github/repo-size/lesskop/file-sorter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/lesskop/file-sorter)
![Stars](https://img.shields.io/github/stars/lesskop/file-sorter?style=social)

Python script for sorting files into folders by extensions

## Quick start

1. Open [config.py](config.py) and write the path to the folder where the sort will be performed:

```python
FOLDER_PATH = Path('drive:/folder/another-folder/yet-another-folder')
```

Example

```python
FOLDER_PATH = Path('D:/Downloads')
```

2. Set up a dictionary `SUBFOLDER_NAME_TO_EXTENSIONS` for your sorting method.

**Key** - subfolder name, **value** - tuple of file extensions for this subfolder.

```python
SUBFOLDER_NAME_TO_EXTENSIONS = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma'),
    'image': ('jpg', 'png', 'bmp', 'jpeg', 'svg', 'tif', 'tiff'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'pkg', 'deb'),
    'text': ('pdf', 'txt', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xlsx', 'xls', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
    # 'subfolder-name': ('extension', 'another-extension')
}
```

## Logs

You can check the logs in `logs/file_sorter.log` after script execution.

```
[18:08:01] INFO - Sorting files by extensions in d:\downloads
[18:08:01] INFO - winrar.zip ---> archive/winrar.zip
[18:08:01] INFO - cute cat.png ---> image/cute cat.png
[18:08:01] INFO - dissertation.docx ---> text/dissertation.docx
[18:08:01] INFO - Morbius.mkv ---> video/Morbius.mkv
[18:08:01] INFO - mvp.pptx ---> presentation/mvp.pptx
[18:08:01] INFO - salary.xlsx ---> spreadsheet/salary.xlsx
[18:08:01] INFO - there are no passwords.txt ---> text/there are no passwords.txt
[18:08:01] INFO - Script execution time: 0.01600000000144064 seconds
```

---
## Content

I did a general refactoring for this project so this content is out of date.

[YouTube video](https://youtu.be/kzVqBtrlr9o)

[Статья на Хабре](https://habr.com/ru/post/562362/)
