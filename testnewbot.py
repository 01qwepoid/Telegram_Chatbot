import json
import random
import requests 	
import time 
import urllib   # handles special characters
from testdb import DBHelper
from time import strftime

db = DBHelper()

TOKEN = "456115127:AAG8WH_MtCLfUFQ-OenfA_X6yg3-BhEq5mc"  
URL = "https://api.telegram.org/bot{}/".format(TOKEN)  

DIRECTOR = "Dr. Prakash Gopalan"  
DOSA = "Dr. Maneek Kumar"  
DOAA = "Dr. SS Bhatia"  
HEADCSED = "Dr. Maninder Singh"  




def func(a, b):
  return not set(a).isdisjoint(b)
		
def handle_updates(updates):
	branch = set(['cml1','cml2','cml3','cml4'])
	hostel = set(['A','B','C','D','E','FRC','G','H','I','J','K','L','M','N','PG'])
	time = {'8','9','10','11','12','1','2','3','4'}
	days = {'sun':0,'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6}
	year = set(['2019','2020','2021','2022','2023'])		
	who = set(['who','who\'s'])
	what = set(['what','What\'s','what\'s'])
	botname = set(['Name','name','named'])
	lunch = set(['lunch','Lunch'])
	breakfast = set(['breakfast','Breakfast'])
	dinner = set(['dinner','Dinner?'])
	today = set(['today','tonight'])
	tomorrow = set(['tomorrow'])
	dean = set(['dean','dean?'])
	dosa = set(['dosa','dosa?'])
	doaa = set(['doaa','doaa?'])
	tomorrow = set(['tomorrow','tomorrow?'])
	sem1 = {'mathematics-i','applied chemistry','electronic engineering','mechanics','computer programming-i','energy and environment'}
	sem2 = {'mathematics-ii','applied physics','introduction to pe','electrical engineering','computer programming-ii','engineering design-i'}
	sem3 = {'numerical analysis','engineering materials','engineering design-ii (catapult)','discrete mathematical structure','information management system','energy and environment'}
	sem4 = {'optimization techniques','solids and structures','thermo-fluids','manufacturing processes','data structures and algorithms','ict','engineering design iii (buggy)','employment development skills'}
	sem5 = {'advanced data structures and algorithms','software engineering','computer arch and organization','theory of computation','artificial intelligence','professional practices','elective i'}
	sem6 = {'microprocessor-based systems design','embedded systems design','image processing','elective ii','elective iii','innovation and entrepreneurship','capstone project'}
	cssem = {'semester 1','semester 2','semester 3','semester 4','semester 5','semester 6'}


	greetings = {'hey','hello','hola','hi','hii','hie','heya'}
#	greetask = {'howdy','how are you', 'how\'re you','how\'s you'}
	complaint =9999
	step=9999
	print("In handle updates")

	for update in updates["result"]:
		chat = update["message"]["chat"]["id"]
		exists = list(update["message"].keys())
#		print(exists) ......................debug
#Master Code to block Khanna
#		if chat ==180160591: 
#			break
#Master Code to block Sumit 
#		if chat ==500330866:
#			break

#handles forwarded texts ##################
		if exists[4] == 'forward_from':
			if exists[6] !='text':
				send_message("I'm not sure, what to do with this ! ",chat)
				break

		elif exists[4] != 'text':
			send_message("I'm not sure, what to do with this ! ",chat)
			break


		text = update["message"]["text"]
		text = text.lower()
		print("text is : {}".format(text))
		ctext = []
		ctext.append(text)
		ctext = set(ctext)
		ctextstr = list(ctext)[0]
		print("ctextstr = {}".format(ctextstr))
		print("ctext is : {}".format(ctext))
		name = update["message"]["chat"]["first_name"]
		wordsold = set(text.split())
		words=set(map((lambda x:x.strip('?')),wordsold))
		print("words are : {}".format(words))
		l=list(text)
		feetable = db.get_yearlist()
		print("I am here too")
		print("List is : {}".format(l[0:]))


#			if(db.exists(chat)):
#				send_message("You are already registered. You need help with something else?")
#				continue
			#key  board = build_keyboard(feetable)

		if text =='cancel':
			send_message("Please type /help to check what else you can do.",chat)
			break
#registeration #################
		if text=='/start' :
			send_message("Welcome to Thapar University, {} !. Please enter your roll no.".format(name), chat)
			db.add_user(chat)
			continue
		
		if 'more info' in text:
			print('inside here')
			s = {'1','2','3','4','5','6'}
			sem = list(set(words & s))
			print("sem is {}".format(sem))

			if len(sem)>0:
				sem = list(set(sem))
				sub = db.get_CSsubjects(chat, sem[0])
				sub = set(sub)
				print("sub : {}".format(sub))
				keyboard = build_keyboard(sub)
				send_message("Select a subject",chat, keyboard)
				break





#				keyboard = build_keyboard(sub)
#				send_message("Please select subject: ",chat,keyboard)

		
			# elif len((words & breakfast) | (words & lunch) | (words & dinner))>0:
			# mealtime = list((words & breakfast) | (words  & lunch) | (words & dinner))[0]
			# smday = set(map((lambda x:x[:3]),words)) & days.keys()

		# if text in sem1 | text in sem2 | text in sem3 | text in sem4:
		# 	print("found")

		
		if len((ctext & sem1) | (ctext & sem2) | (ctext & sem3) | (ctext & sem4) | (ctext & sem5) | (ctext & sem6))>0:
			sub = list((ctext & sem1) | (ctext & sem2) | (ctext & sem3) | (ctext & sem4) | (ctext & sem5) | (ctext & sem6))[0]
			sub = sub.upper()
			details = db.get_subjectdetail(sub)
			print("details are : {}".format(details[0]))
			lec = list(set(details[0]))
			tut = list(set(details[1]))
			prac = list(set(details[2]))
			cred = list(set(details[3]))
			tname = db.get_teacher(sub)
			#tname = list(set(tname[0]))
			print(tname)

			send_message("{} :\nL:{}\tT:{}\tP:{}\nCredits:{}\nSubject Teacher :{} ".format(sub,lec,tut,prac,cred,tname[0]),chat)
			print("i am here")
			print(sub)
			break








		if text =='/coursescheme':
			sem = ['semester 1','semester 2','semester 3','semester 4','semester 5','semester 6']
			keyboard = build_keyboard(sem)
			send_message("Select Semester : ",chat, keyboard)
			break
			

		elif len(ctext & cssem)>0:
			sem = list(ctext & cssem)[0]
			sem1 = sem[9:]
			print("sem1 : {}".format(sem1))
			a = db.get_CSsubjects(chat, sem1)
			a = list(set(a))

			send_message("You have : ",chat)
			for sub in a:
				send_message("\n{}".format(sub),chat)
				print("\n{}".format(sub))
			options = ['More info on semester {}'.format(sem1),'Cancel']
#			options = ['More info on Semester {}'.format(sem1),'Cancel']
			print(options)
			keyboard = build_keyboard(options)
			send_message("menu",chat,keyboard)
			break


		elif 'sem1' in text:
			s1 = [db.get_cg(chat, 1)][0]
			s1 = list(set(s1))
			send_message("You cg from sem 1 is : {}".format(s1),chat)
			break
		elif 'sem2' in text:
			s1 = [db.get_cg(chat, 2)][0]
			s1 = list(set(s1))
			send_message("You cg from sem 2 is : {}".format(s1),chat)
			break
		elif 'sem3' in text:
			s1 = [db.get_cg(chat, 3)][0]
			s1 = list(set(s1))
			send_message("You cg from sem 3 is : {}".format(s1),chat)
			break
		elif 'sem4' in text:
			s1 = [db.get_cg(chat, 4)][0]
			s1 = list(set(s1))
			send_message("You cg from sem 4 is : {}".format(s1),chat)
			break

		elif '/cg' in text:
			a = ['Sem1','Sem2','Sem3','Sem4']
			keyboard = build_keyboard(a)
			send_message("Please select the semester : ",chat,keyboard)
			break


# Fee and bill modules start ####################################
		if 'acad fee' in text or 'academic fee' in text:
			af = db.get_acadfee(chat)
			b = af[0]
			send_message("Your academic fee is {}".format(b),chat)
			print(text)
			continue

		elif 'mess fee' in text or 'mess bill' in text:
			af = db.get_messbill(chat)
			b = af[0]
			send_message("Your pending mess bill is {}".format(b),chat)
			break

		elif 'bill' in text or 'fee' in text: 
			f1 = db.get_messbill(chat)
			mb = f1[0]
			f2 = db.get_acadfee(chat)
			af = f2[0]
			send_message("Your academic fee is: {} \nYour peding mess bill is: {}".format(af,mb),chat)
			break

# Fee and bill modules ends ####################################

		elif '/gt' in text:
			sub = "UML501"
			t = db.get_allteachers(sub)
			a = t[0]
			send_message(a,chat)
			break

		elif text.startswith('101') and  len(text)==9:
			db.updatesmtablerollno(chat, text)
			py = ['2018','2019','2020','2021','2022']
			keyboard = build_keyboard(py)
			send_message("Please enter your pass year", chat,keyboard)
			continue
#step2
		elif text in year:
			db.updatesmtablepassyear(chat, text)
			br = ['cml1','cml2','cml3','cml4']
			keyboard = build_keyboard(br)
			send_message("Please enter your branch", chat,keyboard)
			continue	
	
#step3
		elif text.lower() in branch:
			db.updatesmtablebranch(chat, text)
			hstl = ['A','B','C','D','E','FRC','G','H','I','J','K','L','M','N','PG']
			keyboard = build_keyboard(hstl)
			send_message("Please enter your Hostel", chat,keyboard)	
			continue

#step4
		elif text.upper() in hostel:
			db.updatesmtablehostel(chat, text)
			send_message("Thank You ! You are now registered with us !", chat)
			send_message("Please type /help to check what you can do.",chat)

		elif '/help' in text:
			send_message("You can do the following : \n\n\
			1. Check your meal menu \n\
			2. Check your time-table \n\
			3. Check you past semester CGPA. Use '/cg' \n\
			4. Check Course Scheme. Use '/coursescheme'\n\
			5. Check you pending fee",chat)
			 

#step5
		# elif room ==1:
		# 	db.updatesmtableroom(chat, text)
		# 	send_message("Thank You ! You are now registered with us !", chat)	
		# 	room=0
		# 	continue


		#	isunique = db.updatesmtablerollno(chat, text)
			#size =  db.isrollunique(text)
#			for u in size:
#				send_message(u,chat)
#			if(len(size)<1):
#				send_message("Please enter your passing out year", chat)
#				continue
#			send_message("This roll no. is already registered with us. Please check the value entered.",chat)
#			continue	

 		# elif text =='/complaint':
 		# 	complaint =1
 		# 	step=0
 		# 	send_message("Please enter your grievance")

 		# elif complant = 1 and step =0:
 		# 	id = db.takecomplaint(chat, text)
 		# 	send_message("Thank You! Your complaint has been noted. Your id is {}".format(id),chat)
 
		elif text=='/complaint':
			complaint = 1
			step=0
			print(room)
			send_message("Please enter your grievance",chat)
		elif text =='/test':
			print(chat)

#		elif text=='/getbranch':
#			a = list(db.get_branch(chat))
#			print(a[0])
			#send_message(a[0],chat)

		elif complaint ==1 and step ==0:
			id = db.takecomplaint(chat, text)
			complaint =9999
			step = 9999
			send_message("Thank You. Your grievance has been noted. Your id is {}".format(id),chat)




		elif text.startswith("/"):
			continue
	
		elif len((words & breakfast) | (words & lunch) | (words & dinner))>0:
			mealtime = list((words & breakfast) | (words  & lunch) | (words & dinner))[0]
			smday = set(map((lambda x:x[:3]),words)) & days.keys()
			if len(smday)>0:
				dish = db.get_messmenu(chat, days[list(smday)[0]], mealtime.lower())			
				print(days[list(smday)[0]])
				print("I am here")
			elif len(words & tomorrow)>0:
				smday = int(strftime("%w"))+1
				dish = db.get_messmenu(chat,smday , mealtime.lower())
				print("No, I am here")
			else:
				smday = int(strftime("%w"))
				dish = db.get_messmenu(chat,smday , mealtime.lower())
				print("no no I am here")

			send_message(dish[0],chat)
			print(mealtime)
			print(smday)
			print(dish)


		elif func(who,words):
			if func(words,botname):
				send_message("My developer, Shubham Khanna named me :)",chat)	
			
		elif func(what,words):
			if func(words,botname):
				send_message("My name is Alskl bot ! :D",chat)		 	
			elif 'age' in words:
				send_message("I am 18 days old!",chat)
			elif 'class' in words:
				smday = int(strftime("%w"))
				smtime = int(strftime("%H"))
				batch="cml4"
				if 'now' in words:
					br = db.get_timeclass(smday,smtime, batch)
					if len(br)>0:
						a = br[0]
						send_message("You have : {}".format(a),chat)
					else:
						send_message("You don't have any class now!",chat)

				elif len(words & time)>0:

					pday = set(map((lambda x:x[:3]),words)) & days.keys() 

					if len(pday)>0:
						smday = days[list(pday)[0]]

					t = list(words & time)[0]
					t24= int(t)
					if t24 <4:
						t24= 12+t24	
					br = db.get_timeclass(smday,t24, batch)
					if len(br)>0:
						a = br[0]
						send_message("You have : {}".format(a),chat)
					else:
						send_message("You have no class at this time ! ",chat)





			# 	print("a is ")
					
			# 	smday=1
			# 	smtime =11
			# #	print(type(a))
			# 	print(a)
			# #	db.

		elif 'when' in words:
			if 'born' in words:
				send_message("I was conceptualised on November 8, 2017.",chat)
	
		# elif func(greetask,words):
		# 	send_message("I'm good ! :)",chat)

		elif func(greetings, words):
			reply = random.choice(list(greetings))
			send_message(reply,chat)
		else:
			if len(text)>0:
				message = "\nYou're talking gibberish ! >.<"
				send_message(message, chat)
			else:
				continue
			

def build_keyboard(listofit):   
	keyboard = [[item] for item in listofit]
	reply_markup = {"keyboard":keyboard, "one_time_keyboard":True}
	return json.dumps(reply_markup)

def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content

def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js

def get_updates(offset=None):
	url = URL + "getUpdates?timeout=100"
	if offset:
		url+="&offset={}".format(offset)
	js = get_json_from_url(url)
	return js

def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	last_update = num_updates -1
	text = updates["result"][last_update]["message"]["text"]
	chat_id = updates["result"][last_update]["message"]["chat"]["id"]
	return (text,chat_id)

def get_last_update_id(updates):
	update_ids = []
	for update in updates["result"]:
		update_ids.append(int(update["update_id"]))
	return max(update_ids)	


# def send_message(text, chat_id, reply_markup=None):
# 	text = urllib.parse.quote_plus(text)
# 	url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text,chat_id)
# 	if reply_markup:
# 		url+="&reply_markup={}".format(reply_markup)
# 	get_url(url)

def send_message(text, chat_id, reply_markup=None):
	text = urllib.parse.quote_plus(text)
	url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text,chat_id)
	if reply_markup:
		url+="&reply_markup={}".format(reply_markup)
	get_url(url)


def main():
	db.setupall()
	db.add_messmenu()
	db.add_subjecttable()
	db.add_facultytable()
	db.add_timetable()
	db.add_feetable()
	db.add_cgtable()
	db.add_courseschemecs()
	last_update_id = None
	print("started main")
	room=1
	while True:

		print("inside while")
		updates = get_updates(last_update_id)
		if len(updates["result"])>0:
			print("results>0")
			last_update_id = get_last_update_id(updates) + 1
			handle_updates(updates)
			#echo_all(updates)
		time.sleep(0.5)


		# text,chat = get_last_chat_id_and_text(get_updates())
		# if (text,chat) != last_textchat:
		# 	send_message(text,chat)
		# 	last_textchat = (text,chat)

if __name__ == '__main__':
	main()