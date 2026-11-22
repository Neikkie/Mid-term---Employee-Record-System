# import the required model
import tkinter as tk
from tkinter import messagebox

# global variables
employees = []
selected_index = None

# create the main window
main_window = tk.Tk()
# set the size
main_window.geometry('550x650')
# create the title
main_window.title('Employee Record System')


# application title
title_label = tk.Label(main_window, text = 'Employee Record System', font = ('Arial', 16, 'bold'),
                       relief= 'ridge', borderwidth= 3)
title_label.pack(pady=15, ipadx = 10, ipady = 5)

# employee information labels
name_label = tk.Label(main_window, text = 'Employee Name', relief= 'solid', borderwidth= 1)
name_label.pack(pady=5, ipadx = 10, ipady = 5, padx = 10)

# employee name entry
name_entry = tk.Entry(main_window, font = ('Arial', 12, 'bold'), width = 20, bg = 'white', fg = 'black', insertbackground='black', insertwidth=2)
name_entry.pack(pady=5, ipadx = 10, ipady = 5, padx = 10)
name_entry.focus_set()

# department label
department_label = tk.Label(main_window, text = 'Department', relief= 'solid', borderwidth= 1)
department_label.pack(pady=5, ipadx = 10, ipady = 5, padx = 10)

# department dropdown options
department_dropdown = ['Human Resources', 'Finance', 'Information Technology',
                       'Marketing', 'Operations']

# Storing each department using variables
department_variables = tk.StringVar()
department_variables.set('Select Department')

# create department dropdown menu
department_menu = tk.OptionMenu(main_window, department_variables, * department_dropdown)
department_menu.pack(pady=5, ipadx = 10, ipady = 5)

# employee status label
employee_status_label = tk.Label(main_window, text = 'Employee Status', relief= 'solid', borderwidth= 1)
employee_status_label.pack(pady=5, ipadx = 10, ipady = 5, padx = 10)

# check whether an employee is full time or part-time
full_time = tk.BooleanVar(value=True)
part_time = tk.BooleanVar(value=False)

# function to select full time
def select_full_time():
    if full_time.get():
        part_time.set(False)
    else:
        part_time.set(True)


# function to select full time
def select_part_time():
    if part_time.get():
        full_time.set(False)
    else:
      full_time.set(True)

# create full-time checkbutton
full_time_check = tk.Checkbutton(main_window, text = "Full Time", variable = full_time, command = select_full_time)
full_time_check.pack(pady=5)

# create part-time check button
part_time_check = tk.Checkbutton(main_window, text = "Part Time", variable = part_time, command = select_part_time)
part_time_check.pack(pady=5)

# function to validate employee information
def validate_employee_input(name_label, department_label):
    if name_label == '':
        messagebox.showerror('Error', 'Employee Name cannot be empty')
        return False

    if department_label == 'Select Department':
        messagebox.showerror('Error', 'Department cannot be empty')
        return False

    return True

# function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    department_variables.set('Select Department')
    full_time.set(True)
    part_time.set(False)
    name_entry.focus_set()

# function to display employee records
def display_employee_records():
    employee_listbox.delete(0, tk.END)

    for employee in employees:
        employee_listbox.insert(tk.END, f'{employee[0]} | {employee[1]} | {employee[2]}')

# function to add employees
def add_employee():
    global selected_index

    # retrieve employee information
    employee_name = name_entry.get().strip()
    department = department_variables.get()

    if full_time.get():
        employee_status = 'Full Time'
    else:
        employee_status = 'Part Time'

    # validate the employee information
    if not validate_employee_input(employee_name, department):
        return

    # add employees to the record
    employee = [employee_name, department, employee_status]
    employees.append(employee)

    # display the employee record
    display_employee_records()
    # clear selection the input field
    employee_listbox.selection_clear(0, tk.END)
    selected_index = None
    clear_fields()
    name_entry.focus_set()
    # success message
    messagebox.showinfo('Success', 'Employee Record Successfully Added')

# function to select employee
def select_employee(event):
    global selected_index

    selected = employee_listbox.curselection()

    if selected:
        selected_index = selected[0]
        employee = employees[selected_index]

    # display the selected employee information
        name_entry.delete(0, tk.END)
        name_entry.insert(0, employee[0])

        department_variables.set(employee[1])

        if employee[2] == 'Full Time':
            full_time.set(True)
            part_time.set(False)
        else:
            full_time.set(False)
            part_time.set(True)


# function to edit employee
def edit_employee():
    global selected_index

    if selected_index is None:
        messagebox.showerror('Error', 'Please select an employee to edit')
        return
    # retrieve the selected information
    updated_name = name_entry.get().strip()
    updated_department = department_variables.get().strip()

    if full_time.get():
        employee_status = 'Full Time'
    else:
        employee_status = 'Part Time'
    # validate the information
    if not validate_employee_input(updated_name, updated_department):
        return

    # save the updated information
    employees[selected_index] = [updated_name, updated_department, employee_status]
    # update employee listbox
    display_employee_records()

    # update the listbox fields
    employee_listbox.selection_clear(0, tk.END)
    selected_index = None
    clear_fields()

    messagebox.showinfo('Success', 'Employee Record Successfully Updated')

# function to quit application
def quit_application():
    main_window.destroy()

# create a button frame
btn_frame = tk.Frame(main_window)
btn_frame.pack(pady=10)

# add employee button
btn_employee = tk.Button(btn_frame, text = "Add Employee", command = add_employee)
btn_employee.pack(side='left',pady=5)

#button to edit employee
btn_edit_employee = tk.Button(btn_frame, text = "Edit Employee", command = edit_employee)
btn_edit_employee.pack(side='left',pady=5)

# employee record display
record_label = tk.Label(main_window, text = 'Employee Record', font = ('Arial', 13, 'bold'),
                        relief= 'groove', borderwidth= 2)
record_label.pack(pady=10, ipadx = 10, ipady = 5)

# create a list frame
list_frame = tk.Frame(main_window)
list_frame.pack(pady=5)

# employee record list box
employee_listbox = tk.Listbox(list_frame, width=50, height=5, exportselection=False)
employee_listbox.pack(side='left')

# Create a vertical list scroll bar
list_bar = tk.Scrollbar(list_frame, orient='vertical', command=employee_listbox.yview)
list_bar.pack(side='right', fill='y')

# connect to the listbox to the scrollbar
employee_listbox.config(yscrollcommand=list_bar.set)

# connect the listbox selection to the function
employee_listbox.bind('<<ListboxSelect>>', select_employee)

# button to quit the program
tk.Label(main_window, text='Ready to exit?').pack(pady=5, ipadx = 10, ipady = 5)
tk.Button(main_window, text = "Quit", command = quit_application).pack(pady=5, ipadx = 10, ipady = 5)

# output
main_window.mainloop()