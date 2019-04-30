#!/usr/bin/python	
import os	
from subprocess import call	

 currentdir=os.getcwd()	

 os.chdir(str(currentdir))	

 if (os.path.isdir(str(currentdir)+"/ToolBox")) is False:	
	os.makedirs(str(currentdir)+"/ToolBox")	

 os.chdir(str(currentdir)+ "/Lists")	

 files = [x for x in os.listdir(currentdir+str("/Lists")) if x.endswith('.txt')]	

 for filename in files:	
	dirname= os.path.splitext(str(filename))[0]	
	os.chdir(str(currentdir)+"/ToolBox/")	
	if (os.path.isdir(str(currentdir)+"/ToolBox/")) is False:	
		os.system("rm -rf "+str(dirname))	
	if (os.path.exists(str(currentdir)+"/ToolBox/"+str(dirname))) is False:	
		os.makedirs(str(currentdir)+"/ToolBox/"+str(dirname))	
	os.chdir(str(currentdir)+"/ToolBox/"+str(dirname))	
	f=open(str(currentdir)+ "/Lists/"+str(filename))	
	line=f.readline()	
        line.replace("git clone", "git pull")	
	while line:	
		os.system(str(line))	
		line=f.readline()	
	f.close()
