# Running the file:

Running the file can be done in the terminal using the python command. Using the terminal enter "python", then the name of the desired file to run e.g. "Code/event_planner.py", finally choose the desired text file to run using the 2 algorithms and make sure the correct file path is used. For example if the list of text files are stored in a file called "Input_Files" use file name "Input_Files/input_10.txt" for example.


To run this program in the terminal use "python Code/event_planner.py Input_Files/input_10.txt", replacing the "input_10.txt" with a file of your choice as well as the "event_planner.py" with a python file of your choice. Run this in the main terminal and not inside any enclosed folders or directories as some of the resources may not be accessible inside separate directories.

```console
$ python Code/event_planner.py Input_Files/input_10.txt
```

When running the code, if you have chosen to run the program on a text file that has more activities than the "input_20.txt" file it will not function correctly as the brute force algorithm cannot compute that many possibilities in a suitable time-frame. If you would like to run files that have a larger length then please use just the dynamic algorithm which is stored in the "Code" folder named "Dynamics.py". This can be run in the same way as the other programs. 

When running the "comparisons.py" there is no need to choose an input file to run it. It can be run using just: "python Code/comparisons.py" or by pressing the run button in an IDE. This is because no input file is used on this file so it can be run with no arguments passed in. 

```console
$ python Code/comparisons.py
```

# Libraries and dependancies:

The main dependancy for running this program is having Python installed. Having an updated version of Python such as Python 3.13 is necessary for the execution of this program. To check your python version use the following command below.

```console
$ python --version
```

There are several libraries used in the execution of this program and the main files for creating the event planner use only built-in python modules. The modules time and sys are imported as well as chain and combinations from Itertools. As these are all built-in no external dependancies need to be installed.  

If you want to run the comparisons.py file there are a few different depenancies that will need to be installed prior to running the file. Firstly, the libraries matplotlib and numpy must be installed on the selected python interpreter. These libraries can be installed using 'pip' and an example will be avilable below. If the "pip" command is not available then it can be installed using another command listed below. Once these libraries have been installed this file can be ran in the same way as the other event_planner files. Also the event_planner.py file will need to be downloaded on the computer that the comparisons.py file is being run on as there are 2 imported functions from event_planner.py. The output of the comparisons.py file will be stored in 2 separate PNG files. 

### Install PIP
```console
python -m ensurepip --upgrade
```
### Install Libraries
```console
$ pip install numpy
```

# File structure overview:

There are 4 separate folders that will contain the necessary files for this assignment. 

The folder labelled as "Code" contains all of the python files that will be needed for this assignment as well as the graphs created for the extenison 2 performance modelling and any other files made for an extension. All of the code written for this project can be accessed in this directory.

The folder labelled as "Documents" contains all of the written documents used for this assignment which are the documentation pdf and group contribution pdf. 

The folder named "Input_Files" contains all of the text input files used for computing the best possible combinations of activities. There are several files used that vary in size and can be used for testing the algorithms to see how they perform on files of different sizes. 

The folder called "Presentation" holds the powerpoint presentation for our group. This will be used when we present our project. 


