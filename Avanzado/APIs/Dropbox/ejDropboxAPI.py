#############
# API Dropbox
#############
import dropbox

class DBManager(object):
	"""Una clase envolvente para el API de Dropbox"""
	def __init__(self,key=None):
		self.key=key
		self.api=""
		self.connect()

	def connect(self):
		"""Metodo para conectarnos al API de Dropbox"""
		self.api=dropbox.Dropbox(self.key)
		print("Conexión Exitosa")
		print("Bienvenido!! "+self.getAccountInfo().name.display_name)
 
	def getAccountInfo(self):
		return self.api.users_get_current_account() 

	def listDir(self,directory):
		if not directory:
			print("No es un directorio")
		else:
			for subdir in self.api.files_list_folder("/"+directory).entries:
				print("-> ",subdir.name)

	def upload(self,file):
		with open(file,'rb') as f:
			self.api.files_upload(f.read(),"/"+file)

	def download(self,file):
		self.api.files_download_to_file(file,"/"+file)

if __name__ == '__main__':
	dM=DBManager(open("llave.txt").read())
	dM.listDir("/")
	dM.upload("koala.jpg")
	dM.download("script.bat")
