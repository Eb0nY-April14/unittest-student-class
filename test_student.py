import unittest
# This will import the class we created in 'student.py' file named 
# 'Student' into our test file i.e test_student.py file.
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    # Adding the @classmethod decorator to a method & passing ‘cls’ as a 
    # method parameter will make it a class method which acts on the class 
    # instead of an instance of the class. This class method will be run 
    # just once unlike the 'setUp' & 'tearDown' methods that runs at every 
    # instance of the class.
    @classmethod
    def setUpClass(cls):
        print('setUpClass')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    # Since most of our tests use the student instance which brings about 
    # code repition & violates the DRY principle. To prevent this, we'll 
    # create a 'setUp' function. Unittest gives us two methods that will 
    # be run at the start & end of each test method. They are called 'setUp' 
    # & 'TearDown' respectively & are optional. They are used to set up and 
    # teardown/destroy a testing environment for each test method. 
    # This setUp() function will be used to create the instance of the Student
    # class called 'student' so we no longer need to repeat creating the instance  
    # for every test.    
    # NOTE: These methods must be defined using camel case instead of the conve-
    # ntional snake case used in Python or else it won't run.
    # The 'setUp' method can be used to create temporary files and folders or set up  
    # a database connection during tests.
    # THE setUp() METHOD MUST RUN BEFORE EACH TEST METHOD  
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')


    # The 'tearDown' method would be used to remove temporary files or folders or close 
    # a connection to a database.
    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        # Here, we asserted that the full_name method returns the correctly 
        # formatted student name.
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')  


    # We'll use self.assertTrue to test whether student.naughty_list is True. 
    # NOTE: We don’t pass a 2nd argument to 'assertTrue' as it’s not comparing 
    # 2 values but simply checking whether an expression or value is True.
    # The 'test_alert_santa()' method below will test the behaviour of a method 
    # called 'alert_santa()' to check if it will set/change the value of the 
    # naughty_list property from False to True when called.  
    def test_alert_santa(self): 
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list) 


    def test_apply_extension(self):
        # current value of end date is stored in old_end_date variable
        old_end_date = self.student.end_date 
        # We'll call the apply_extention method on student and pass in 
        # an argument of 5 for the number of days required.
        self.student.apply_extension(5)
 
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5)) 
        # We can use assertNotEqual too as shown on the next line below:
        # self.assertNotEqual(self.student.end_date , self.student.end_date + timedelta(days=5))


    # We’ll use a context manager for our test method. we want to mock a get request in the student module,  
    # so we can write with patch(‘student.requests.get’) as mocked_get: to set our context manager.   
    # This creates an object called ‘mocked_get’ which we can use to test the 'get request' functionality.
    def test_course_schedule_success(self):
        # NOTE: Since we imported the student class at the top of this file, we have to use 
        # 'student.requests.get' to access it.
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            # Store the student’s course schedule in a variable called schedule. It holds 
            # the returned response text for a successful call.
            schedule = self.student.course_schedule()
            # We'll use assertEqual to compare the variable “schedule” which holds the returned 
            # response text for a successful call i.e the string “Success”.
            self.assertEqual(schedule, "Success")


    def test_course_schedule_failed(self):
        # NOTE: Since we imported the student class at the top of this file, we have to use 
        # 'student.requests.get' to access it.
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            # mocked_get.return_value.text = "Something went wrong with the request!"

            # Store the student’s course schedule in a variable called schedule. It holds 
            # the returned response text for a successful call.
            schedule = self.student.course_schedule()
            # We'll use assertEqual to compare the variable “schedule” which holds the returned 
            # response text for a successful call i.e the string “Success”.
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == '__main__':
    unittest.main()    