- Date : 2020-06-25
- Tags : #Java

## Interface can extend another interface


Interfaces are a special kind of class which is completely abstract.  Variables are always `static` and `final` and methods are always `public abstract`.  An interface cannot implment another interface, because that would require we define those methods, but an interface does not include method definitions. So use `interface SubInterface extends MainInterface`.

[Why an interface cannot implement another interface in Java?](https://www.tutorialspoint.com/why-an-interface-cannot-implement-another-interface-in-java)
