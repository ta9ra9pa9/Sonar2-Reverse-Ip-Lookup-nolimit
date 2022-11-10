### Python v3
### By @ta9ra9pa9 , For more Hacking tools visite our channel https://datanumbersunlimited.t.me/
###
import requests,time,urllib3
from multiprocessing import Pool
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)	

class INDEx:
	def __new__ (self):
		print("""
		
Script Started - 
				By @ta9ra9pa9
		contact https://t.me/datanumbersunlimited
		
		""")

class Ipto():
	def __init__(  self , ip ):
		"""
				Hello , Have fun any Problems or Bugs contact me !! at @ta9ra9pa9
		"""
		self.ip = ip
		self.website = "https://sonar2.pythonforautomation.com/ip/%s" % ip
		self.domains = None

	def __str__(  self ):
		
		self.domains = requests.get(self.website , timeout=20 ).text
		return self.domains
		
	def __repr__( self ):
		return str(self.__str__())
		
		
def findandsave(ip):
	"""
	Save Data

	"""
	for x in range(6):
		try:
			list = eval ( str(   Ipto(ip)   ) )		
			# ~ print(type( list ) )
			if list:
				[ open("domains.txt",  "a"  , encoding="Latin-1").write("%s\n" % bb ) for bb in list  ]
				print("From this ip ==> %s saved %s domains "  % ( ip  , len(list)     ) )
				break
		except:
			time.sleep(5)
			pass


# ~ findandsave("192.241.255.16")
def main():
	
	namelist = input("[x] list ip : " )
	
	try:
		listip = open( namelist , "r" , encoding="Latin-1" ,  errors='ignore').read().splitlines()
	except:
		print("List Problem !")
		exit()

	ThreadPool = Pool(20) # Please don't change this "20" !!
	ThreadPool.map(findandsave, listip)


if __name__ == "__main__":
	INDEx()
	main()
