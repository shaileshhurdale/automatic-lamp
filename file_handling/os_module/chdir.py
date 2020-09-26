import os;

path = r"D:\python examples\file_handling";
os.chdir(path);
os.mkdir("sampleDir");
print("Directory has been changed!!");
print("current working dir: "+os.getcwd());