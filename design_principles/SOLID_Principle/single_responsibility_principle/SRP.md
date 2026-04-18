###Single Responsibility Principle 

```A class should have only one reason to change.```

The principle states that if we have  2 reasons to change a class, we have to split the functionality in two classes. Each class will handle only one responsibility and in the future if we need to make one change we are going to make a change in the class having more responsibilities. The change might effect the other functionality related to the other responsibility in the class.

The *Single Responsibility Principle* is a simple and intuitive principle but in practise it is sometimes hard to get it right. 

**Wikipedia says**:
 
```Single Responsibility Principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software and that responsibility should be encapsulated by the class, module or function.```


####Conclusion 
The Single Responsibility Principle represents a good way of identifying classes during the design phase of an application and it reminds you to think of all the ways a class can evolve. A good separation of responsibility is done only when the full picture of how the application should work is well understood.