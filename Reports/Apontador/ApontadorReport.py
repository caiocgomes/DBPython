import Dev.DB.Oracle

class GenerateReport(object):
	def __init__(self):
		self.db = Dev.DB.Oracle.oracle()
	
	def QueryLastMonth(self,time,rownum):
		query = 'select * from (select lbs_id,sum(visit) as visits,sum(phone) from CONTABILIZAR.tbl_mongo_sumarizado where data>\'{data}\' group by lbs_id order by visits desc) where rownum <= {rownum} order by visits desc'
		cursor = db.query(query.format('data'=data,'rownum'=rownum)
		dados = cursor.fetchall()
		for linha in dados:
			
			

	def QueryYearPlusOne(self,time):
	
