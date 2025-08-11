from multiprocessing import shared_memory

#ids={}

class connect:
    class mainToModuleConnector:
        def __init__(self):
            self._ids = {'id':'idhere'}
            #pass

        def receive(self, id):
            return shared_memory.SharedMemory(name=self._ids[id].name)

        def createConnection(self,id):
            self._ids[id]=shared_memory.SharedMemory(create=True, size=1024)

        def addData(self, id, data):
            self._ids[id].buf[:len(data)] = data
   
class tools:
    class logger:
        @staticmethod
        def log(message):
            print(f"[LOG] {message}")

        @staticmethod
        def error(message):
            print(f"[ERROR] {message}")

        @staticmethod
        def info(message):
            print(f"[INFO] {message}")
            
    class changeData:
        variables={'testvar1': 'value1', 'testvar2': 'value2'}

def main():
    pass