import inspect

class Component:
    func = None
    res = []

    num_params = 0

    arg_names = []
    params = {}

    index = 0

    def __init__(self, func):
        self.func = func
        self.num_params = inspect.getargspec( func )
        self.arg_names = inspect.getfullargspec( func )[0]

    def populateParam( self, value ) -> bool:
        temp = { self.arg_names[ self.index ] :  value }
        if len( self.params ) == 0:
            self.params = temp
        else:
            self.params.update( temp )
        self.index += 1

        return len( self.params ) == len( self.arg_names )

    def populateParams( self, values : dict ) -> bool:
        self.params = values
        
    def run(self):
        return self.func(**self.params)
