class Parent:
    def __init__(self):
        print("Parent Class..");
    
    def sampleMethod(self):
        print("Sample Parent method..");
    
    def secondMethod(self):
        print("second Method of parent class!")
        
class Child(Parent):
    def __init__(self):
        print("Child Class..");
    
    def sampleMethod(self):
        print("Sample child method...");
        
    def childMethod(self,str):
        print(" arg: "+str);
        
    def childMethod(self,str1,str2):
        print("args: "+str1+" "+str2);
        
c=Child();
c.sampleMethod();
c.secondMethod();
c.childMethod("Shailesh","Hurdale");