import os
import time
import glob
import shutil

timer_start=time.time()
file_counting=0

# Indiquer le chemin de votre dossier contenant les fichiers .h5
source_file_folder = r'E:\Session 2021-04-28 09-31-51'

# Indiquer le chemin où l'ensemble des fichiers doivent être copiés
output_folder = r'C:\Users\thfaure\Desktop\2021\Pop_50025\Avril_2021'

os.chdir(source_file_folder)

h5_folder_list = glob.glob('*_1')
# print("Debug only : "+h5_folder_list)

for folder in h5_folder_list:
	print("Current folder is : "+folder)
	os.chdir(source_file_folder+'/'+folder)

	h5_file = glob.glob('*_1.h5')

	for file in h5_file:
		print("File currently processed : "+file)
		shutil.copy(file, output_folder)
		file_counting=file_counting+1


timer_end = time.time()
print("")
print(str(file_counting)+" h5 files from copying from directory " + source_file_folder + " took " + str(int(timer_end - timer_start)) + " seconds")