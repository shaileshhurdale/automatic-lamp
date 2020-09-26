fileref=open("sample.txt","r");
str= fileref.read();
fileref.close();
print("The contents of the file: "+str);

fileref=open("sample.txt","r");

str = fileref.read(4);
fileref.close();
print("Reading first 4 char: "+str);

fileref=open("sample.txt","rb");

str = fileref.read(4);
fileref.close();
print("Reading first 4 Byte: ");
print(str);


fileref=open("sample.txt","rb");

str = fileref.read();
fileref.close();
print("Reading all Byte: ");
print(str);




