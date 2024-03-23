import Serialize
import Deserialize
msg = {
    'msgId':100001,
    'IncreaseNum':0,
    'accountId':12349,
    'sessionId':'7bc212eaa0bb3fd4f0b206bdff950a57',
    'targetUid':1012361,
    'logicalId':259,
    'clientIp':'192.168.8.22',
    'lanuage':'',
    'unsupported':'unsupported',
    'b':0,
    'cn':'cn',
    'appversion':'6874',
    'encryption':0,}


def zuzhuangshuju():
    s = Serialize.Assemble()
    msgId = s.PutInt(msg['msgId'])
    IncreaseNum = s.PutBytes(msg['IncreaseNum'])
    accountId = s.PutLong(msg['accountId'])
    sessionId = s.PutString(msg['sessionId'])
    targetUid = s.PutLong(msg['targetUid'])
    logicalId = s.PutInt(msg['logicalId'])
    clientIp = s.PutString(msg['clientIp'])
    lanuage = s.PutString(msg['lanuage'])
    unsupported = s.PutString(msg['unsupported'])
    b = s.PutInt(msg['b'])
    cn = s.PutString(msg['cn'])
    appversion = s.PutString(msg['appversion'])
    data = s.Result()
    return data
z = zuzhuangshuju()


d = Deserialize.Analysis(z)
msgId = d.GetInt()
print(f'msgId:{msgId}')
IncreaseNum = d.GetBytes()
print(f'IncreaseNum:{IncreaseNum}')
accountId = d.GetLong()
print(f'accountId:{accountId}')
sessionId = d.GetString()
print(f'sessionId:{sessionId}')
targetUid = d.GetLong()
print(f'targetUid:{targetUid}')
logicalId = d.GetInt()
print(f'logicalId:{logicalId}')
clientIp = d.GetString()
print(f'clientIp:{clientIp}')
lanuage = d.GetString()
print(f'lanuage:{lanuage}')
unsupported = d.GetString()
print(f'unsupported:{unsupported}')
b = d.GetInt()
print(f'b:{b}')
cn = d.GetString()
print(f'cn:{cn}')
appversion = d.GetString()
print(f'appversion:{appversion}')










