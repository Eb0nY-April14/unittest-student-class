import unittest
# This will import the class we created in 'student.py' file named 
# 'Student' into our test file i.e test_student.py file.
from student import Student


class TestStudent(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()    