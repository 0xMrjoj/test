from requests import post,get
import requests,threading,random

class Program_Features:
	def __init__(self): 
		self.bad=0
		self.LoginUser=input('[+] Enter Username: ')
		if self.LoginUser:pass
		else:print('[-] Please Enter username !! ');return Program_Features()
		self.LoginPass=input('[+] Enter Password: ')
		if self.LoginPass:pass
		else:print('[-] Please Enter Password !! ');return Program_Features()
		self.UsernameList=input('[+] Enter  List name : ')
		try:open(self.UsernameList,'r')
		except FileNotFoundError:print('[-] file not found , Try again.. '); return Program_Features()
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		self.login_Instagram()
	def Extracting_accounts_information(self,IDS,sess,Users):
		infoData = get(f'https://i.instagram.com/api/v1/users/{IDS}/info/',headers={'accept': '*/*','accept-language': 'ar,en-US;q=0.9,en;q=0.8','cookie': 'sessionid='+sess,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'})
		print('hhhhdujed')
		try:
			emails = str(infoData.json()['user']['public_email'])
			if emails=='':print(f'{Users}: There is no email...')
			else:
				Alls= f'{Users}:{emails}'
				print(Alls)
				with open('DataBase-Instagram.txt', 'a') as J:J.write(Alls+'\n')
   
		except KeyError:
			print(f'{Users}: There is no email...')

		try:
			numbers=str(infoData.json()['user']['contact_phone_number'])
			if numbers=='':print(f'{Users}: There is no number...')
			else:
				Allw= f'{Users}:{numbers}'
				print(Allw)
				with open('DataBase-Instagram.txt', 'a') as J:J.write(Allw+'\n')
		except KeyError:
			print(f'{Users}: There is no number...')
  
		try:
			numbers2=str(infoData.json()['user']['whatsapp_number'])
			if numbers2=='':print(f'{Users}: There is no whatsapp number...')
			else:
				All= f'{Users}:whatsapp:{numbers2}'
				print(All)
				with open('DataBase-Instagram.txt', 'a') as J:J.write(All+'\n')
		except KeyError:
			print(f'{Users}: There is no whatsapp number...')
  
		
	def Extract_ID_accounts(self):
		global sess
  		
		while True:
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				for Users in open(self.UsernameList,'r').read().splitlines():
					getInfo=get(f'https://www.instagram.com/{Users}/?__a=1&__d=dis',headers={'Host': 'www.instagram.com','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Cookie': 'sessionid='+sess,'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Accept-Language': 'en','Connection': 'keep-alive'},proxies=PROXY)
					if ( 'id' in getInfo.text ):
						try:
							IDS = getInfo.json()['graphql']['user']['id']
							self.Extracting_accounts_information(IDS,sess,Users)
							#threading.Thread(target=self.Extracting_accounts_information(IDS,sess,Users)).start()
						except requests.exceptions.JSONDecodeError:print(f'[-] User not found : {Users}')
					elif getInfo.status_code==404:print(f'[-] User not found : {Users}')
					elif getInfo.status_code==401:
						self.bad+=1
						print(f'\r[+] Bad Proxy : [{self.bad}]\r',end="")
					else:
						print('======================')
						print(getInfo)
						print(getInfo.text)
			except requests.exceptions.ConnectionError:
					self.bad+=1
					print(f'\r[+] Bad Proxy : [{self.bad}]\r',end="")
			except requests.exceptions.ReadTimeout:
					self.bad+=1
					print(f'\r[+] Bad Proxy : [{self.bad}]\r',end="")
	
	def Trts(self):
		global sess
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Extract_ID_accounts)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
	def login_Instagram(self):
		global sess
		CheckLogin = post('https://www.instagram.com/accounts/login/ajax/', headers={'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"','user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36','x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0','x-instagram-ajax': '0c15f4d7d44a','x-requested-with': 'XMLHttpRequest'}, data={f'username': self.LoginUser,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:'+self.LoginPass,'queryParams': '{}','optIntoOneTap': 'false'})
		if ( 'userId' in CheckLogin.text ):
			print(f'[+] Successful login [{self.LoginUser}]')
			print('\n==============================\n')
			sess=CheckLogin.cookies['sessionid']
			self.Trts()
		else:print(CheckLogin.text);print(CheckLogin);input(' ')
Program_Features()
