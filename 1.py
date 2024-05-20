import keyboard
from zipfile import ZipFile
 


def on_triggered():
    print("Ваша функция!!!")
    myzip = ZipFile("newzip.zip", "w")

keyboard.add_hotkey('ctrl+shift', on_triggered)


print("Нажмите ESC для остановки")
keyboard.wait('esc')
print("Программа идет дальше... ") # отработает после нажатия esc
