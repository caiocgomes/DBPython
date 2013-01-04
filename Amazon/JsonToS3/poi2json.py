from boto.s3.connection import S3Connection
from boto.s3.key import Key
import pymongo
import json
import gzip


akey = 'AKIAJNKUEYCQAAUVKK2A'
skey = 'ISWP9VQLP5s7tVA9QlB0NQElQHu1s3oYGPN6A4CA'

conn = S3Connection(akey,skey)
bucket = conn.get_bucket('lbs-pois')
k = Key(bucket)
connMongo = pymongo.Connection('192.168.3.1')

db = connMongo.apontador
data = db.pois.find_one()
string = 'poi/{lbsid}/basicprofile.json.gz'
f = open('foo.json','w')


k.key =string.format(lbsid = data[u'_id'])
zdata = json.dumps(data,sort_keys=True,indent=4, separators=(',', ': '))


f.write(zdata)
k.set_contents_from_file(zdata)
k.make_public()