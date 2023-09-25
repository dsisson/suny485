 def is_fruit(fruit_candidate):
     """ 
     Perform a lookup for `fruit_candidate` against a list of simple
     fruit names, and return True if found, else returm False.
     
     :param fruit_candidate: str, simple fruit name
     :return: bool
     """
     fruits = ['apple', 'pear', 'bannana', 'grape']
     
     if fruit_candidate in fruits:
         return True
    else:
        return False
        