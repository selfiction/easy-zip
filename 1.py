import keyboard
from zipfile import ZipFile
def on_triggered():
    myzip = ZipFile("newzip.zip", "w")
    print ("ZIP-файл создан")
keyboard.add_hotkey('ctrl+shift', on_triggered)
print("Нажмите ESC для остановки")
keyboard.wait('esc')
print("Программа идет дальше... ")
