class InvalidCourse(Exception):
    def __str__(self):
        return 'Course not found!'
    
class InvalidLevel(Exception):
    def __str__(self):
        return 'Course level not found!'

class InvalidInstructor(Exception):
    def __str__(self):
        return 'Instructor  not found!'

    

class CourseList(list):
    def search(self, key, search_criteria):
        matching_courses = []
        if search_criteria == 't': #search by title
                for course in self:
                    if key == course.title:
                        matching_courses.append(course)
        elif search_criteria == 'i': #search by instructor --> one instructor can offer multiple course
                for course in self:
                    if key == course.instructor:
                        matching_courses.append(course)
        elif search_criteria == 'l': #search by level
                for course in self:
                    if key == course.level:
                        matching_courses.append(course)
        return matching_courses
            
class Course(object):
    all_courses = CourseList()
    def __init__(self, level, course_id,title, instructor):
        self.level = level
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        Course.all_courses.append(self)

    def __str__(self):
        return 'Level #: {}\nID: {}\nTitle: {}\nInstructor: {}\n'.format(\
    	self.level, self.course_id, self.title, self.instructor)
    
class Online(Course):
    def __init__(self, level, course_id,title, instructor, location):
        super().__init__(level, course_id,title, instructor)
        self.location = location #mystery, historic
        
    def __str__(self):
        return super().__str__() + 'Location: {}\n'.format(self.location)
        
        
class InPerson(Course):
    def __init__(self, level, course_id,title, instructor, campus, location):
        super().__init__(level, course_id,title, instructor)
        self.campus = campus
        self.location = location
        
    def __str__(self):
        return super().__str__() + 'Campus: {}\nLocation: {}\n'.format(self.campus, self.location)

def main():
    
    with open('courses.txt') as f:
    #process input file and creating course objects
        for line in f:
            line =  line.strip('\n').split(',')
            level,course_id,title,instructor = line[:4]
            additional_info = line[4:]
            if 'DL' in course_id: #create an online course object
                location = additional_info[0]
                o = Online(level, course_id,title, instructor, location)
            else: #create an in-person object
                campus, location =additional_info
                p = InPerson(level, course_id,title, instructor, campus, location)
            
        
main()
            
                
            
        
    
        
        
    
