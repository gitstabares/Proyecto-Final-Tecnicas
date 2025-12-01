from .singleton import _Singleton

class userManager(_Singleton):
    __usersByName__ = []
    __usersByID__ = []