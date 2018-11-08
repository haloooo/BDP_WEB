# * coding:utf-8 *
# Author    : Administrator
# Createtime: 8/17/2018
import os
from xml.dom.minidom import parse
import xml.dom.minidom

def exportToResult(xmlPath):
    result = []
    # xmlPath = r'D:\test\evidence\log\TestScript'
    xmlList = os.listdir(xmlPath)
    for i in range(0,len(xmlList)):
        path = os.path.join(xmlPath,xmlList[i])
        print(path)
        DOMTree = xml.dom.minidom.parse(path)
        collection = DOMTree.documentElement
        errors = collection.getAttribute("errors")
        name = collection.getAttribute("name")
        result.append({'name':name,'error':errors,'path':path})
    return result
if __name__ == '__main__':
    xmlPath = r'D:\test\evidence\log\TestScript'
    exportToResult(xmlPath)