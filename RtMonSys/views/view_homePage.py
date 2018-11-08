# -*-coding:utf-8 -*-
from __future__ import unicode_literals

import time,shlex,subprocess
from django.shortcuts import render
from django.http import HttpResponse
import json,os

from BDP.config import constants
from BDP.tool import GenerateReport
from RtMonSys.models import model_homePage, models_common, test
from RtMonSys.models.models_logger import Logger
from dwebsocket.decorators import accept_websocket, require_websocket
isrunning = True
is_stop = True

def set_pause(request):
    global isrunning
    flag = request.GET.get("isrunning")
    if(flag == 'false'):
        isrunning = False
    if(flag == 'true'):
        isrunning = True
    result = {'state':'success'}
    jsonstr = json.dumps(result)
    return HttpResponse(jsonstr)

def set_stop(request):
    global is_stop
    is_stop = False
    result = {'state': 'success'}
    jsonstr = json.dumps(result)
    return HttpResponse(jsonstr)

def go_homePage(request):
    Logger.write_log("初始化Home Page数据")
    return render(request, 'HomePage.html')

def go_output(request):
    return render(request, 'Output.html')

def get_all_model(request):
    Logger.write_log("获取所有类型model数据")
    result = model_homePage.get_all_models()
    jsonstr = json.dumps(result)
    return HttpResponse(jsonstr)

@accept_websocket
def echo_once(request):
    global isrunning
    global is_stop
    isrunning = True
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'HomePage.html')
    else:
        for message in request.websocket:
            content = bytes.decode(message)
            list = json.loads(content)
            for item in list:
                run_count = item["run_count"]
                print(os.getcwd())
                folderName = item["model"] + '_case'
                path2 = os.path.join(os.getcwd(),'BDP')
                path3 = os.path.join(path2,folderName)
                filePath = str(os.path.join(path3,item["case"] + '.py'))


                # filePath = os.getcwd() + '\\BDP\\BDP'

                for i in range(0,int(run_count)):
                    # filePath = filePath.replace(filePath,"\\",'/')
                    # filePath.replace('\\', '/')
                    # print(filePath)
                    shell_cmd = 'python ' + filePath
                    print(shell_cmd)
                    # cmd = shlex.split(shell_cmd)
                    p = subprocess.Popen(shell_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    request.websocket.send(str.encode('Run Count:' + str(i)))
                    while p.poll() is None:
                        line = p.stdout.readline()
                        line = line.strip()
                        if line:
                            request.websocket.send(str.encode('Output: [{}]'.format(line)))
                    if p.returncode == 0:
                        request.websocket.send(b'Success')
                    else:
                        request.websocket.send(b'Failed')
                    while not isrunning:
                        if not is_stop:
                            break
                        time.sleep(2)
                    if not is_stop:
                        break
            if not is_stop:
                request.websocket.send(b'Finish')
                is_stop = True
                break
            request.websocket.send(b'Finish')

def set_output(request):
    log_dir = constants.log_dir
    result = GenerateReport.exportToResult(log_dir)
    jsonstr = json.dumps(result)
    return HttpResponse(jsonstr)

def showDetail(request):
    path = request.GET.get('path')
    f = open(path)
    line = f.readline()
    lines = []
    while line:
        lines.append(line)
        line = f.readline()
    f.close()
    jsonstr = json.dumps(lines)
    return HttpResponse(jsonstr)




