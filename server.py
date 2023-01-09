import xmlrpc.server

class RPCServer:

    def procedure1(self, x):
        """Accepts an integer and returns an integer"""
        result = x + 1
        return result

    def procedure2(self, x, y):
        """Accepts an integer and string and returns a floating point"""
        result = float(x) / len(y)
        return result

    def procedure3(self, x):
        """Accepts an integer and returns a string"""
        result = str(x * x)
        return result

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(RPCServer())
server.serve_forever()