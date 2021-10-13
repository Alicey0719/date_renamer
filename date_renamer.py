from pathlib import Path
import datetime
import shutil
import glob
import sys
import os

def file_move(from_file_path, to_dir_path):
    shutil.move(from_file_path, to_dir_path)

def get_filedate(path):
    path = Path(path)
    time = datetime.date.fromtimestamp(path.stat().st_mtime)
    return time

def get_filelist(dir_path):
    l = glob.glob(dir_path+'[!*.py]')
    # print(l)
    return l

def main():
    ## pathの取得
    try:
        filelist = get_filelist(sys.argv[1])
    except IndexError:
        print('ERROR:引数に対象を指定してください.')

    ## 移動処理
    for f in filelist:
        fdate = get_filedate(f)
        try:
            os.mkdir(str(fdate))
        except FileExistsError:
            pass
        file_move(f, str(fdate)+'/'+f)


if __name__ == '__main__': main()