Lecture 23 - Inheritance
-------------------------

One of the major benefits of the object-oriented paradigm
is that you can reuse code, because a *class* is a kind
of a data type structure template.

An easiest way to reuse code, is using **Inheritance**,
which is a good approach to implement relationship between classes.

The best way to understand the concept behind *inheritance*,
is with an example situation.

Lets think in a program to coordinate
the people in a virtual system created by us (University).

If we think in people, there are several characteristics
in common, regardless the profession or activity,
like some functionalities, and attributes (age, sex, address,
name, etc).
But, depending of the activity their have specific characteristics,
like the amount of the salary, the marks, the courses, etc.

We can create a first class called `People`:

::

    class People():
        def __init__(self,name,age,sex,address):
            self.name = name
            self.age = age
            self.sex = sex
            self.address = address
        def get_name(self):
            return self.name
        def get_age(self):
            return self.age
        def get_sex(self):
            return self.sex
        def get_address(self):
            return self.address
        def talk(self):
            print 'Hello, my name is', self.get_name


   
Looks complicated, but the idea is very simple,
returning the *data* of the class with *methods*,
and a little methods to present the person,
saying `Hello`.

Now we need to create two different classes
which **inherit** from the `People` class their structure,
called `Student` and `Professor`.

Note that creating another classes to differentiate
the students from the professors, we have more possibilities
to add and change new functionality. Also, you can always
refer to a student or professor object as a `People` object,
which will be very useful in cases when you try to know
the total amount of people in the University.

Lets create the `Professor` class:

::

    class Professor(People):
        def __init__(self,name,age,sex,address):
            People.__init__(self,name,age,sex,address)
            self.courses = {}
        def add_course(self,course,number):
            self.courses[number] = course
        def del_course(self,number):
            del self.courses[number]
        def get_courses(self):
            return self.courses

The only strange lines for you,
will be:

::

    class Professor(People):

This means, that we are creating a new class called `Professor`
which inherit attributes (variables and methods) from `People` class.

::

    People.__init__(self.name,age,sex,address)

This means that we will initialize the `Professor`
instance using the method in the *parent class*,
called `People`.


A couple of live examples:

::

    >>> p = Professor('John Smith',34,'male','Evergreen Terrace, 742')
    >>> print p.get_address()
    Evergreen Terrace, 742
    >>> p.talk()
    Hello, my name is John Smith
    >>> p.add_course('Python','PPC01')
    >>> print p.get_courses()
    {'PPC01': 'Python'}


Now we will create the `Student` class:

::

    class Student(People):
        def __init__(self,name,age,sex,address):
            People.__init__(self,name,age,sex,address)
            self.grades = {}
        def add_course(self,course):
            self.grades[course] = []
        def add_grade(self,course,grade):
            tmp = self.grades[course]
            tmp.append(grade)
            self.grades[course] = tmp
        def get_average(self):
            for course in self.grades:
                tot = 0
                for grade in self.grades[course]:
                    tot += grade
                print 'Course:', course, ':',tot/len(self.grades[course]), '(',self.grades[course],')'


The methods here are different to the `Professor` methods,
and if you note, both classes has a method with the same name (this is called **Polymorphism**).
The idea is to have a dictionary with the grades of the courses,
in the form:

::

    {'PPC01':[100,65,20],'PPC02':[20,100,100]}

Then we have methods to add new courses and calculate the
average of each course.

A couple of live examples:

::

    >>> s = Student('Marge Simpson',19,'female','Good street, 657')
    >>> s.add_course('PPC01')
    >>> s.add_grade('PPC01',100)
    >>> s.add_grade('PPC01',50)
    >>> s.add_course('PPC02')
    >>> s.add_grade('PPC01',30)
    >>> s.add_grade('PPC02',10)
    >>> s.get_average()
    Course: PPC02 , Average: 10 ( [10] )
    Course: PPC01 , Average: 60 ( [100, 50, 30] )

So finally, we have one parent class,
who is the base for another two new subclasses.
We are reusing code,
we write a good structure to work
with different data,
and the main idea is that the OO paradigm,
is very huge and useful, this is only
a little example to understand
the concept behind, but will be really
good if you can read an Object-Oriented book.


Another simple and used example to understand
the **polymorphism** and the **inheritance** concepts,
is the following:

Two Cat objects and one Dog are instantiated and given names, and then they are gathered in an array animals and their talk() method is called.

::

    class Animal:
        def __init__(self, name):
            self.name = name
        def talk(self):
            raise NotImplementedError("You need to implement this method in a Subclass")

    class Cat(Animal):
        def talk(self):
            return 'Meow!'     

    class Dog(Animal):
        def talk(self):
            return 'Woof! Woof!'
    
    class Cow(Animal):
        def talk(self):
            return 'Moooo!'
    
    class Snake(Animal):
        def talk(self):
            return 'Ssssss!'


All the subclasses inherit the empty method from
`Animal` and their implemented with the sound
of the animals.

So, lets try this code:

::

    >>> animals = []
    >>> animals.append(Cat('Tom'))
    >>> animals.append(Dog('Bobby'))
    >>> animals.append(Cow('Amy'))
    >>> animals.append(Snake('Beast'))
    >>> for i in animals:
    ...    print i.name, ':', i.talk()
    ...    
    >>> 
    Tom : Meow!
    Bobby : Woof! Woof!
    Amy : Moooo!
    Beast : Ssssss!
 

Exercises
~~~~~~~~~

* Look carefully the next example, and without execute it,
  answer the question, What will be the output?

  ::
  
      class A:
          def f(self):
              return self.g() 
          def g(self):
              return 'A'
      class B(A):
          def g(self):
              return 'B'
      a = A()
      b = B()
      print a.f(), b.f()
      print a.g(), b.g()

  Execute the code and verify your answer.

* PENDING
* Chess
