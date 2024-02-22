import pickle


def storage_save_file(self):
    stor = {"id": self.__id, "data": self.data}
    try:
        with open(self.path, "wb") as fh:
            pickle.dump(stor, fh)
    except Exception as err:
        raise err


def storage_load_file(self):
    try:
        with open(self.path, "rb") as fh:
            response = pickle.load(fh)
            self.stor = response
    except Exception as err:
        print("!!!Error load. Save New structore")
        self.stor["id"] = 0
        self.save()


# def __storage_load_file__(storage):
#     filename = storage["path"]
#     try:
#         with open(filename, "rb") as fh:
#             unpacked = pickle.load(fh)
#             storage["data"].data = unpacked["stor"]
#             storage["data"].id = unpacked["id"]
#     except Exception as err:
#         raise err
#     return storage


# def __storage_save_file__(storage, id=None):
#     filename = storage["path"]
#     # stor = {"id": storage["id"], "stor": storage["data"]}
#     stor = {}
#     with open(filename, "wb") as fh:
#         pickle.dump(stor, fh)
#         # print(f"Book saved {storage.__name__}!")
