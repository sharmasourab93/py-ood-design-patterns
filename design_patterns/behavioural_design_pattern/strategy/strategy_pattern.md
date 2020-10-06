# Strategy  

**Strategy** is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable. 


**Strategy** defines an interface common to all supported algorithms. Context uses this interface to call algorithms defined by concrete strategy. 


#### Motivation

There are common situations when classes  differ only in their behavior. For such cases, it is a good idea to isolate the algorithms in separate classes and have the ability to select different algorithms at runtime. 


#### Specific Problems

1. Passing data to/from Strategy Object. 
2. Families of related algorithms 
3. Optionally Concrete Strategy Objects
4. Strategy and Creational Patterns
5. Strategy and Bridge 


#### Hot Points 
The strategy design pattern splits the behaviour of a class from the class itself. This has some advantages, but the main drawback is that a client must understand how the strategies differ. Since, clients get exposed to implementation issues, the strategy design patterns should be used only when the variation in behaviour is relevant to them. 


#### Main Points For Strategy Pattern

1. Encapsulate Algorithms 
2. Several Techniques available 
3. Sequence of If/Else are a red flag.

#### Usage of the pattern in Python 

##### Usage Examples
The strategy pattern is very common in Python code. It's often used in various frameworks to provide users way to change the behaviour of a class without extending it. 

##### Identification
_Strategy pattern can be recognized by a method that lets nested object do the actual work, as well as the setter that allows replacing that object with a different one._ 


### Relations With Other Patterns
 
**Bridge**, **State**, **Strategy** have very similar structures. Indeed all of these patterns are based on _composition_, which is delegating work to other objects. However, they all solve different problems. A pattern isn't just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves. 
 

**Command** & **Strategy** may look similar because you can use both the parameterize an object with some action. However, they may have very different intents.
 
 - You can use **Command** to convert any operation into an object. The operation's parameters become fields of that object. The conversion lets you defer execution of the operation, queue it, store the history of commands to remote services etc. 
 
 - On the other hand, **Strategy** usually describes different ways of doing the same thing, letting you swap these algorithms within a single context class. 
 
**Decorator** lets you change the skin of an object, while strategy lets you change the guts. 
 
**Template Method** is based on inheritance: it lets you alter parts of an algorithm by extending those parts in sub-classes. **Strategy** is based on composition: you can alter parts of the object's behavior by supplying it with different strategies that correspond to that behavior. Template method works at the class level, so it's static. Strategy works on the object level, letting you switch behaviors at runtime. 
 
**State** can be considered as an extension of **Strategy**. Both patterns are based on composition: they change the behavior of the context by delegating some work to helper objects. **Strategy** makes these objects completely independent and unaware of each other. However, **State** doesn't restrict dependencies between concrete states, letting them alter the state of the context at will.  


#### References

1. [Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
2. [OODesign](https://www.oodesign.com/strategy-pattern.html)
3. Pluralsight Courses