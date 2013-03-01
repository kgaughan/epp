import asyncore


class MuxRequestHandler(asyncore.dispatcher_with_send):
    """
    Manages a 
    """

    def handle_read(self):



class MuxServer(asyncore.dispatcher):
    """
    """

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            MuxRequestHandler(sock)
