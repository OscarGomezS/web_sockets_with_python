from dataFinal import DataFinal
from counter import Counter

import websockets
import asyncio

class DataInitial:
    url          = str
    time         = int
    time_counter = 0
    counter      = Counter().set_counter_json()


    def __init__(self, url, time):
        self.url  = url
        self.time = time

    async def listen_server(self):
        """
        Listen the server and count the amount of loops
        """
        async with websockets.connect(self.url, ping_interval=None) as ws:
            while self.time_counter < self.time:
                msg = await ws.recv()
                self.counter += 1
                self.time_counter = self.stop_loop(self.counter)
                self.counter = DataFinal(msg).run_data_final(self.counter)
    
    def run_loop(self):
        """
        Start the loop of reciving the json files from the server
        """
        asyncio.get_event_loop().run_until_complete(self.listen_server())

    def stop_loop(self, counter):
        if counter == 60000:
            self.time_counter += 1
        return self.time_counter