# 0x00. AirBnB clone - The console 

## Resources:books:
Read or watch:
* [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rwi)
* [packages](https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q)
* [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g)
* [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q)
* [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g)
* [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

---
## Learning Objectives:bulb:
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module 
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

## Usage
Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

---

### [0. README, AUTHORS]
* Write a ```README.md```:
    * description of the project
    * description of the command interpreter
        

### [1. Be PEP8 compliant! ]
* Write beautiful code that passes the PEP8 checks. 


### [2. Unittests](tests/)
* All your files, classes, functions must be tested with unit tests 


### [3. BaseModel](models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes


### [4. Create BaseModel from dictionary](models/base_model.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation. 


### [5. Store first object](models/engine/file_storage.py)
* Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
* Update models/__init__.py: to create a unique FileStorage instance for your application
* Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter
```bash
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ 
```


### [7. Console 0.1](./console.py)
* Update your command interpreter (console.py) to have these commands:
    * `create`
    * `show`
    * `destroy`
    * `all`
    * `update`

```bash
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
```

### [8. First User](models/user.py)
* Write a class User that inherits from BaseModel
* Update FileStorage to manage correctly serialization and deserialization of User
* Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User

### [9. More classes!]
Write all those classes that inherit from BaseModel:
    * [State](models/state.py)
    * [City](models/city.py)
    * [Amenity](models/amenity.py)
    * [Place](models/place.py)
    * [Review](models/review.py)
    

### [10. Console 1.0]
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
* Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

---

## Authors
* **Tim McMacken** - [TMcMac](https://github.com/TMcMac)
* **Viet Tran** - [veeteeran](https://github.com/veeteeran)
