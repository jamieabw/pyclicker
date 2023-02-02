try:
    import tkinter as tk
    import pyautogui as auto
    import time
except ImportError:
    print("PLEASE INSTALL TKINTER, PYAUTOGUI AND TIME BEFORE RUNNING THIS PROGRAM.")
    input()
    quit(-1)

def autoclick(clicks, amount):
    for i in range(clicks):
        time.sleep(amount)
        auto.click()

def main():
    root = tk.Tk()
    root.geometry("250x150")
    root.title("AUTOCLICKER")
    label1 = tk.Label(root, text="ENTER AMOUNT OF CLICKS")
    label2 = tk.Label(root, text="ENTER AMOUNT OF TIME BETWEEN CLICKS")
    enter_clicks = tk.Entry(root)
    enter_time = tk.Entry(root)
    confirm = tk.Button(root, text="AUTOCLICK", command=lambda : autoclick(int(enter_clicks.get()), float(enter_time.get())))
    label1.pack()
    enter_clicks.pack()
    label2.pack()
    enter_time.pack()
    confirm.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
