# -*- coding: UTF-8 -*-
import os
import sys
from xml.dom.minidom import parse
import xml.dom.minidom
import time

#当前文件的父路径
# father_path=os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
father_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(father_path, 'IR_sender')

def get_ir_code(comman):
    load_path = os.path.join(file_path, 'IR_CODE_DEFINE.xml')
    
    # 使用解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(load_path)
    collection = DOMTree.documentElement
    codes = collection.getElementsByTagName("code")  # 拿到所有的CODE
    
    # 遍历code
    for item in codes:
        s_key = item.getElementsByTagName('key')[0]
        if comman == s_key.childNodes[0].data:  # 寻找发射的编码
            s_value = item.getElementsByTagName('value')[0]
            sendValue = s_value.childNodes[0].data
            return sendValue
    return "No defined"

def get_ir_error(comman):
    load_path = os.path.join(file_path, 'IR_ERROR_MESSAGE.xml')
    r_DOMTree = xml.dom.minidom.parse(load_path)
    r_collection = r_DOMTree.documentElement
    r_codes = r_collection.getElementsByTagName("code")  # 拿到所有的CODE
    # 遍历code
    for item in r_codes:
        r_key = item.getElementsByTagName('key')[0]
        c_key = int(r_key.childNodes[0].data)
        if comman == c_key:  # 寻找发射的编码
            r_value = item.getElementsByTagName('value')[0]
            resultValue = r_value.childNodes[0].data
            return resultValue
    return "No defined"

def get_platform_version():
    # 获取机器是32还是64
    bit = sys.maxsize
    if bool(bit > 2 ** 32) == False:
        return "32"
    else:
        return "64"
 
def send(code):
    ircode = get_ir_code(code)  
    # father_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
    father_path = os.path.abspath(os.path.join(os.getcwd(), "BDP"))
    platformbit = get_platform_version()

    exe_path = os.path.join(father_path, 'tool', 'IRSender' ,platformbit, 'IRSender.exe')
    # 执行
    result = os.system(r'%s "%s"' % (exe_path, ircode))
    return result, get_ir_error(result)

if __name__ == '__main__':
    send("RIGHT")
    time.sleep(3)
    send("RIGHT")
    time.sleep(3)
    send("ENTER")
    time.sleep(3)



