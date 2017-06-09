#!/usr/bin/python
#encoding: utf-8
'''
Created on 2016年5月30日

@author: Ljj
'''
import sys
def Add_inter(prefix,inter,get_pr,post_pr):#(前缀,接口名,get参数.post参数)
    t=''
    a=('*** Keywords ***'+'\n')
    a=a+(prefix+'_'+inter+'\n')+'    [Arguments]    '
    #print prefix+'_'+inter
    #sys.stdout.write('    [Arguments]    ')
    if get_pr!='NULL':
        t=''
        for jj in range(0,len(get_pr.split(','))):
            t=t+'${'+get_pr.split(',')[jj]+'}'+'    '
    a=a+t
    t='' 
    for InterNum in range(0,len(post_pr.split(','))):
        t=t+('${'+post_pr.split(',')[InterNum]+'}'+'    ')
    a=a+t+'\n'+'    ${time}    timenow\n'+('    ${'+prefix+'_'+inter+'_SignData}    Create Dictionary    agent=android    app=app_broker    ')
    t='    '
    for InterNum in range(0,len(post_pr.split(','))):
        t=t+(post_pr.split(',')[InterNum]+'=${'+post_pr.split(',')[InterNum]+'}'+'    ')
    a=a+t+'\n'+('    '+'${'+prefix+'_'+inter+'_sign}    sign    /'+prefix+'/'+inter+'    ${'+prefix+'_'+inter+'_SignData}    ${time}    app_broker\n') \
    +('    ${'+prefix+'_'+inter+'_Data}    Create Dictionary    agent=android    app=app_broker    ')
    t='    '
    for InterNum in range(0,len(post_pr.split(','))):
        t=t+(post_pr.split(',')[InterNum]+'=${'+post_pr.split(',')[InterNum]+'}'+'    ')
    a=a+t+'\n' \
    +('    '+'Comment'+'    '+'Create Session    sqapi    @{sqapi_API}[1]    ${xgjj_headers}')+'\n' \
    +('    ${'+prefix+'_'+inter+'_Reponse}    Post Request    销冠助手    /'+prefix+'/'+inter+'?sign=${'+prefix+'_'+inter+'_sign}')
    if get_pr!='NULL':
        t=''
        sys.stdout.write('')
        for InterNum in range(0,len(get_pr.split(','))):
            t=t+(get_pr.split(',')[InterNum]+'=${'+get_pr.split(',')[InterNum]+'}'+'')
        a=a+t
    a=a+('    ${'+prefix+'_'+inter+'_Data}    ${xgjj_headers}\n')\
    +'    [Return]    ${'+prefix+'_'+inter+'_Reponse}'
    #写入文件
    f = file('E:\\RF\\xgzs_new\\xgzs_new\\NewInter.txt', 'a+')
    f.write("\r\n")
    f.write(a)
    f.close
    return a



