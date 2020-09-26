fileref = open("samplewrite.txt","w");
fileref.seek(2,0);
fileref.write("I am writing new text in file");
fileref.close();
print("Data has been written successfully in file!");