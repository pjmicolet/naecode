from component import Component

class Engine:
    components = []
    inputParams = {}

    def __init__(self, components : list ):
        self.components = components

    def setInputParams(self, params: dict):
        self.inputParams = params

    def execute(self):
        first = True
        nextParams = []
        for func in self.components:
            if first:
                func.populateParams( self.inputParams )
                first = False
            else:
                for item in nextParams:
                    func.populateParam( item )
            nextParams = func.run()
