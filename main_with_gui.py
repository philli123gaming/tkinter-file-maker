import sys
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from tkinter import filedialog
import os

def generate_python_script(python_code2=""""""):
    python_code1 = """
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
    """


    root = tk.Tk()
    root.withdraw()  # Hide the root window
    # Set the root window to be always on top
    root.attributes('-topmost', True)

    file_path = filedialog.asksaveasfilename(initialdir="D:/users/Philli123gaming/Documents/code/Github/tkinter practise",
                                             defaultextension=".py",
                                             filetypes=[("Python Files", "*.py"), ("All files", "*.*")])

    print("File path selected:", file_path)
    if file_path:
        # Extract the file name from the file path
        file_name = file_path.split("/")[-1]  # Assuming '/' is the path separator
        file_name = os.path.splitext(file_name)[0]
    python_code3 = f"""
window = tk.Tk()
window.geometry("600x800")
window.title("{"Empty template used" if not file_name else file_name}")

window.mainloop()
"""
    python_code = python_code1 + python_code2 + python_code3
    with open(file_path, 'w') as f:
        f.write(python_code)
    print(f"Tasks saved as {file_name} to: {file_path}")

def load_config():
    print("Loading existing config file...")

def create_config():
    print("Creating a new config file...")
# Generate Python script and save it to a file

def add_widget():
    available_widgets = ["label", "button", "text", "entry", "checkbox", "radio", "frame"]
    print(f"Avaliable Widgets:")
    for index, widget_choice in enumerate(available_widgets, start=1):
        print(f"{index}. {widget_choice}")
    choice = input("please choose a widget to add\n")
    if choice == '1':
        newlabel = []
        while True:
            is_window = input("Is the master a window? (yes/no): ").strip().lower()
            if is_window == "yes":
                newlabel.append("master = window")
                break
            elif is_window == "no":
                print("Master is not a window.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    elif choice == '2':
        pass


def view_widgets():
    print("Viewing widgets...")

def edit_widgets():
    print("Editing widgets...")

def reorder_widgets():
    print("Reordering widgets...")

def bind_events():
    print("Binding events to widgets...")

def save_config():
    print("Saving configuration...")

def exit():
    sys.exit()

def main():
    while False:
        if choice == '1':
            load_config()
        elif choice == '2':
            python_code = ""
            while True:
                print("Widget Menu:")
                print("1. Add a widget")
                print("2. View widgets")
                print("3. Edit widgets")
                print("4. Reorder widgets")
                print("5. Bind events to widgets")
                print("6. Save configuration")
                print("7. Back to main menu")

                choice = input("Enter your choice: ")

                if choice == '1':
                    add_widget()
                elif choice == '2':
                    view_widgets()
                elif choice == '3':
                    edit_widgets()
                elif choice == '4':
                    reorder_widgets()
                elif choice == '5':
                    bind_events()
                elif choice == '6':
                    save_config()
                elif choice == '7':
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            generate_python_script()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    window = tk.Tk()
    main_menu = Frame(window)
    main_menu.grid(row=0, column=0, sticky="nsew")
    widget_menu = Frame(window)
    widget_menu.grid(row=0, column=0, sticky="nsew")

    button1 = Button(main_menu, command=load_config)
    button1.pack()
    button2 = Button(main_menu,text="Create new script", command=widget_menu.tkraise)
    button2.pack()
    button3 = Button(main_menu, text="Create a quick tkinter file", command=generate_python_script)
    button3.pack()
    button4 = Button(main_menu,text="Exit",command=exit)
    button4.pack()


    widget_menu_label = Label(widget_menu, text="Widget Menu")
    widget_menu_label.pack()
    button5 = Button(widget_menu)
    button5.pack()
    button6 = Button(widget_menu)
    button6.pack()
    button7 = Button(widget_menu)
    button7.pack()
    button8 = Button(widget_menu)
    button8.pack()
    button9 = Button(widget_menu)
    button9.pack()
    button10 = Button(widget_menu)
    button10.pack()
    button11 = Button(widget_menu,text="Back to main menu", command=main_menu.tkraise)
    button11.pack()
    button12 = Button(widget_menu,text="Exit",command=exit)
    button12.pack()

    main_menu.tkraise()
    window.mainloop()
if __name__ == "__main__":
    main()
