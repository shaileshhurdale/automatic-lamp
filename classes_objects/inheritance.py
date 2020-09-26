class Parent:
    parentAttr=100;
    
    def __init__(self):
        print("caling parent class constructor..");
        
    def parentMethond(self):
        print("calling parent method..");
        
    def increaseCounter(self):
        Parent.parentAttr+=100;
        print("Updated counter value: "+str(Parent.parentAttr));
        
class Child(Parent):
    
    def __init__(self):
        print("calling the child constructor...");
        
    def childMethod(self):
        print("Calling child method....");
        
c = Child();
c.parentMethond();
c.increaseCounter();
c.childMethod();

p=Parent();