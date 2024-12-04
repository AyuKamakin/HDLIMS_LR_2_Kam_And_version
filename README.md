### HDLIMS_LR_2_Kam_And_version
## Practice in Python and OpenCV for Raspberry Pi.

Here you can get 3 programs to use your webcam, implement face detection and MobileNet with Raspberry Pi.

### Requirements
1. Raspberry Pi with more than 2 GB OS;
2. Micro SD card with 32 or more space;
3. Keyboard, mouse, monitor, webcam, GPIO button, GPIO servomotor, GPIO LED.

### Part 1. Starting with Raspberry Pi
At first, install Raspberry OS that fits for your Raspberry Pi.
In this work I used Raspberry OS 64-bit version.  
You can download it from [here](https://www.raspberrypi.com/software/).  
Install OS to Micro SD via Rufus, use guide [here](https://jes.saxe.dk/raspberrypi/easy-way-to-install-raspberry-pi-rasbian-os-via-rufus-134).  
When OS is loaded to Micro SD card, connect to Raspberry Pi your keyboard, mouse, monitor, webcam, install Micro SD into Raspberry Pi.  
When all connected, plug in power cable into Raspberry Pi. If all done correct, OS will start and you can setup and customize your OS.

### Part 2. Setting up Python environment
At first, update and upgrade your installers:   
`sudo apt-get update && sudo apt-get upgrade`

Therefore Python is to be installed, use the following command:   
`sudo apt-get install python`

After installing Python, a virtual environment is to be created and activated.   
Use `cd /needed_directory/` to move to the directory where you want to create it.  

To activate environment use the following command:   
`python<version> -m venv <virtual-environment-name>`

Example:   
`python3 -m venv myEnvironment`   

The environment is to be activated with the command:   
`source myEnvironment/bin/activate`

After activation, use the command `python` to start the Python environment.

### Part 3. Installing libraries
There are some libraries that are required.     
You can install them with using the following command:   
`pip install someLibrary`  

Libraries that are required:   
1. numpy   
2. opencv-python   
3. tensorflow   
4. keras   
5. scikit-learn

### Part 4. Webcam usage example   
Check if terminal is opened in the python environment directory, where all needed libraries   
are installed in the previous step.   

To move to needed directory use
`cd needed_directory/`

Than use following command to open environment directory in the Explorer of your file system   

`open .`

Create a python file named webcamExample.py.   

Copy into webcamExample.py contents of webcamExample.py from this repository via preferred text editor.   

Save the file.   

Use following line to start your program:   

`webcamExample.py`

To stop execution, open terminal window, where from program was started, and press CTRL+C to stop execution.

### Part 5. Creating spinning camera

Download xml file containing information for face-detection model [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)   

Move xml file to the python environment directory   

Connect your GPIO peripherals as shown in the [guide](https://ul-cad.yonote.ru/share/HLIMDS_CAD_LR_02)   

Led signal wire must be connected to BCM-numbered port 2, servomotor signal wire must be connected to BCM-numbered port 3,   
button signal wire must be connected to BCM-numbered port 4.      

Create file GPIO_main.py with the containtment of file with this name from this repository where the xml file is   

Run script via   

`GPIO_main.py`   

### Part 6. Implementing MobileNet

Do the steps of part 4, Webcam usage example, for the file 'MobileNet_implementation.py' from this repository.   

If any errors occured, check the errors for the messages of libraries installment, if some are not installed, use   

`python`   

And than use following line, where some_required_lib is to be changed to needed library name.   

`pip install some_required_lib`
