'''
Created on 12 May 2015

@author: DLH
'''
import os,string,csv,datetime,smtplib,string
from xml.etree.ElementTree import ElementTree
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage 

from BDP.config import  constants
dailyresult=[]
allresult=[]
dailyfailcaselist=[]
dailyblockcaselist=[]
allfailcaselist=[]
allblockcaselist=[]
def parResult(sourcepath,cscfilepath):
    if not os.path.isdir(sourcepath):
        print("ERROR dir")
        return
    firmware=constants.devicefirmware
    csvfile = open(cscfilepath, 'wb')
    writer = csv.writer(csvfile)  
    data=[("CaseName", "Status","Fail_message","Block_message","Firmware")]    
    writer.writerows(data)
    for xmlfile in os.listdir(sourcepath):
        sourcefile=os.path.join(sourcepath,xmlfile)
        if str(xmlfile).find("xml")!=-1:
            fail_message=''
            block_message='' 
            status=''
            result=ElementTree(file=sourcefile).getroot()
            testsuitname='TEST-'+result.get('name')
            failures=string.atoi(result.get('failures'))
            errors=string.atoi(result.get('errors'))
            if errors!=0:
                testcase=result.findall('testcase')
                for eachcase in testcase:
                    if eachcase.find('error')!=None:
                        error_message= eachcase[0].get("message") 
                        status="Block"  
                        block_message=error_message            
            elif failures!=0:
                status="Fail"
                testcase=result.findall('testcase')
                for eachcase in testcase:
                    if eachcase.find('failure')!=None:
                        fail_message= eachcase[0].get("message")
                        if  fail_message in constants.errorlist:
                            status="Fail"   
            else :
                status="OK"
            data=[(testsuitname, status,fail_message,block_message,firmware)]    
            writer.writerows(data)
    csvfile.close()  

def makeDailyJenkinsXml(cscfilepath,dailyjenkinsxml):
#    result=[success,failed,blocked]
    result=[0,0,0]
    csvfile = open(cscfilepath, 'r')
    reader = csv.reader(csvfile,delimiter=',',quotechar='|')
    today=datetime.datetime.now()
    currentday="%d%02d%02d"%(today.year,today.month,today.day)
    for row in reader:
        if len(row)==0:
                break
        if str(row[0]).find(currentday)>0:
            if row[1]=="OK":
                result[0]=result[0]+1
            elif row[1]=="Fail":
                result[1]=result[1]+1 
                dailyfailcaselist.append((row[0],row[2]))   
            elif row[1]=="Block":
                result[2]=result[2]+1   
                dailyblockcaselist.append((row[0],row[3]))                   
    csvfile.close()
    tree = ElementTree(file=dailyjenkinsxml)  
    projectname=tree.getroot()
    for i in range(0,len(projectname[0])):
        projectname[0][i].set("num",str(result[i]))
    tree.write(dailyjenkinsxml)
    global dailyresult
    dailyresult=result
     
def makeAllJenkinsXml(cscfilepath,alljenkinsxml):
#    result=[success,failed,blocked]
    result=[0,0,0]
    csvfile = open(cscfilepath, 'r')
    reader = csv.reader(csvfile,delimiter=',',quotechar='|')
    for row in reader:
        if len(row)==0:
                break
        if row[1]=="OK":
            result[0]=result[0]+1
        elif row[1]=="Fail":
            allfailcaselist.append((row[0],row[2]))   
            result[1]=result[1]+1 
        elif row[1]=="Block":
            result[2]=result[2]+1
            allblockcaselist.append((row[0],row[3]))                            
    csvfile.close()
    tree = ElementTree(file=alljenkinsxml)  
    projectname=tree.getroot()
    for i in range(0,len(projectname[0])):
        projectname[0][i].set("num",str(result[i]))
    tree.write(alljenkinsxml) 
    global allresult
    allresult=result  
    
def makeHtml(isdaily,modelhtml,resulthtml): 
    try:
        output=open(modelhtml,"r", encoding='UTF-8')
        modelstr=output.read()
        if isdaily==True:
            result=dailyresult
            failcaselist=dailyfailcaselist
            blockcaselist=dailyblockcaselist
            chartsrc="http://%s:8088/xml?datasource=dailyResult&config=dailycolumn"%constants.serverIP
        else:
            result=allresult
            failcaselist=allfailcaselist
            blockcaselist=allblockcaselist
            chartsrc="http://%s:8088/xml?datasource=allResult&config=allcolumn"%constants.serverIP
        total=0
        t = datetime.datetime.now()
        timestr="%d%02d%02d" % (t.year, t.month, t.day)
        modelstr=modelstr.replace("bdptime", timestr)
        for num in result:
            total=num+total 
        totalstr="%d(%d*14)"%(total,total/14)
        modelstr=modelstr.replace("bdptotal",totalstr)
        successstr="%d"%result[0]
        failedstr="%d"%result[1]
        blockedstr="%d"%result[2]
        modelstr=modelstr.replace("bdpsuccess", successstr)
        modelstr=modelstr.replace("bdpfailed", failedstr)
        modelstr=modelstr.replace("bdpblocked", blockedstr)
        modelstr=modelstr.replace("bdpfirmware", constants.devicefirmware) 
        modelstr=modelstr.replace("bdpnummode", "%d(%s)"%(len(constants.deviceIplist),constants.deviceMode))
        modelstr=modelstr.replace("Chartsrc", chartsrc) 
        
        failresultstr=''
        failedmodelstr='''<tr><td>failcasename</td><td>failcasemessage</td><td>case_log:<a href="caselogpath">caselogpath</a><br>movie:<a href="moviepath">moviepath</a></td></tr>'''
        for index in range(len(failcaselist)):
            tempstr=failedmodelstr
            casename=failcaselist[index][0].split('-2')
            tempstr=tempstr.replace("failcasename", casename[0])
            tempstr=tempstr.replace("failcasemessage", failcaselist[index][1])
            caselogpath=r'http://%s:8080/job/BDP_RunCase/ws/evidence/log/TestScript/%s.xml'%(constants.serverIP,failcaselist[index][0])
            tempstr=tempstr.replace("caselogpath", caselogpath)
            moviepath=r'http://%s:8080/job/BDP_RunCase/ws/evidence/Video/%s.flv'%(constants.serverIP,failcaselist[index][0])
            tempstr=tempstr.replace("moviepath", moviepath) 
            if index%2!=0:
                tempstr=tempstr.replace("<tr>","<tr style=\"background:#c6ffff\">")
            failresultstr=failresultstr+tempstr
        modelstr=modelstr.replace("faillist", failresultstr)  
        
        blockresultstr=''
        for index in range(len(blockcaselist)):
            blockdmodelstr='''<tr><td>blockcasename</td><td>blockcasemessage</td><td>case_log:<a href="caselogpath">caselogpath</a><br>movie:<a href="moviepath">moviepath</a></td></tr>'''
            tempstr=blockdmodelstr
            casename=blockcaselist[index][0].split('-2')
            tempstr=tempstr.replace("blockcasename", casename[0])
            tempstr=tempstr.replace("blockcasemessage", blockcaselist[index][1])
            caselogpath=r'http://%s:8080/job/BDP_RunCase/ws/evidence/log/TestScript/%s.xml'%(constants.serverIP,blockcaselist[index][0])
            tempstr=tempstr.replace("caselogpath", caselogpath)
            moviepath=r'http://%s:8080/job/BDP_RunCase/ws/evidence/Video/%s.flv'%(constants.serverIP,blockcaselist[index][0])
            tempstr=tempstr.replace("moviepath", moviepath)
            if index%2!=0:
                tempstr=tempstr.replace("<tr>","<tr style=\"background:#ffb6c1\">") 
            blockresultstr=blockresultstr+tempstr
        modelstr=modelstr.replace("blockllist", blockresultstr)   
        output.close()
    except Exception as e:
        print(e)
        pass
    try:
        output=open(resulthtml,"w", encoding='UTF-8')
        output.write(modelstr)
        output.close()
    except Exception as e:
        print(e)
        pass
         
# def sendMail(subject, content, attach1,attach2,sendEmailFrom=None, sendEmailTo=None, smtpInfo = None):
#
#     emailFrom = constants.mailfrom
#     emailTo = constants.mailtolist
#     emailCC = constants.mailcclist
#     smtpHostandPort =  constants.smtpHostandPort
#     smtpLoginName =  constants.smtpLoginName
#     smtpLoginPwd = constants.smtpLoginPwd
#     msg = MIMEMultipart()
#     if smtpInfo != None:
#         global smtpHostandPort
#         smtpHostandPort = smtpInfo[0]
#         global smtpLoginName
#         smtpLoginName =  smtpInfo[1]
#         global smtpLoginPwd
#         smtpLoginPwd = smtpInfo[2]
#     if sendEmailFrom != None:
#         msg['From'] = sendEmailFrom
#     else:
#         msg['From'] = emailFrom
#     if sendEmailTo != None:
#         msg['To'] = sendEmailTo
#     else:
#         msg['To'] = emailTo
#         msg['CC'] = emailCC
#     msg['Subject'] = subject
#     msgcontent = content
#
#     txt = MIMEText(msgcontent,_subtype='html', _charset='utf-8')
#     msg.attach(txt)
#
#     att1 = MIMEText(open(attach1, 'rb').read(), 'base64', 'utf-8')
#     att1["Content-Type"] = 'application/octet-stream'
#     att1["Content-Disposition"] = 'attachment; filename=dailyreport.html'
#     msg.attach(att1)
#
#     att2 = MIMEText(open(attach2, 'rb').read(), 'base64', 'utf-8')
#     att2["Content-Type"] = 'application/octet-stream'
#     att2["Content-Disposition"] = 'attachment; filename=histroyreport.html'
#     msg.attach(att2)
#
#
#
#
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpHostandPort)
#     smtp.login(smtpLoginName, smtpLoginPwd)
#     emailList = str(msg['To']).split(";")
#     smtp.sendmail(msg['From'], emailList , msg.as_string())
#     smtp.quit()
#
def timestamp():
    t = datetime.datetime.now()
    return "%d_%02d_%02d" % (t.year, t.month, t.day)   

if __name__=="__main__":
    workpath=constants.dirname
    cscfilepath=os.path.join(workpath,'result.csv')
    parResult(constants.script_log,cscfilepath)
    makeDailyJenkinsXml(cscfilepath,constants.dailyjenkinsxml)
    makeAllJenkinsXml(cscfilepath,constants.alljenkinsxml)
    subject = "[BDP][Test Report][%s]"%(timestamp())
    templatepath=os.path.join(constants.dirname,"template.html")
    dailyresultpath=os.path.join(constants.dirname,"dailyresult.html")
    allresultpath=os.path.join(constants.dirname,"allresult.html")
    makeHtml(True,templatepath,dailyresultpath)
    makeHtml(False,templatepath,allresultpath)
    if os.path.isfile(allresultpath):
        output=open(allresultpath,'r', encoding='UTF-8')
        mailContent=output.read()
        output.close()
        # sendMail(subject, mailContent,dailyresultpath,allresultpath)