#-------------------------------------------------------------------------------
# HA4
# Student Name: David Ahlstrom
# Python version: 3.7.8 
# Submission Date: 11/05/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Slides and example code
#-------------------------------------------------------------------------------
# Notes to grader: N/A
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

from tkinter import *
from david_ahlstrom_HA4_class import InvalidCourse, InvalidLevel, InvalidInstructor,CourseList, Course, Online, InPerson

class MyFrame(Frame):

    #init method
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.data = StringVar(self, '-')
        self.create_components()

    #clears the previous frame
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Create GUI components 
    def create_components(self):
        self.clear_frame() 

        #Welcome label
        self.welcome_label = Label(self, text = 'Welcome')
        self.welcome_label.grid(row=0,column=0)

        #Search by title button
        self.title_btn = Button(self, text = 'Search by Title', command = self.title_btn_click) #by title
        self.title_btn.grid(row=1,column=0)

        #Search by instructor button
        self.instructor_btn = Button(self, text = 'Search by Instructor', command = self.instructor_btn_click) #by title
        self.instructor_btn.grid(row=2,column=0)

        #Search by level button
        self.level_btn = Button(self, text = 'Search by Level', command = self.level_btn_click) #by title
        self.level_btn.grid(row=3,column=0)        

    def title_btn_click(self):
        self.clear_frame()

        #Label for title text entry
        self.title_label = Label(self, text = 'Enter title: ')
        self.title_label.grid(row=0, column = 0)

        #Title text entry space
        self.title_entry = Entry(self)
        self.title_entry.grid(row = 0, column = 1)

        #Next button to return results
        self.button_next = Button(self, text = "Next", command = self.title_next_handler)
        self.button_next.grid(row=1,column=0)

        #Main menu button to bring user to main menu
        self.button_mm = Button(self, text = "Main Menu", command = self.create_components)
        self.button_mm.grid(row=1,column=1)

        #set the self.data to empty string clear the previous search results
        self.data = StringVar(self, '')

        #Returns search results
        self.title_info_label = Label(self, textvariable = self.data)
        self.title_info_label.grid(row = 4, column = 0, columnspan = 2)

        #Label to denote where search results will occur
        self.results_label = Label(self, text = 'Search results appear below:')
        self.results_label.grid(row=2,column=1)
          
    def instructor_btn_click(self):
        self.clear_frame()

        #Label for instructor text entry
        self.instructor_label = Label(self, text = 'Enter Instructor Name: ')
        self.instructor_label.grid(row=0,column=0)

        #Instructor text entry space    
        self.instructor_entry = Entry(self)
        self.instructor_entry.grid(row = 0, column = 1)

        #Next button to return results
        self.button_next = Button(self, text = "Next", command = self.instructor_next_handler)
        self.button_next.grid(row=1,column=0)

        #Main menu button to bring user to main menu
        self.button_mm = Button(self, text = "Main Menu", command = self.create_components)
        self.button_mm.grid(row=1,column=1)

        #set the self.data to empty string clear the previous search results
        self.data = StringVar(self, '')

        #Returns search results
        self.instructor_info_label = Label(self, textvariable = self.data)
        self.instructor_info_label.grid(row = 4, column = 0, columnspan = 2)

        #Label to denote where search results will occur
        self.results_label = Label(self, text = 'Search results appear below:')
        self.results_label.grid(row=2,column=1)

    def level_btn_click(self):
        self.clear_frame()

        #Label for level text entry
        self.level_label = Label(self, text = 'Enter level: ')
        self.level_label.grid(row=0,column=0)

        #Level text entry space 
        self.level_entry = Entry(self)
        self.level_entry.grid(row = 0, column = 1)

        #Next button to return results
        self.button_next = Button(self, text = "Next", command = self.level_next_handler)
        self.button_next.grid(row=1,column=0)

        #Main menu button to bring user to main menu
        self.button_mm = Button(self, text = "Main Menu", command = self.create_components)
        self.button_mm.grid(row=1,column=1)

        #set the self.data to empty string clear the previous search results
        self.data = StringVar(self, '')

        #Returns search results
        self.level_info_label = Label(self, textvariable = self.data)
        self.level_info_label.grid(row = 4, column = 0, columnspan = 2)

        #Label to denote where search results will occur
        self.results_label = Label(self, text = 'Search results appear below:')
        self.results_label.grid(row=2,column=1)

    #Title exception handler, returns matching courses if no exception occurs, otherwise displays exception
    def title_next_handler(self):
        key = self.title_entry.get()
        search_criteria = 't' 
        try:
            matching_courses = Course.all_courses.search(key, 't')
            if len(matching_courses) == 0:
                raise InvalidCourse
            else:
                for c in matching_courses:
                    self.data.set(str(c))
        except InvalidCourse as x:
            self.data.set(x) 

    #Instructor exception handler, returns matching courses if no exception occurs, otherwise displays exception
    def instructor_next_handler(self):
        key = self.instructor_entry.get() 
        search_criteria = 'i'
        try:
            matching_courses = Course.all_courses.search(key, 'i')
            if len(matching_courses) == 0:
                raise InvalidInstructor
            else:
                instructors_matched = ''
                for c in matching_courses:
                    instructors_matched += str(c)
                self.data.set(instructors_matched)
        except InvalidInstructor as x:
            self.data.set(x)

    #Level exception handler, returns matching courses if no exception occurs, otherwise displays exception
    def level_next_handler(self):
        key = self.level_entry.get() 
        search_criteria = 'l'      
        try:
            matching_courses = Course.all_courses.search(key, 'l')
            if len(matching_courses) == 0:
                raise InvalidLevel
            else:
                levels_matched = ''
                for c in matching_courses:
                    levels_matched += str(c)
                self.data.set(levels_matched)
        except InvalidLevel as x:
            self.data.set(x)

    #Did not see if we needed an exit button on the assignment guidelines, but this *would* be used to exit the program
    def exit_handler(self):
        self.root.destroy()


# Configure frame
root = Tk()
root.title("Course Options")
root.geometry("300x400")

# Create application GUI
f = MyFrame(root)
f.grid()
# Initialize application
root.mainloop()


