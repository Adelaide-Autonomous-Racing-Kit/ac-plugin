from multiprocessing.connection import Listener
from threading import Thread

import ac

ADDRESS = "localhost"
PORT = 6337


class AARCServer:
    """
    Socket server that listens for client requests
    """

    def __init__(self):
        self.listener = Listener((ADDRESS, PORT))
        self.is_running = True

    def send_state(self, connection):
        is_connected = True
        while is_connected:
            read = connection.recv_bytes()
            if read.decode("utf-8") == "reset_car":
                ac.ext_resetCar()

    def run(self):
        while self.is_running:
            connection = self.listener.accept()
            worker = Thread(target=self.send_state, args=[connection], daemon=True)
            worker.start()

    def start(self):
        self._server_thread = Thread(target=self.run, daemon=True)
        self._server_thread.start()
