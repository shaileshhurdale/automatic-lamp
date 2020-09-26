import intro

#from intro import *

import math

#introfun();

#secondFun();

def helloWorld():
    print("printting hello world inside function!!");
    return;
    
def printData(str):
    print("Input string provided: "+str);
    return;
    
helloWorld();

printData("shailesh");

myList=[10,20,30];

print("list before function call: "+str(myList));

print("adding some changes to at remote repo");


def modifyList(list):
    list.append([1,2,3]);
    return;
    
modifyList(myList);

print("list after calling function: "+str(myList));

def callByvalue(data):
    data+=" Hurdale";
    print("Data inside function: "+data);
    return;
    
data="shailesh";

callByvalue(data);

print("Data outside function: "+data);

def funArg(str,num="18"):
    print(str+" "+num);
    return;
    
funArg("Entered Number is ","10");

funArg(str="number is: ");

def printParams(firstNum,*varArgs):
    print("firstNUm "+firstNum);
    for val in varArgs:
        print(" "+val);
        
    return;
    
printParams("10","20","30","40","50","Data");

sum = lambda arg1,arg2:arg1+arg2;

print(sum(10,20))

print(dir(intro))

reload(intro)
        
    
    
    
