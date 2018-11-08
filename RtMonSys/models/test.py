import shlex,os
import subprocess

if __name__ == '__main__':
    m = os.path.join('路径', '文件名.txt')
    m.replace('\\', '/')
    print(m)
