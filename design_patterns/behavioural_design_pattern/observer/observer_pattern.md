# Observer Pattern 


*Observer* is a behavioral pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing. 


### Intent

Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. 

### Motivation 

To have a good design means to decouple as much as possible and to reduce the dependencies. The Observer design pattern can be used whenever a subject has to be observed by one or more observers. 

### Specific Problems 
1. Many Subjects to Many Observers
2. Who triggers the Update?
3. Making sure subject state is self-consistent before notification  
4. Specifying points of Interest 
5. Encapsulating Complex Update Semantics.
6. Push and Pull Communication Methods.
