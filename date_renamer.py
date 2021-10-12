from pathlib import Path
import datetime

def file_move(from_file_path, to_dir_path):
    return

def get_filedate(path):
    path = Path(path)
    time = datetime.date.fromtimestamp(path.stat().st_mtime)
    return time

def main():
    a = get_filedate(r'test.jpg')
    print(type(a),a )

if __name__ == '__main__': main()