import os
import zipfile
# os.chdir('c:\\')
exampleZip=zipfile.ZipFile('C:\\Users\\liming\\Desktop\\program\\work\\example-code.zip')
filename=exampleZip.namelist()
print(filename)
exampleZip.extractall()
exampleZip.close()