class NoHelperFound(BaseException):
    pass

class ParsingError(BaseException):
    def __init__(self, line='<line not provided>', reader=None):
        if reader:
            BaseException.__init__(self,
                                   'Error at file offset %d, parsing line: %s' %
                                   (reader.tell(), line))
        else:
            BaseException.__init__(self, 'Error parsing line: %s' % line)
