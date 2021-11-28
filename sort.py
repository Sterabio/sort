#!/usr/bin/env python
import os
import shutil
import argparse
import subprocess

path = ""
def main():
    parser = argparse.ArgumentParser(description ="cryptor")
    parser.add_argument("-p",'--path',action='store', dest='path',help="path")
    parser.add_argument("-e",'--extension',action='store', dest='type',help="file")
    parser.add_argument("-size",'--size',action='store_true', dest='size',help="size")
    args = parser.parse_args()
	 
    if args.path:
	    path = args.path
    else:
	    path = os.getcwd()
        

    if args.type:
        if os.path.exists(path):
            sort(path,args.type)
        else: 
            print("path not exists")
    if args.size:
        get_sizes(path)
    else:
        print("???")
    
def get_sizes(path):
    print(path)
    directory = os.listdir(path)
    #nbytes = sum(d.stat().st_size for d in os.scandir(path) if d.is_file())
    #print(nbytes)
    def getSize(filename):
        st = os.stat(filename)
        if os.path.isfile(filename):
            return st.st_size
        else: 
            nbytes = sum(d.stat().st_size for d in os.scandir(filename) if d.is_file())
            return nbytes
    def du(path):
        """disk usage in human readable format (e.g. '2,1GB')"""
        return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
    d = {}
    for i in directory:
        p = f"{path}/{i}"
        # s = getSize(p)
        s = du(p)
        print(s)
        r = s #* 0.000001
        n = {}
        n[p] = (r)
        d.update(n)
    d = sorted(d.items(), key=lambda x: x[1])
    print(f'+{"-"*11}+```+{"-"*52}+')
    for i in d:
        l = len(str(i[1]))
        l = 10 - l
        dl = 50 - len(i[0])
        # print(len(i[0]))
        print(f'|{" " * l}{i[1]} | = | {i[0]}{" " * dl} |')
        print(f'+{"-"*11}+...+{"-"*52}+')
        #print('\n')


def sort(path,type):
    moved = 0
    p = f"{path}/{type}_files"
    directory = os.listdir(path)
    if not os.path.exists(p):
        os.makedirs(p)
    else:
        print("directory exists continue? (y)")
        if input() == "y":
            print("ok")
        else:
            print("fine")
            exit()
    

    for i in directory:
        #print(i)
        if i.endswith(f".{type}"):
            print(i)
            src_dir = f'{path}/{i}'
            target_dir = f'{p}/{i}'
            if not os.path.exists(target_dir):
                shutil.move(src_dir, target_dir)
                moved +=1
            else:
                for x in range(5):
                    print(f"failed{x}")
                    p = f"{p}/duplicates{x}"
                    print(p)
                    if not os.path.exists(p):
                        os.makedirs(p)
                    target_dir = f'{p}/{i}'
                    if not os.path.exists(target_dir):
                        
                        print(target_dir)
                        shutil.move(src_dir, target_dir)
                        moved +=1
                        break

    
    print(f"moved {moved} files")


if __name__ == "__main__":
    main()