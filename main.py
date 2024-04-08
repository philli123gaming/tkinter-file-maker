def generate_python_script(file_name, python_code = """
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry("600x800")
window.title("Empty template used")

window.mainloop()
    """):


    with open(file_name, 'w') as f:
        f.write(python_code)

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

#

def main():
    while True:
        print("1. Load existing config file")
        print("2. Create a new config file")
        print("3. Create a quick tkinter file")
        print("4. Exit")

        choice = input("Enter your choice: ")

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
            generate_python_script(file_name=input("what would you like to name the new file\n") + ".py")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

