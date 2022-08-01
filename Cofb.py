print ("""\033[1;39m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;32m

    _                      ____            
   / \   _ __   __ _ ___  |  _ \ _ __ ___  
  / _ \ | '_ \ / _` / __| | |_) | '__/ _ \ 
 / ___ \| | | | (_| \__ \ |  __/| | | (_) |
/_/   \_\_| |_|\__,_|___/ |_|   |_|  \___/ 


\033[1;39m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                           
""")
import requests,random,os
Enter = input('''\033[0;39m[\033[0;34m1\033[0;39m] \033[0;32mCreate Accounts 
\033[0;39m[\033[0;34m2\033[0;39m] \033[0;32mComplete Tasks
\033[0;39m[\033[0;34m3\033[0;39m] \033[0;32mExtract ID

\033[0;39m* \033[0;32mEnter The Selection Number \033[0;34m:\033[0;39m ''')
print()
if Enter == '1' :
	code = input('\033[0;39m* \033[0;32mEnter Your Code \033[0;34m:\033[0;39m ')
	count = input('\033[0;39m* \033[0;32mEnter The Number Of Invitations \033[0;34m:\033[0;39m ')
	print()
	for anas in range (int(count)) :
		anaspro = anas+1
		Numbers = '0123456789'
		Letters = 'abcdefghijklmnopqrstuvwxyz'
		user = random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)
		pwd = random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Letters)+random.choice(Numbers)+random.choice(Numbers)+random.choice(Numbers)
		link1 = 'https://api.cofb8.com/login/register'
		header1 = {'Host':'api.cofb8.com',
		'content-length':'156',
		'lang':'US',
		'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
		'content-type':'application/x-www-form-urlencoded',
		'accept':'*/*',
		'origin':'https://www.cofb8.com',
		'x-requested-with':'mark.via.gp',
		'sec-fetch-site':'same-site',
		'sec-fetch-mode':'cors',
		'sec-fetch-dest':'empty',
		'referer':'https://www.cofb8.com/',
		'accept-encoding':'gzip, deflate',
		'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
		data1 = {'lang':'US','username':user,'password':pwd,'code_value':'','code_key':'','areacode':'57','phone':'','code':'','rec_code':code,'mail':'','mail_code':''}
		req1 = requests.post(link1,headers=header1,data=data1)
		if 'Successful Operation' in req1.text :
			token = req1.json()['data']['token']
			token_key = req1.json()['data']['token_key']
		else :
			print('\033[0;39m» \033[0;31mAccount Creation Error\033[0;39m')
			break
		link2 = 'https://api.cofb8.com/action/apply'
		header2 = {'Host':'api.cofb8.com',
		'content-length':'19',
		'lang':'US',
		'usertoken':token,
		'usertokenkey':token_key,
		'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
		'content-type':'application/x-www-form-urlencoded',
		'accept':'*/*',
		'origin':'https://www.cofb8.com',
		'x-requested-with':'mark.via.gp',
		'sec-fetch-site':'same-site',
		'sec-fetch-mode':'cors',
		'sec-fetch-dest':'empty',
		'referer':'https://www.cofb8.com/',
		'accept-encoding':'gzip, deflate',
		'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
		data2 = {'lang':'US','action_id':'2'}
		req2 = requests.post(link2,headers=header2,data=data2)
		if 'Successful Operation' in req2.text :
			file = open('Cofb.txt','a+')
			file.write(f'{user}:{pwd}\n')
			print(f'\033[0;39m» \033[0;32mSuccessfully Added Account\033[0;34m {anaspro}\033[0;39m ')
		else :
			print('\033[0;39m» \033[0;31mBonus Error\033[0;39m')
			break
		file.close()
if Enter == '2' :
	Sc = input('\033[0;39m* \033[0;32mEnter SC_ID \033[0;34m:\033[0;39m ')
	Bd = input('\033[0;39m* \033[0;32mEnter BD_ID \033[0;34m:\033[0;39m ')
	print()
	try :
	   uspd= open('Cofb.txt','r')
	except :
		print('\033[0;39m» \033[0;31mError In The File \033[0;39m')
		exit()
	for dup in uspd.readlines():
	      splitfile = dup.strip().split(":")
	      user = splitfile[0]
	      pwd = splitfile[1]
	      link3 = 'https://api.cofb8.com/login/login'
	      header3 = {'Host':'api.cofb8.com',
  		'content-length':'156',
  		'lang':'US',
  		'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
  		'content-type':'application/x-www-form-urlencoded',
  		'accept':'*/*',
  		'origin':'https://www.cofb8.com',
  		'x-requested-with':'mark.via.gp',
  		'sec-fetch-site':'same-site',
  		'sec-fetch-mode':'cors',
  		'sec-fetch-dest':'empty',
  		'referer':'https://www.cofb8.com/',
  		'accept-encoding':'gzip, deflate',
  		'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
	      data3 = {'lang':'US','username':user,'password':pwd,'code_value':'','code_key':''}
	      req3 = requests.post(link3,headers=header3,data=data3)
	      if 'Successful Operation' in req3.text :
	      	token = req3.json()['data']['token']
	      	token_key = req3.json()['data']['token_key']
	      	link4 = 'https://api.cofb8.com/my/info'
	      	header4 = {'Host':'api.cofb8.com',
		      'content-length':'19',
  			'lang':'US',
 	 		'usertoken':token,
  			'usertokenkey':token_key,
		  	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
		  	'content-type':'application/x-www-form-urlencoded',
		  	'accept':'*/*',
  			'origin':'https://www.cofb8.com',
  			'x-requested-with':'mark.via.gp',
  			'sec-fetch-site':'same-site',
		  	'sec-fetch-mode':'cors',
  			'sec-fetch-dest':'empty',
  			'referer':'https://www.cofb8.com/',
  			'accept-encoding':'gzip, deflate',
		  	'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
	      	data4 = {'lang':'US'}
	      	req4 = requests.post(link4,headers=header4,data=data4)
	      	balance = req4.json()['data']['balance']
	      	link5 = 'https://api.cofb8.com/match/buy'
	      	header5 = header4
	      	data5 = {'lang':'US','sc_id':Sc,'bd_id':Bd,'zd_type':'2','money':balance,'money_type':'1'}
	      	req5 = requests.post(link5,headers=header5,data=data5)
	      	if 'Successful Operation' in req5.text :
	      		print(f'\033[0;39m» \033[0;32mTask Completed For \033[0;34m{user}\033[0;39m')
	      	else :
	   	   	print(f'\033[0;39m» \033[0;31mTask Error For \033[0;34m{user}\033[0;39m')
	      else :
	      	print(f'\033[0;39m» \033[0;31mLogin Failed For \033[0;34m{user}\033[0;39m')
if Enter == '3' :
	   try :
	   	uspd= open('Cofb.txt','r')
	   except :
	   	print('\033[0;39m» \033[0;31mError In The File \033[0;39m')
	   	exit()
	   for dup in uspd.readlines():
	      splitfile = dup.strip().split(":")
	      user = splitfile[0]
	      pwd = splitfile[1]
	      link6 = 'https://api.cofb8.com/login/login'
	      header6 = {'Host':'api.cofb8.com',
  		'content-length':'156',
  		'lang':'US',
  		'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
  		'content-type':'application/x-www-form-urlencoded',
  		'accept':'*/*',
  		'origin':'https://www.cofb8.com',
  		'x-requested-with':'mark.via.gp',
  		'sec-fetch-site':'same-site',
  		'sec-fetch-mode':'cors',
  		'sec-fetch-dest':'empty',
  		'referer':'https://www.cofb8.com/',
  		'accept-encoding':'gzip, deflate',
  		'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
	      data6 = {'lang':'US','username':user,'password':pwd,'code_value':'','code_key':''}
	      req6 = requests.post(link6,headers=header6,data=data6)
	      if 'Successful Operation' in req6.text :
	      	token = req6.json()['data']['token']
	      	token_key = req6.json()['data']['token_key']
	      	sc_id = input('\x1b[0;39m* \x1b[0;32mEnter SC_ID \x1b[0;34m:\x1b[0;39m ')
	      	link7 = 'https://api.cofb8.com/match/play'
	      	header7 = {'Host':'api.cofb8.com',
		      'content-length':'19',
  			'lang':'US',
 	 		'usertoken':token,
  			'usertokenkey':token_key,
		  	'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; BASIC Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Safari/537.36',
		  	'content-type':'application/x-www-form-urlencoded',
		  	'accept':'*/*',
  			'origin':'https://www.cofb8.com',
  			'x-requested-with':'mark.via.gp',
  			'sec-fetch-site':'same-site',
		  	'sec-fetch-mode':'cors',
  			'sec-fetch-dest':'empty',
  			'referer':'https://www.cofb8.com/',
  			'accept-encoding':'gzip, deflate',
		  	'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
	      	data7 = {'lang':'US','sc_id':sc_id}
	      	req7 = requests.post(link7,headers=header7,data=data7)
	      	result = input('\x1b[0;39m* \x1b[0;32mEnter The Match Result \x1b[0;34m:\x1b[0;39m ')
	      	splitfile2 = result.strip().split('/')
	      	zd = int(splitfile2[0])
	      	kd = int(splitfile2[1])
	      	for vpro in req7.json()['data']['bd'] :
	      		if vpro['zd'] == zd :
	      			if vpro['kd'] == kd :
	      				bd_id = vpro['bd_id']
	      				os.system('clear')
	      				print(f'\033[0;39m» \033[0;34m{sc_id}')
	      				print(f'\033[0;39m» \033[0;34m{bd_id}')
	      				input()
	      else :
	      	print(f'\033[0;39m» \033[0;31mLogin Failed For \033[0;34m{user}\033[0;39m')
	      	print()