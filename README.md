# l-systems  
## Summary and features  
This is a program written in python. It's main purpose is to draw l-systems using the turtle library.  
Its features are:  
- Expanding and drawing l-systems.  
- A system history  
- Automatic backups of the system history file  
- Exporting the drawings  
  
The supported drawing operations are the followed:  
- **angle \<amount>**: Turn \<amount> degrees to the left.
- **draw \<amount>**: Draw a line of \<amount> long.
- **forward \<amount>**: Move \<amount> forward without drawing a line.
- **nop**: Do nothing.
- **push**: Push the current drawing state (angle, position, ...) on the stack.
- **pop**: Replace the current drawing state with the one on top of the stack.
- **color \<name>**: Change the color from this point to the given name.

# Usage
## Setup
To use the program on a unix based os, use the following steps:

### Cloning the repo
Clone the repo into the desired directory using the following command
```
git clone https://github.com/M-Ketels/l-systems
```

### Setting up the virtual environment
You can set up the venv using the following commands:
```
python3 -m venv lsys-venv
source lsys-venv/bin/activate
```

### Setting up pip and the used packages
Using the following commands you can install pip. After this installation you can install all the needed packages using the requirements.txt file
```
sudo apt install pip
pip install -r requirements.txt
```

## Usage of the program
To make use of the program you have to use the following command to start the main function:
```
python3 main.py
```
You will now need to enter the path of the json file that holds the l-system. Then how many iterations you wish to expand the axiom.

**NOTE:** once the main function has been called, the backup functionality will also begin. This will not stop unless specifically told using the command:
```
python3 stop_backup.py
```

### Exporting images
To export the drawn l-system, use the following command:
```
python3 main.py --export <image_name.eps>
```
This will export the drawn l-system to a given file.

### Restoring the history file to a backup
You can restore the system history using the following command:
```
python3 restore_backup.py
```
You will now be prompted with all the possible backup files like this:
```
1 backupDD-MM-YYYY_hours:min:sec
2 backupDD-MM-YYYY_hours:min:sec
3 backupDD-MM-YYYY_hours:min:sec
4 backupDD-MM-YYYY_hours:min:sec
Choose a backup to restore.
```
You can now enter any of the left numbers to choose a backup file to restore to.

## Deactivating and reactivating
First always remember to stop the backups with the command:
```
python3 stop_backup.py
```

Then you can deactivate the virtual environment using the command:
```
deactivate
```

Finally if you wish to reactivate the virtual environment, then you don't need to fully repeat the setup but only this single command:
```
source lsys-venv/bin/activate
```