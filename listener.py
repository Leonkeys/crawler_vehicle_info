import os
import subprocess
import time
import psutil

# ===setting===
FILE_DIR_PATH = "./output"
CHECK_INTERVAL = 120
MAX_NO_CHANGE_TIME = 1200
PYTHON_SERVICE_COMMOND = [r"C:\Users\chd\AppData\Local\Programs\Python\Python311\python.exe", "main.py"]

# status
last_size = -1
last_change_time = time.time()


def get_file_size(path):
    try:
        return os.path.getsize(path)
    except OSError:
        return -1


def kill_process_by_name(name):
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            cmdline = proc.info.get("cmdline")
            if not cmdline:
                continue
            if name in " ".join(cmdline):
                print(f"终止进程 PID={proc.info['pid']}")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue


def restart_service():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 文件未变化，重启服务")
    kill_process_by_name("main.py")
    time.sleep(3)
    subprocess.Popen(PYTHON_SERVICE_COMMOND)
    print(f"[{time.strftime('%Y-%m-%d: %H:%M:%S')}] 服务已重启")


def get_file_path(dir_path):
    subfolders = [os.path.join(dir_path, d) for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    if not subfolders:
        return None
    latest_folder = max(subfolders, key=os.path.getmtime)
    return os.path.abspath(latest_folder)


while True:
    current_file_dirpath = get_file_path(FILE_DIR_PATH)
    # current_file_dirpath = "./tmp"
    file_path = os.path.join(current_file_dirpath, "output.csv")
    # err_file_path = os.path.join(current_file_dirpath, "error_put.csv")
    current_size = get_file_size(file_path)
    # err_current_size = get_file_size(err_file_path)
    if current_size != last_size:
        last_size = current_size

        last_change_time = time.time()
    else:
        if time.time() - last_change_time >= MAX_NO_CHANGE_TIME:
            restart_service()
            last_change_time = time.time()
    time.sleep(CHECK_INTERVAL)
