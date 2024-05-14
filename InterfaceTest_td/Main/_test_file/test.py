# 解析 XML
import json
import xmltodict
import time
import _thread

def xml_to_json(xmlstr):
    xmlparse = xmltodict.parse(xmlstr)
    print(xmlparse)
    jsonstr = json.dumps(xmlparse, indent=1)
    data = json.loads(jsonstr)
    print(data)
    return data


xml = '''<message name="CG_GetPlayerBag" comment="请求-玩家-背包数据" authorization="true" queueName="MsgAsyncQueue" msgId="101101" resMsgId="101102">
		<field type="List" value="Integer" name="itemTypes" comment="要请求的背包中的物品类型信息，如果为空，则表示获取全部背包内容"/>
	</message>'''



def print_time(thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print (f'线程名称{thread} 当前时间:{time.ctime()}')

try:
   _thread.start_new_thread( print_time, ('T---1,',1,) )
   _thread.start_new_thread( print_time, ('T---2', 3,) )
except:
   print ("Error: 无法启动线程")

while 1:
   pass
