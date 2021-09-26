from datetime import date, timedelta

class Student:
    """A Student class as base for method testing"""

    def __init__(self, first_name, last_name):
        # Prepend the first_name, last_name etc. properties with an underscore 
        # if you want them to be read-only fields so it will signify its 
        # usage (i.e read-only) to other developers.
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False  # initial value set to false


        # METHOD TO RETURN A STUDENT'S FULL NAME.
    #  We’ll add the '@property decorator' to our 'full_name'
    #  method since it's a method to get data only (i.e read-only).
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}" 

        # METHOD TO SET THE VALUE OF THE 'naughty_list' 
        # PROPERTY TO True. 
    def alert_santa(self):
        self.naughty_list = True


    # METHOD THAT WILL RETURN A STUDENT'S EMAIL ADDRESS. IT'LL TAKE A 
    # STUDENT'S FIRST NAME & LAST NAME, PUT A DOT IN THEIR MIDDLE & 
    # ATTACH '@email.com' AT THE END.
    #  We’ll add the '@property decorator' to our 'full_name'
    #  method since it's a method to get data only (i.e read-only).
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com" 
   