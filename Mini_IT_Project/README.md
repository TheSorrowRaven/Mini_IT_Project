Description:

The following are the files that have been made so far by our group. However some of these files , stored away in the "Not in Program"
folder is not been integrated to use with the main code as of now and tend to work as a temporary import module or independantly by itself.


Copy-Paste into Command Prompt / Python Shell / Windows Powershell install Required Modules to run via Programming Software ( ex. : VSCode ) :

python -m pip install requests
python -m pip install luno_python
python -m pip install Pillow
python -m pip install matplotlib
python -m pip install tkcalendar
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


Note to run : Run the whole program via Main.py


COMPILATION GUIDE:

1. Shift + Right Click in this folder and click on the "Open Powershell window here" option.
2. Run the following two commands:
       
       -> pip -m install pyinstaller  ( If pyinstaller is not installed )
       -> pyinstaller --onefile -w main.py

3. Move compiled Main.exe from the newly created "dist" folder to this main folder.

NOTE THAT RUNNING MAIN.PY THROUGH PYTHON IDLE CAN'T RUN TKINTER PROPERLY

FILE STARTING WITH F ( stored away in Not in Program folder ) IS FLAGGED FOR NOT INCLUDED IN MAIN PROGRAM
ALL FILES HAS BEEN LOWER-CASED RENAMED