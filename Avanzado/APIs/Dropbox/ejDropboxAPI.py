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
		"""Metodo para regresarnos la información de una cuenta"""
		return self.api.users_get_current_account() 

	def listDir(self,directory="/"):
		"""Metodo para listar un directorio"""
		if not directory:
			print("No es un directorio válido")
		else:
			for subdir in self.api.files_list_folder("/"+directory).entries:
				print("-> ",subdir.name)

	def download(self,file):
		"""Metodo para descargar un archivo a dropbox"""
		self.api.files_download_to_file(file,"/"+file)
		
	def upload(self,file):
		"""Metodo para cargar un archivo a dropbox"""
		with open(file,'rb') as f:
			self.api.files_upload(f.read(),"/"+file)


if __name__ == '__main__':
	dM=DBManager(open("llave.txt").read())
	dM.listDir("/")
	dM.upload("koala.jpg")
	dM.download("script.bat")
