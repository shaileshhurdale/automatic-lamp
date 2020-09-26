
try:
	fileRef = open("sample1.txt","r");
	str = fileRef.read();
	print("The contents of the file: "+str);
	fileRef.close();
except IOError as e:
	print("unable to find the specified file! ",e);
finally:
    print("This code will be executed!");
#except:
   # print("Error in the execution!")
#else:
	#print("file had been read successfully!");