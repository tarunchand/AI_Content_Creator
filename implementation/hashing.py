import hashlib
from interfaces.hash import Hash


class MD5(Hash):
    def __int__(self):
        pass

    def hash(self, data):
        return hashlib.md5(data.encode()).hexdigest()
