#Python_project_template

## Elevator pitch intro

This is a general purpose template for Python projects. It includes some bare-bones features that are usefull accross 
most Python projects.

## Requirements and dependencies
- Python 3.6 (tested)  

## Directory and file structure

This is the vanilla directory structure for the template:

    .
    ├── app
    │   └── __init__.py
    ├── config
    │   ├── dev.ini
    │   ├──__init__.py
    │   ├── prod.ini
    │   └── test.ini
    ├── logs
    ├── main.py
    ├── README.md
    ├── run_tests.py
    ├── tests
    │   ├── __init__.py
    │   └── tests_basic.py

Quick directory legend:
- **root**: main directory for the project as a whole
- **app**: main application directory. Put your code and app-specific directorires here. 
Please note the **\__init\__.py** file, which containts an app factory function, i.e. it should import and call your 
application code. This application factory function is called by **main.py**
- **config**: contains .ini files for different app configurations. By default production, development and testing 
config files are present.
- **logs**: default logfile directory
- **tests**: test definitions for _unittest_ are containted here. By default only a handful of very basic test cases 
are included

## App architecture
                  
                  
                         |    INTERNAL APP MODULES AND RESOURCES    |
                         |(helpers, static files,db migrations etc.)|
                                            ^
                                            ^
                                            ^
                           | LOGGER | <<<| APP |<<<| CONFIG |
                                |           |           |
                                |           |           |    
                                |           |           |
                                -------------------------
                                            |
                                            |
                                            |
                                         | MAIN | <---------- | TESTS | 
                                                                          
                                                      
                                                                        
    
- MAIN (**main.py**) is the central orchestration scrippt
* MAIN initializes the LOGGER, loads the CONFIG and creates an APP instance
* APP should expect the config to be passed in as a dictionary
* APP will write to the LOGGER (with whatever output the LOGGER handlers will be configured with; see *Reference* 
section for details)
* APP should import it's own modules and resources (the user will likely be best served by putting them in the **app** 
project directory). The idea is to keeep **main.py** clean and only used it for cross-project imports and 
functionalities. This should guarantee that testing will separate any issues with the app proper from basic issues with
**main.py** or it's core functionalities.
* **TESTS** are executed by calling **MAIN**, not the **APP** directly.
 
## Running the template scripts

To run the scripts provided in the template, cd into the template directory and:
- set the desired application environment type (prod, dev, test) on the command line:
       
        export APP_ENV=test
       

- For the main script running the app:
    
        python3 main.py
   
- For the predefined basic test set:
        
        python3 run_tests.py

## Installation

Since this template is so basic, you won't have much to do to get it running.

### 1. Download

Clone or download the zipped files to your directory of choice.

### 2. Checking the installation

The template should be ready to go as soon as you clone/download it, but I'd recommend running the template scripts
referenced in the *Running the template scripts* section above. The output for **run_tests.py** should be similar to:

    /usr/bin/python3.6 /home/newton/Programming/Python/Python_project_template/run_tests.py
    test_app_is_not_none (tests_basic.BasicTestCase) ... ok
    test_config_is_not_empty (tests_basic.BasicTestCase) ... ok
    test_logger_is_present (tests_basic.BasicTestCase) ... ok
    test_main_is_running (tests_basic.BasicTestCase) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.007s

    OK
    
Running **main.py** should give you:

    2019-05-23 00:30:22,155 : __main__ : main : 38 : INFO : Running app: Anonymous App
        

## Use cases

This project is meant as a starting point for other Python projects, big and small. You can build out your app into 
whatever flavour you like and the project framework is simply kickstarting that process. The end goal is to allow the 
user to focus on implementing their own ideas fast and smooth, without wasting time on set up tasks. 

## Further development

Currently no further functionalities are planned (this is supposed to be a very lightweight project). I will be adding 
to it if I decide that a feature is greatly needed across many Python projects. 

## FAQ

**Q:** Who is this for?

**A:** Beginner and intermediate Python programmers. If you've cut your teeth on Python esoterica, you probably use a
framework or own templates. But if you're frustrated with having to shuffle files around, play with imports etc. and 
just want something to quickly start developing your Greatest Ever App Idea, I hope this helps.

**Q:** Why not use a proper framework, say Flask or Django?

**A:** By any means, go ahead! You can pick up my template in 10 minutes and just start hacking away code though. I'd 
still advise working with a framework if you want to do something bigger than a prototype project.


**Q:** You say "app instance" but it's not a instance of a class. Huh? I'm confused.

**A:** Yup. This is deliberate non-commitment on my part. Using a class instance as default could give off the 
impression that going for a Object Oriented Programming flavour is the best answer for all apps, when it's surely not. 
If you want to create a simple Python program for, say, disk cleanup tasks, it might just be a straightforward 
functional or procedural app, no "encapsulation via classes" needed. If however you want OOP, simply modify the 
**__init__.py** in the *./app* directory to return an instance of a class of your choosing. It will work as well.

**Q:** Where should I put my helpers scripts and class definitions?

**A:** I'd strongly advise putting all of the application-specific code in the *./app* directory and any subdirectories
there.

**Q:** Why does the **app** need to be called via **main.py**? Seems convoluted.

**A:** This seems to me to be a good away of keeping the call and import stacks in order. This is the answer to the 
following problem. If you execute your app from the *./app* directory, *./logs*, *./tests* and *./config* are all in the
parent directory and Python runtime get's fussy when trying to import from directories that are parents to the directory
in which the executed file is. (It treats the executable's directory as root basically.) If you put you app file on the
same directory level as, say, *./tests* you encounter other problems (especially if you have a lot of user-defined 
modules and files). The way this project does it, **main.py** represents the root level. Modules such as **logging**
branch "down". This should limit import issues (which are imho the bain of beginner Python users) to a minimum. 


## References

1. Flask: this small project was largely (and probably quite obviously) inspired by the way Flask does it's thing. If 
you don't know, Flask is a "micro-framework" for Python web apps. It's great. Give it a go at:
 [flask.pocoo.org/](flask.pocoo.org/)
2. ConfigParser: I used this Microsoft Windows-style configuration module since .ini files are pretty common and are
easily readable (easier than JSON I think). The ideas is that the user can add further sections to the .ini files 
provided in the **./config** directory or create their own config files.
3. Logger: the logging module is just great. Honestly, I feel kinda ashamed I haven't discovered it earlier. It also
plays pretty nice with ConfigParser, so you don't need a config mechanism separate from the one that's used for the app
in general. *mariocj89* wrote a great gist about the module, I highly recommend it for anybody wanting to use the 
logging module:
[https://gist.github.com/mariocj89/73824162a3e35d50db8e758a42e39aab](https://gist.github.com/mariocj89/73824162a3e35d50db8e758a42e39aab)
4. unittest: the basic unittest module is good enough for most projects: 
[https://docs.python.org/3.6/library/unittest.html](https://docs.python.org/3.6/library/unittest.html)
5. Pathlib: this one is both great and not-so-great (it abstracts the differences between file systems, which I think 
any dev should be exposed too at least once or twice). Still, a great module for handling paths gracefully. Here
is a good Real Python writeup on Path: [https://realpython.com/python-pathlib/](https://realpython.com/python-pathlib/)
    
