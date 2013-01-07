import pymssql


connSQL = pymssql.connect(host='localdb-office.cyvpw3imwgyw.sa-east-1.rds.amazonaws.com',user='usr_dbowner',password='caio0123',database='baselog')

cursor = connSQL.cursor()
query2 = 'select path from [baselog].[dbo].[baselog] where trackuserid=\'{user}\' and convert(date,createat) = \'{data}\' group by path'
cursor.execute('select queryinfo,convert(date,createat),couponid from [baselog].[dbo].[couponclickdetail]')
cursorCoupon = connSQL.cursor()
queryCoupon = 'select latitude,longitude from [baselog].[dbo].[coupon] where couponid = \'{basecouponid}\''
distances = []
cursor2 = connSQL.cursor()
rows = cursor.fetchall()
for row in rows:
	a = row[0].split('=')[2]
	d = row[1]
	cursor2.execute(query2.format(user=a,data=d))
	row2 = cursor2.fetchone()
	rows2 = cursor2.fetchall()
	cursorCoupon.execute(queryCoupon.format(basecouponid = row[2]))
	latlog = cursorCoupon.fetchall()

	for row2 in rows2:
		if len(row2[0].split('/'))>2:
			try:
				cursorMongo = pois.find({u'_id':row2[0].split('/')[5]})
				for linha in cursorMongo:
					print linha[u'coords']
					print latlog
					distances.append(haversine(linha[u'coords'][u'lon'],linha[u'coords'][u'lat'],latlog[0][1],latlog[0][0])*1000)
					print "----"
			except:
					pass
		
	


cursor.execute('select queryinfo from [baselog].[dbo].[couponclickdetail]')
row = cursor.fetchone()
while row:
	a = row[0].split('=')[2]
	cursor2.execute(query2.format(user=a))
	row2 = cursor2.fetchone()
	print a
	row = cursor.fetchone()