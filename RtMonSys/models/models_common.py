# * coding:utf-8 *
# Author    : Administrator
# Createtime: 8/14/2018
import os,json,subprocess, shlex

def get_config(key):
    # 加载配置文件
    file_path = os.getcwd() + '/config/config.json'
    fp = open(file_path)
    json_data = json.load(fp)
    return json_data[key]

def exec_command(comm):
    shell_cmd = 'C://Users//Administrator//venv//Scripts//python.exe E://BDP_WEB//BDP_WEB//RtMonSys//models//output.py'
    cmd = shlex.split(shell_cmd)
    print("shell_cmd: " + shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            print('Subprogram output: [{}]'.format(line))
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')




if __name__ == '__main__':
    popen = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE)
    while True:
        print(popen.stdout.readline())