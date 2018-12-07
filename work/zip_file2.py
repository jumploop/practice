import zipfile

newzip=zipfile.ZipFile('newzip.zip','w')
newzip.write('zip_file.py',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()