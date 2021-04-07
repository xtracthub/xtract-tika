
import os
import tika
import time
from tika import parser
from queue import Queue
import threading
import json
# from random import randint
import argparse


class TikaParser:

    def __init__(self, write_path):
        self.shared_dir_q = Queue()
        self.mdata_to_save = Queue()
        self.weird_fails = 0
        self.runtime_fails = 0
        self.write_path = write_path
        self.cur_val = 0

    def thr_extract_metadata(self):

        while not self.shared_dir_q.empty():

            item = self.shared_dir_q.get()
            # exit()

            try:
                # opening pdf file
                time.sleep(0.01)  # minimum amount of buffer time to keep Tika from crashing with 'restart' issues.
                                  # Note that this is faster than simply 'not' sleeping (or sleeping < 10ms).

                t_ext_start = time.time()
                # print(f"Item: {item}")
                # print(type(item))
                parsed_pdf = parser.from_file(item)
            except IsADirectoryError as e:
                print("Actually a directory. Skipping!")
                continue
            except OSError as e2:
                print(e2)
                self.weird_fails += 1
                time.sleep(2)
                print(f"Current weird fails: {self.weird_fails}")
                continue
            except RuntimeError as e:
                self.runtime_fails += 1
                print(f"Current runtime fails: {self.runtime_fails}")
                continue

            # try:
            # opening

            # saving content of pdf
            # you can also bring text only, by parsed_pdf['text']
            # parsed_pdf['content'] returns string
            data = parsed_pdf['metadata']
            self.mdata_to_save.put('hi')

            write_path = os.path.join(self.write_path, str(self.cur_val))
            self.cur_val += 1
            t_ext_end = time.time()
            with open(write_path, 'w') as f:
                json.dump({'ext_time': t_ext_end-t_ext_start, 'mdata': data, 'timestamp': time.time()}, f)

    def extract_tika(self, dir_name, pct_to_transfer=0, num_thr=1):
        t0 = time.time()
        print("Phase 1: Configuring Tika...")
        tika.TikaClientOnly = True

        print("Phase 2: Crawling the files. Creating shared file list...")
        # First create full list of files in directory
        print(f"Dir name: {dir_name}")
        print(f"Pct to Transfer: {pct_to_transfer}")
        print(f"Num threads: {num_thr}")


        all_subdirs = os.listdir(dir_name)

        for subdir in all_subdirs:
            dir_full_path = os.path.join(dir_name, subdir)

            if os.path.isdir(dir_full_path):
                all_files = os.listdir(dir_full_path)

                for filename in all_files:
                    file_full_path = os.path.join(dir_full_path, filename)
                    self.shared_dir_q.put(file_full_path)
            # Otherwise it's a file.
            else:
                self.shared_dir_q.put(dir_full_path)

        print(f"Phase 3: Files crawled! Spinning up {num_thr} processing threads...")
        # Spinning up n threads -- this should be configured to the number of available cores.
        for i in range(0, num_thr):
            thr = threading.Thread(target=self.thr_extract_metadata, args=())
            thr.start()

        print(f"Number of files: {self.shared_dir_q.qsize()}")
        while True:
            print(f"Time elapsed: {time.time() - t0}")
            print(f"Number files extracted: {self.mdata_to_save.qsize()}")
            time.sleep(1)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Add args to Tika extraction run. ')
    p.add_argument('--num_threads', metavar='N', required=True)
    p.add_argument('--read_dir', metavar='R', required=True)
    p.add_argument('--write_dir', metavar='W', required=True)
    # dir_to_proc = "/project2/chard/skluzacek/data_to_process"
    # dir_to_proc = '/Users/tylerskluzacek/Desktop'
    # write_dir = '/Users/tylerskluzacek/Desktop/mdata'
    # write_dir = '/project2/chard/skluzacek/mdata'
    args = p.parse_args()
    print(args.write_dir)
    tp = TikaParser(write_path=str(args.write_dir))
    print(int(args.num_threads))
    tp.extract_tika(str(args.read_dir), pct_to_transfer=0, num_thr=int(args.num_threads))
