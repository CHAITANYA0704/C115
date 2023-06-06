import os

source =  "C:/Users/salun/OneDrive/Desktop/Python/PRO-C113-Student-Boilerplate-main-main/DownloadAndMove.py"

dest =  "C:/Users/salun/OneDrive/Desktop/Python/PRO-C113-Student-Boilerplate-main-main/DownloadAndMove1.py"

os.rename(source, dest)
print("source Path renamed to destination path successfully")