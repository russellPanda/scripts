from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FileDirHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'文件被修改了{event.src_path}')
        # copy_f2f(event.src_path, dst_dir)

    def on_created(self, event):
        print(f'文件被创建了{event.src_path}')

    def on_deleted(self, event):
        print(f'文件被删除了{event.src_path}')




def watching_file(path: str):
    event_handler = FileDirHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("kaishi")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    path=r"D:\projects\pyProject\scripts\2"
    watching_file(path)