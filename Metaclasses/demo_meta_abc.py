from abc import ABC, ABCMeta, abstractmethod

class FileManagerABC(ABC):
    @abstractmethod
    def read_file(self):
        pass

print(FileManagerABC)
print(FileManagerABC.mro())
print(type(FileManagerABC))

class FileManager(FileManagerABC):
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        print("read file", self.filename)


if __name__ == "__main__":
    print(FileManager('name'))