# -*- coding:utf-8 -*-
import requests
import json

# QURL="http://127.0.0.1:7079/v1/jobs"
# AURL="http://127.0.0.1:7079/v1/job"
QURL="http://127.0.0.1:7079/nova/jobs"
AURL="http://127.0.0.1:7079/nova/job"
# AURL="http://223.202.202.38:7079/nova/job"


#查询所有任务 
def query():
    print QURL
    r =requests.get(QURL)
    print r
    body = r.json()
    print type(body)
    print body
    # for m in  body:
    #     for k,v in m.items():
    #         print k,v
#增加或更新任务 
def add_job():
    print AURL
    # body={"id":"","kind":0,"name":"t5","oldGroup":"","group":"nova","user":"root","cmd":"555","pause":False,"parallels":0,"timeout":0,"interval":0,"retry":0,"rules":[{"id":"NEW0.7940123521381119","timer":"0 30 13 * * *","gids":["7ff89786"]}],"fail_notify":False,"log_expiration":0,"to":[]}
    #body={"id":"23070787","name":"t5","group":"nova","cmd":"555","user":"root","rules":[{"id":"20070787","timer":"0 30 13 * * *","gids":["7ff89786"],"nids":null,"exclude_nids":null}],"pause":true,"timeout":0,"parallels":0,"retry":0,"interval":0,"kind":0,"avg_time":0,"fail_notify":false,"to":[],"log_expiration":0,"oldGroup":"nova"}
    #date: sun,mon,tue,wed,thu,fri,sat,*
    # .---------------- minute (0 - 59) 
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ... 
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)  OR
    #sun,mon,tue,wed,thu,fri,sat 
    # |  |  |  |  |
    # *  *  *  *  *  command to be executed
    # minute：代表一小时内的第几分，范围 0-59。
    # hour：代表一天中的第几小时，范围 0-23。
    # mday：代表一个月中的第几天，范围 1-31。
    # month：代表一年中第几个月，范围 1-12。
    # wday：代表星期几，范围 0-7 (0及7都是星期天)。

    body={"id":"", "date":"*", "name":"测试任务", "time":"19:00", "pause":False, 
        "command":"""/root/.pyenv/versions/nova/bin/python test_domain.py '{"data": [{"nameid": [{"strategy": "1,4", "cname": "ccgslb.ccmplus.net,www.tenspy10.novacdn.com.cdn.ccmplus.com.cn", "TTL": "3600", "location": "default"}], "domain": "www.tenspy10.novacdn.com"}, {"nameid": [{"strategy": "1,4", "cname": "ccgslb.ccmplus.net,www.www.tenspy11.
novacdn.com.cdn.ccmplus.com.cn", "TTL": "3600", "location": "default"}], "domain": "www.tenspy11.novacdn.com"}], "username": "admin", "userid": 1}'""","task_group":"nova_api","node_group":"nova_node"}
    r = requests.put(AURL,data=json.dumps(body))
    print r
    print r.text

#删除任务 
def del_job():
    print AURL
    dels=AURL+"/nova"+"-"+"1649e685"
    print dels
    r= requests.delete(dels)
    print r
    print r.text

#暂停或启动任务
def pause_job():
    print AURL
    p_url=AURL+"/nova"+"-"+"587e8acf"
    print p_url
    dic = {"pause":False}
    r= requests.post(p_url,data=json.dumps(dic))
    print r
    print r.text

#立即执行任务 
def execute_job():
    print AURL
    p_url=AURL+"/nova"+"-"+"04e019cc"+"/execute?node=192.168.153.133"
    # p_url="http://127.0.0.1:7079/v1/job/nova-04e019cc/execute?node=192.168.153.133"
    print p_url
    r= requests.put(p_url)
    print r
    print r.text

def main():
    # add_job()
    # del_job()
    # query()
    # pause_job()
    execute_job()

if __name__ == '__main__':
    main()