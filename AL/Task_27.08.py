class Course:
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudent = m
        self.__NumberOfClasses = 0
        self.__CourseLesson = []
        self.__CourseAssessment = Assessment

    def AddLesson(self, t, d, r):
        self
