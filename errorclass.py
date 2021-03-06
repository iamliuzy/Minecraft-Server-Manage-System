class MSMSError(Exception):
    """description of class"""
    def __init__(self, name, code,description):
        Exception.__init__(self)
        self.name = name
        self.code = code
        self.description = description


