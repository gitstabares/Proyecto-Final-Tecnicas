class _Singleton:
    '''
        Singleton Pattern Design. Inherit from this and use static or class methods to make a singleton
    '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(_Singleton, cls).__new__(cls)
        return cls._instance