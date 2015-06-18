class DBObject:
    def __init__(self):
        self.__id = None

    def set_id(self, id):
        if isinstance(id, str):
            self.__id = id
        else:
            raise TypeError("DBObject's id should be a string")

    def is_id_set(self):
        return self.__id is not None

    def get_id(self):
        return self.__id

    def get_as_map(self):
        if self.is_id_set():
            return {"id": self.get_id()}
        return {}
