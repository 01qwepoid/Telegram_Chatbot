	
import sqlite3

class DBHelper:
	def __init__(self, dbname="testdb0.sqlite"):
		self.dbname = dbname
		self.conn = sqlite3.connect(dbname)

	def setupall(self):
		tblstmt1 = "CREATE TABLE IF NOT EXISTS studentmaintable (owner TEXT , rollno TEXT, hostel TEXT, pass TEXT, year TEXT, branch TEXT, approved TEXT, room TEXT)"
		tblstmt2 = "CREATE TABLE IF NOT EXISTS messmenutable (hostel TEXT, day integer,  mealtime TEXT, mealmenu TEXT)" 
		tblstmt3 = "CREATE TABLE IF NOT EXISTS feetable (rollno TEXT, acadfee integer, messbill integer)"
#	 	tblstmt3 = ""
		tblstmt4 = "CREATE TABLE IF NOT EXISTS facultytable (facultyname TEXT, subjectcode TEXT DEFAULT 0)"#,FOREIGN KEY(subjectcode) REFERENCES subjecttable(subjectcode) ON DELETE SET DEFAULT)"
		tblstmt5 = "CREATE TABLE IF NOT EXISTS subjecttable (subject TEXT, subjectcode TEXT )"
		#primary key)"
		tblstmt6 = "CREATE TABLE IF NOT EXISTS courseschemeCStable (semester integer, subcode text, subname text, l integer, t integer, p integer, cr decimal(2,2), check (semester in (1,2,3,4,5,6,7,8)))"
		#tblstmt6 = "CREATE TABLE IF NOT EXISTS courseschemetable (dept TEXT, semester integer, subjectcode TEXT, faculty TEXT, credits real, check (semester in (1,2,3,4,5,6,7,8)))"
		tblstmt7 = "CREATE TABLE IF NOT EXISTS cml (batch text,day integer, slot integer,subjectcode text)"
		tblstmt8 = "CREATE TABLE IF NOT EXISTS cgtable (rollno text,sem text, cg decimal(2,2))"

		self.conn.execute(tblstmt1)
		self.conn.execute(tblstmt2)
		self.conn.execute(tblstmt3)
		self.conn.execute(tblstmt4)
		self.conn.execute(tblstmt5)
		self.conn.execute(tblstmt6)
		self.conn.execute(tblstmt7)
		self.conn.execute(tblstmt8)
		self.conn.commit()


	def indexall(self):
		rollidx = "CREATE INDEX IF NOT EXISTS rollNoIndex ON studentmaintable (rollno ASC)"
		hostelidx = "CREATE INDEX IF NOT EXISTS hostelIndex ON messmenutable (hostel ASC)"
		feeidx = "CREATE INDEX IF NOT EXISTS feeIndex ON feetable (rollno ASC)"
		subidx = "CREATE INDEX IF NOT EXISTS subIndex ON facultytable (subject ASC)"
		cschemeidx = "CREATE INDEX IF NOT EXISTS courseSchemeIndex ON courseschemeCStable (semester ASC)"
		self.conn.execute(rollidx)
		self.conn.execute(hostelidx)
		self.conn.execute(feeidx)
		self.conn.execute(subidx)
		self.conn.execute(cschemeidx)
		self.conn.commit()


#1
	def add_user(self, owner):
		stmt = "INSERT INTO studentmaintable (owner , rollno , hostel , pass , year , branch , approved, room) VALUES (?,?,?,?,?,?,?,?)" 
		args = (owner, 'null','null', 0000 , 'null', 'null', 'False','null')
		self.conn.execute(stmt, args)
		self.conn.commit()
#2
	def get_messmenu(self, owner, day, mealtime):
		stmt = "SELECT mealmenu FROM messmenutable WHERE day = (?) AND mealtime = (?)" 
		args = (int(day),mealtime)
		return [x[0] for x in self.conn.execute(stmt, args)]
#3
	def get_otherfaculty(self, subcode):
		stmt = "SELECT facultyname FROM facultytable where subjectcode = (?)"
		args= (subcode)
		return [x[0] for x in self.conn.execute(stmt, args)]

#4	
	def get_branch(self, owner):
		stmt = "SELECT branch from studentmaintable where owner = (?)"
		args= (owner)
		val = [x[0] for x in self.conn.execute(stmt, args)]
		return val

#5
	def add_smtable(self, char_roll, char_hostel, TEXT_passyear, TEXT_branch):
		stmt = "INSERT INTO studentmaintable (owner , rollno , hostel , password , year , branch , approved) VALUES (?, ?, ? ,?, ?, ?, ?)"
		args = (owner, char_roll, char_hostel, 0000 , TEXT_passyear, TEXT_branch, 'False')
		self.conn.execute(stmt, args)
		self.conn.commit()


	
#		return [x[0] for x in self.conn.execute(stmt, args)]


	def get_timtable(self, owner, day, timey):
		stmt1 = "SELECT branch from studentmaintable where owner = (?)"
		args1 = (owner)
		branch = [x[0] for x in self.conn.execute(stmt1, args1)]

		stmt2 = "SELECT subject from timetable where branch = (?) and day = (?) and timey = (?)"
		args2 = (branch[0], day, timey)
		return [x[0] for x in self.conn.execute(stmt2, args2)]


	def updatesmtablepassyear(self, owner, passyear):
		stmt = "UPDATE studentmaintable SET year = (?) WHERE owner = (?)"
		args = (passyear, owner)
		print("Executeed !!")
		self.conn.execute(stmt, args)
		self.conn.commit()

	def updatesmtablebranch(self, owner, branch):
		stmt = "UPDATE studentmaintable SET branch = (?) WHERE owner = (?)"
		args = (branch, owner)
		self.conn.execute(stmt, args)
		self.conn.commit()

	def updatesmtablehostel(self, owner, hostel):
		stmt = "UPDATE studentmaintable SET hostel = (?) WHERE owner = (?)"
		args = (hostel, owner)
		self.conn.execute(stmt, args)
		self.conn.commit()

	def updatesmtablerollno(self, owner, roll):
		stmt = "UPDATE studentmaintable SET rollno = (?) WHERE owner = (?)"
		args = (roll, owner)
		self.conn.execute(stmt, args)
		self.conn.commit()

	def updatesmtableroom(self, owner, room):
		stmt = "UPDATE studentmaintable SET room = (?) WHERE owner = (?)"
		args = (room, owner)
		self.conn.execute(stmt, args)
		self.conn.commit()










	# def add_menutable(self, char_hostel, varchar_day, TEXT_mealtime, TEXT_mealmenu):
	# 	stmt = "INSERT INTO messmenutable (hostel , day, mealtime , mealmenu) VALUES (?, ?, ?, ?)"
	# 	args = (TEXT_hostel, varchar_day, TEXT_mealtime, TEXT_mealmenu)
	# 	self.conn.execute(stmt, args)
	# 	self.conn.commit()

	def get_yearlist(self):
		stmt = "SELECT year FROM studentmaintable"
		return [x[0] for x in self.conn.execute(stmt)] 
	#incomplete--------------
	# def add_feetable(self, int_semester, 	):
	# 	stmt = "INSERT INTO studentmaintable (owner, rollno, hostel, approved) VALUES (?, ?)"
	# 	args = (owner, TEXT_roll, TEXT_hostel, 'No')
	# 	self.conn.execute(stmt, args)
	# 	self.conn.commit()


	def add_facultytable(self, TEXT_facultyname, TEXT_facultysubject):
		stmt = "INSERT INTO facultytable (facultyname, subject) VALUES (?, ?)"
		args = (TEXT_facultyname, TEXT_facultysubject)
		self.conn.execute(stmt, args)
		self.conn.commit()

	def add_courseschemetable(self, char_semester, TEXT_subject):
		stmt = "INSERT INTO facultytable (facultyname, subject) VALUES (?, ?)"
		args = (char_semester, TEXT_subject)
		self.conn.execute(stmt, args)
		self.conn.commit()


	def approve(self, char_roll, yesno):
		stmt = "UPDATE studentmaintable SET approved = (?) WHERE rollno = (?)"
		args = (yesno,char_roll)
	#	arg1 = (yesno)
	#	arg2 = (char_roll)
		self.conn.execute(stmt, args)
	#	self.conn.execute(stmt, arg1,arg2)
		self.conn.commit()


#2






	def isrollunique(self, roll):
		stmt = "SELECT rollno FROM studentmaintable where rollno = (?)"
		args = (roll, )
		return [x[0] for x in self.conn.execute(stmt, args)]


		












	

	def add_subjecttableold(self):
		stmt1 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Software Engineering','UCS503')"
		stmt2 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Data Structures & Algo', 'UCS406')"
		stmt3 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Adv Data Str & Algo','UCS616')"
		stmt4 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Operating Systems','UCS303')"
		stmt5 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Computer Programming I','UTA007')"
		stmt6 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Computer Programming II','UTA009')"
		stmt7 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Machine Learning','UML501')"
		stmt8 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Discrete Mathematical Str','UCS405')"
		stmt9 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Computer Architecture & Org','UCS519')"
		stmt10 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Artificial Intelligence','UCS521')"
		stmt11 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Theory of Computation','UCS701')"
		stmt12 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Image Processing','UCS615')"
		stmt13 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Embedded Systems Design','UCS614')"
		stmt14 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Information Management System','UCS304')"
		stmt15 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Computer Networks','UCS520')"
		stmt16 = "INSERT into subjecttable (subject, subjectcode) VALUES ('Natural Language Processing','UML602')"
		self.conn.execute(stmt1)
		self.conn.execute(stmt2)
		self.conn.execute(stmt3)
		self.conn.execute(stmt4)
		self.conn.execute(stmt5)
		self.conn.execute(stmt6)
		self.conn.execute(stmt7)
		self.conn.execute(stmt8)
		self.conn.execute(stmt9)
		self.conn.execute(stmt10)
		self.conn.execute(stmt11)
		self.conn.execute(stmt12)
		self.conn.execute(stmt13)
		self.conn.execute(stmt14)
		self.conn.execute(stmt15)
		self.conn.execute(stmt16)
		self.conn.commit()

	def get_teacher(self, subject):
		stmt = "select subjectcode from subjecttable where subject = (?)"
		args = (subject,)
		subcode = [x[0] for x in self.conn.execute(stmt, args)]
		print("subcode is {}".format(subcode))

		if len(subcode)>0:
			stmt = "select facultyname from facultytable where subjectcode = (?)"
			args = (subcode[0],)
			print("subcode[0] is {}".format(subcode[0]))
			fac = [x[0] for x in self.conn.execute(stmt, args)]
			if len(fac)>0:
				return fac
			error = "Faculty not defined"
			return error

	def add_facultytable(self):
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Prashant S Rana','UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Shreelekha Pandey','UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Anju Bala','UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Deep Mann','UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Hemant Saxena','UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Prabhleen Kaur','UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Mr Nitin Saxena', 'UCS701')"
		self.conn.execute(stmt)
		self.conn.commit()


	
#		return [x[0] for x in self.conn.execute(stmt, args)]

	def add_subjecttable(self):
		
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('SOFTWARE ENGINEERING','UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('SOFTWARE ENGINEERING LAB','UCS503 lab')"
		self.conn.execute(stmt)
		
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('ADVANCED DATA STRUCTURES AND ALGORITHMS','UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('MACHINE LEARNING','UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('COMPUTER ARCH AND ORGANIZATION','UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('ARTIFICIAL INTELLIGENCE','UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('THEORY OF COMPUTATION','UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('NETWORK SECURITY','UCS522')"
		self.conn.execute(stmt)	
		stmt = "INSERT into subjecttable (subject, subjectcode) VALUES ('OPTIMIZATION TECHNIQUES','UMA031')"
		self.conn.execute(stmt)	
		self.conn.commit()




	def add_facultytableold(self):

		stmt1 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('HS Pannu','UCS405')"
		stmt2 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('HS Pannu','UTA007')"
		stmt3 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('HS Pannu','UTA009')"
		stmt4 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('HS Pannu','UCS303')"
		stmt5 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('HS Pannu','UCS304')"
		stmt6 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Rajanpreet Kour','UCS405')"
		stmt7 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Mr Nitin Saxena','UCS701')"
		stmt8 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr HS Pannu','UTA009')"
		stmt9 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Sukhchandan Randhawa','UCS304')"
		stmt10 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Shivendra Shivani','UCS520')"
		stmt11 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Avleen Kaur','UCS406')"
		stmt12 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Tarunpreet Bhatia','UCS406')"
		stmt13 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Anika','UCS304')"
		stmt14 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('VP Singh','UML602')"
		stmt15 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Prashant S Rana','UML501')"
		stmt16 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Karamjit Kaur','UCS304')"
		stmt17 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Shreelekha Pandey','UCS616')"
		stmt18 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Geeta Kasana','UTA007')"
		stmt19 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Karun Verma','UML602')"
		stmt20 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Anju Bala','UCS519')"
		stmt21 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Rajiv Kumar','UCS616')"
		stmt22 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Singara Singh','UML501')"
		stmt23 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Seema Bawa','UCS520')"
		stmt24 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Seema Bawa','UCS503')"
		stmt25 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Maninder Singh','UCS520')"
		stmt26 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Neeraj Kumar','UTA009')"
		stmt27 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Parteek Bhatia','UML602')"
		stmt28 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Parteek Bhatia','UCS304')"
		stmt29 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Ajay Kumar','UCS305')"
		stmt30 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Rajesh Mehta','UCS616')"
		stmt31 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Ravinder Kumar','UCS616')"
		stmt32 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Rupali Bhardwaj','UCS519')"
		stmt33 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Anjali','UCS519')"
		stmt34 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Prabhleen Juneja','UML501')"
		stmt35 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr AK Loura','UCS701')"
		stmt36 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Vinay Gautam','UCS701')"
		stmt37 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Arzoo','UCS701')"
		stmt38 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Sanmeet Bhatia','UCS503')"
		stmt39 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Seema Bawa','UCS503')"
		stmt40 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Dr Ashima Singh','UCS503')"
		stmt41 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Prabhleen Juneja','UCS503')"
		stmt42 = "INSERT into facultytable (facultyname, subjectcode) VALUES ('Ms Shiwani Garg','UCS503')"
		self.conn.execute(stmt1)
		self.conn.execute(stmt2)
		self.conn.execute(stmt3)
		self.conn.execute(stmt4)
		self.conn.execute(stmt5)
		self.conn.execute(stmt6)
		self.conn.execute(stmt7)
		self.conn.execute(stmt8)
		self.conn.execute(stmt9)
		self.conn.execute(stmt10)
		self.conn.execute(stmt11)
		self.conn.execute(stmt12)
		self.conn.execute(stmt13)
		self.conn.execute(stmt14)
		self.conn.execute(stmt15)
		self.conn.execute(stmt16)
		self.conn.execute(stmt17)
		self.conn.execute(stmt18)
		self.conn.execute(stmt19)
		self.conn.execute(stmt20)
		self.conn.execute(stmt21)
		self.conn.execute(stmt22)
		self.conn.execute(stmt23)
		self.conn.execute(stmt24)
		self.conn.execute(stmt25)
		self.conn.execute(stmt26)
		self.conn.execute(stmt27)
		self.conn.execute(stmt28)
		self.conn.execute(stmt29)
		self.conn.execute(stmt30)
		self.conn.execute(stmt31)
		self.conn.execute(stmt32)
		self.conn.execute(stmt33)
		self.conn.execute(stmt34)
		self.conn.execute(stmt35)
		self.conn.execute(stmt36)
		self.conn.execute(stmt37)
		self.conn.execute(stmt38)
		self.conn.execute(stmt39)
		self.conn.execute(stmt40)
		self.conn.execute(stmt41)
		self.conn.execute(stmt42)
		self.conn.commit()





	def add_messmenu(self):
			stmt1 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',0,'breakfast','Gobi Parantha, Dahi')"
			stmt2 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',0,'lunch','Rajmah Chawal, Dahi Mongra')"
			stmt3 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',0,'dinner','Amritsari Kulha, Chhole, Ice-Cream')"

			stmt4 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',1,'breakfast','Macroni, Aloo Parantha')"
			stmt5 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',1,'lunch','Chhole Bathure, Kulche')"
			stmt6 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',1,'dinner','Shahi Paneer, Mix Veg, Gulab Jamun')"

			stmt7 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',2,'breakfast','Mix Parantha, Sprouts')"
			stmt8 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',2,'lunch','Arhar Dal, Boondi Rayta')"
			stmt9 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',2,'dinner','Paneer Bhurji, Masar Dal')"

			stmt10 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',3,'breakfast','Plain Parantha, Aloo')"	
			stmt11 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',3,'lunch','Mix Dal, Cabbage')"
			stmt12 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',3,'dinner','Mix Dal, Sewayian')"
			
			stmt13 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',4,'breakfast','Cornflakes, Boiled egg')"
			stmt14 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',4,'lunch','Pav Bhaji, Boondi Rayta')"
			stmt15 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',4,'dinner','Munchurian, Fried Rice, Jalebi')"			
			
			stmt16 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',5,'breakfast','Aloo Parantha, Toast')"
			stmt17 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',5,'lunch','Kadi Pakora, Cauliflower, Curd')"
			stmt18 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',5,'dinner','Noodles, Munchurian')"
			
			stmt19 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',6,'breakfast','Aloo Parantha, Dahi')"
			stmt20 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',6,'lunch','Arhar Dal, Mix Veg')"
			stmt21 = "INSERT into messmenutable (hostel, day, mealtime, mealmenu) VALUES ('A',6,'dinner','Malai Kofta, Fried Rice')"
			self.conn.execute(stmt1)
			self.conn.execute(stmt2)
			self.conn.execute(stmt3)
			self.conn.execute(stmt4)
			self.conn.execute(stmt5)
			self.conn.execute(stmt6)
			self.conn.execute(stmt7)
			self.conn.execute(stmt8)
			self.conn.execute(stmt9)
			self.conn.execute(stmt10)
			self.conn.execute(stmt11)
			self.conn.execute(stmt12)
			self.conn.execute(stmt13)
			self.conn.execute(stmt14)
			self.conn.execute(stmt15)
			self.conn.execute(stmt16)
			self.conn.execute(stmt17)
			self.conn.execute(stmt18)
			self.conn.execute(stmt19)
			self.conn.execute(stmt20)
			self.conn.execute(stmt21)
			self.conn.commit()

	def get_class(self,day, slot,batch):
		stmt = "SELECT s.subject, s.subjectcode, f.facultyname  FROM subjecttable s JOIN cml ON s.subjectcode=cml.subjectcode JOIN facultytable f ON s.subjectcode=f.subjectcode AND cml.slot=(?) AND cml.day=(?) AND cml.batch=(?)"
#		s.subjectcode, f.facultyname ,
		args = (slot,day,batch)
		print("inside function")
		print(day)
		print(slot)
		print(batch)
		a = [x[0] for x in self.conn.execute(stmt, args)]
		print(a)


# 	def get_subname(self, subcode):
# 		print("subcode is ")
# 		print(subcode)
# 		stmt989 = "SELECT subject from subjecttable where subjectcode = (?)"
# 		args989 = (subcode,)
# #		stmt = "SELECT subject from subjecttable where subjectcode = {}".format(subcode)
# 		b = [x[0] for x in self.conn.execute(stmt989,args989)]
# #		b = [x[0] for x in self.conn.execute(stmt, args)]
# 		#print(b)
# 		return b


	def get_timeclass(self, day, timeslot, branch ):
			stmt = "SELECT subjectcode from cml where batch = (?) and day = (?) and slot = (?)" 
			args = (branch,day,timeslot)
			a = [x[0] for x in self.conn.execute(stmt, args)]
			if len(a)>0:
#lets try			
				stmt = "SELECT subject from subjecttable where subjectcode = (?)"
				args  = (a[0],)
				b = [x[0] for x in self.conn.execute(stmt, args)]
				return b
			return a

	def add_feetable(self):
		stmt = "INSERT INTO feetable (rollno, acadfee, messbill) VALUES ('101510081',168400, 3200)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO feetable (rollno, acadfee, messbill) VALUES ('101510082',158400, 3500)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO feetable (rollno, acadfee, messbill) VALUES ('101510070',148400, 3800)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO feetable (rollno, acadfee, messbill) VALUES ('101510089',138400, 4100)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO feetable (rollno, acadfee, messbill) VALUES ('101510088',128400, 4300)"
		self.conn.execute(stmt)
		self.conn.commit()

	def get_acadfee(self, owner):
		stmt1 = "SELECT rollno from studentmaintable where owner = (?)"
		args1 = (owner, )
		roll = [x[0] for x in self.conn.execute(stmt1, args1)]
		print(owner)
		print(roll)


		if len(roll)>0:
			stmt = "SELECT acadfee from feetable where rollno = (?)"
			args = (roll[0], )
			return [x[0] for x in self.conn.execute(stmt, args)]
		error = "Your data not found in the database."
		return error


	def get_messbill(self, owner):
		
		stmt1 = "SELECT rollno from studentmaintable where owner = (?)"
		args1 = (owner, )
		roll = [x[0] for x in self.conn.execute(stmt1, args1)]
		print(owner)
		print(roll)


		if len(roll)>0:
			stmt = "SELECT messbill from feetable where rollno = (?)"
			args = (roll[0], )
			return [x[0] for x in self.conn.execute(stmt, args)]
		error = "Your data not found in the database."
		return error






		stmt = "SELECT messbill from feetable where owner = (?)"
		args = (owner, )
		return [x[0] for x in self.conn.execute(stmt, args)]


	def get_allfee(self, owner):
		#af = 	 
		stmt = "SELECT acadfee,  from feetable where owner = (?)"
		args = (owner, )
		return [x[0] for x in self.conn.execute(stmt, args)]


	def add_cgtable(self):
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510081','1',9.79)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510081','2',9.19)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510081','3',8.72)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510081','4',9.59)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510070','1',8.9)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510070','2',9.0)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510070','3',10)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cgtable (rollno, sem, cg) VALUES ('101510070','4',8.6)"
		self.conn.execute(stmt)
		self.conn.commit()
	
	def get_cg(self, owner, semes):
		stmt1 = "SELECT rollno from studentmaintable where owner = (?)"
		args1 = (owner, )
		roll = [x[0] for x in self.conn.execute(stmt1, args1)]
		
		if len(roll)>0:
			stmt = "SELECT cg from cgtable where rollno = (?) and sem = (?)"
			args = (roll[0],semes)
			return [x[0] for x in self.conn.execute(stmt, args)]
		error = "Your data not found in the database."
		return error

	def get_CSsubjects(self, owner, sem):
		stmt1 = "SELECT branch from studentmaintable where owner = (?)"
		args1 = (owner, )
		br = [x[0] for x in self.conn.execute(stmt1, args1)][:3]
	
		if len(br)>0:
			stmt = "SELECT subname from courseschemeCStable where semester = (?)"
			args = (sem,)
			return [x[0] for x in self.conn.execute(stmt, args)]
		error = "Your data not found in the database."
		return error

	def get_subjectdetail(self, subject):
		stmt1 = "SELECT l from courseschemeCStable where subname = (?)"
		print('subname is {}'.format(subject))
		args1 = (subject, )
		l = [x[0] for x in self.conn.execute(stmt1, args1)]
		print('l is {}'.format(l))
	
		if len(l)>0:
			stmt1 = "SELECT t from courseschemeCStable where subname = (?)"
			args1 = (subject, )
			t = [x[0] for x in self.conn.execute(stmt1, args1)]
			print('t is {}'.format(t))

			stmt1 = "SELECT p from courseschemeCStable where subname = (?)"
			args1 = (subject, )
			p = [x[0] for x in self.conn.execute(stmt1, args1)]

			stmt1 = "SELECT cr from courseschemeCStable where subname = (?)"
			args1 = (subject, )
			cr = [x[0] for x in self.conn.execute(stmt1, args1)]

			det=[]
			det.append(l)
			det.append(t)
			det.append(p)
			det.append(cr)
			return det

		error = "Your data not found in the database."
		return error

	def add_courseschemecs(self):
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UMA003','MATHEMATICS-I',	3,	1,	0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UCB008','APPLIED CHEMISTRY'	,3,	1,	2,	4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UEC001','ELECTRONIC ENGINEERING',	3,	1,	2,	4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UES009','MECHANICS',	2,	1,	2,	2.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UTA007','COMPUTER PROGRAMMING-I',	3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (1,'UEN002','ENERGY AND ENVIRONMENT',	3	,0,	0,	3)"
		self.conn.execute(stmt)
		
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UMA004','MATHEMATICS-II',	3,1,	0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UPH004','APPLIED PHYSICS',	3	,1	,2	,4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UHU003','INTRODUCTION TO PE',2,	0,	2,	3)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UEE001','ELECTRICAL ENGINEERING',	3	,1	,2	,4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UTA009','COMPUTER PROGRAMMING-II',	3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (2,'UTA008','ENGINEERING DESIGN-I',2	,4	,0	,4)"
		self.conn.execute(stmt)
			
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UMA007','NUMERICAL ANALYSIS',3,	1,	2,	4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UES012','ENGINEERING MATERIALS',3	,1	,2	,4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UTA010','ENGINEERING DESIGN-II (CATAPULT)',	1,	0,	2,	5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UCS405','DISCRETE MATHEMATICAL STRUCTURE',	3,	1,	0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UCS304','INFORMATION MANAGEMENT SYSTEM',	3,	0,	4,	6)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (3,'UEN002','ENERGY AND ENVIRONMENT',	3	,0	,0	,3)"
		self.conn.execute(stmt)


		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UMA031','OPTIMIZATION TECHNIQUES',	3,	1	,0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UES010','SOLIDS AND STRUCTURES',	3	,1,	2	,4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UES011','THERMO-FLUIDS',	3,	1,	2,	4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UTA002','MANUFACTURING PROCESSES',	2,	0,	3,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UCS406','DATA STRUCTURES AND ALGORITHMS',	3,	0,	2,	6)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UCS407','INTRODUCTION',	2	,0	,0	,2)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'UTA011','ENGINEERING DESIGN III (BUGGY)',	1,	0	,4,	6)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (4,'EDS','EMPLOYMENT DEVELOPMENT SKILLS)',	1,	0,	0,	0)"
		self.conn.execute(stmt)

		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'UCS616','ADVANCED DATA STRUCTURES AND ALGORITHMS',	3,	0	,2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'UCS503','SOFTWARE ENGINEERING',	3	,0	,2	,4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'UCS519','COMPUTER ARCH AND ORGANIZATION',	3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'UCS701','THEORY OF COMPUTATION',3	,1	,0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'UCS521','ARTIFICIAL INTELLIGENCE',	3,	1,	0,	3.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'PP','PROFESSIONAL PRACTICES',	0,	1,	2,	1.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (5,'EL1','ELECTIVE I',	3,	0,	2	,4)"
		self.conn.execute(stmt)

		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'UCS617','MICROPROCESSOR-BASED SYSTEMS DESIGN',	3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'UCS614','EMBEDDED SYSTEMS DESIGN'	,3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'UCS615','IMAGE PROCESSING'	,3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'EL2','ELECTIVE II'	,3	,0	,2	,4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'EL3','ELECTIVE III',	3,	0,	2,	4)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'UTA012','INNOVATION AND ENTREPRENEURSHIP',	1,	0,	2	,4.5)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO courseschemeCStable (semester, subcode, subname, l, t, p, cr) VALUES (6,'UCS794','CAPSTONE PROJECT',	0	,0	,2	,0)"
		self.conn.execute(stmt)
		self.conn.commit()





	






	def add_timetable(self):
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,8,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,9,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,8,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,9,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,8,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,9,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,8,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,9,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,10,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,10,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES  ('cml3',1,10,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,10,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,11,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,11,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,11,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,11,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,15,'UML501 ')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,15,'UML501 ')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,15,'UML501 ')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,15,'UML501 ')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',1,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',1,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',1,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',1,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,8,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,9,'UCS701 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,9,'UCS701 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,9,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,9,'UCS521 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,10,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,10,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,10,'UCS701 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,10,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,11,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,11,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,11,'UCS701 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,11,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,12,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,12,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,12,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,12,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,13,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,13,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,13,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,13,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,15,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,15,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,15,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,15,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',2,16,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',2,16,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',2,16,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',2,16,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,9,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,9,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,9,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,9,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,10,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,10,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,10,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,10,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,11,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,11,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,11,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,11,'UCS616 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,12,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,12,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,12,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,12,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,14,'UCS503')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',3,16,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',3,16,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',3,16,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',3,16,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,8,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,8,'break')"
		self.conn.execute(stmt)
		stmt= "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,9,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,9,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,9,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,9,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,10,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,10,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,10,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,10,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,11,'UCS503 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,11,'UML501 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,11,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,11,'UCS519 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,14,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,14,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,14,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,14,'UCS701')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,15,'UCS521')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',4,16,'UCS521 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',4,16,NULL)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',4,16,NULL)"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',4,16,'UCS701 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,8,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,8,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,8,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,8,'UCS519')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,9,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,9,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,9,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,9,'UCS616')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,10,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,10,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,10,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,10,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,11,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,11,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,11,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,11,'UCS523 lab')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,12,'UCS522')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,13,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,14,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,14,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,14,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,14,'UML501')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,15,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,15,'UCS521 tut')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,15,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,15,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml1',5,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml2',5,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml3',5,16,'break')"
		self.conn.execute(stmt)
		stmt = "INSERT INTO cml (batch ,day , slot ,subjectcode) VALUES ('cml4',5,16,'break')"
		self.conn.execute(stmt)
		self.conn.commit()