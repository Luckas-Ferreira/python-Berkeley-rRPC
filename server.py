from concurrent import futures
import grpc
import time
import chat_pb2 as chat
import chat_pb2_grpc as rpc
from datetime import datetime

class ChatServer(rpc.ChatServerServicer):
    def __init__(self):
        self.chats = []
        self.time_difference = []

    def ChatStream(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

    def SendNote(self, request: chat.Note, context):
        timestamp = datetime.fromtimestamp(request.timestamp + 60).strftime('%Y-%m-%d %H:%M:%S')
        print("[{}] {}: {}".format(request.name, request.message, timestamp))
        self.chats.append(request)
        return chat.Empty()



    def SyncTime(self, request, context):
        server_time = time.time()
        time_difference = server_time - request.client_time
        corrected_time = server_time + time_difference
        return chat.TimeResponse(server_time=corrected_time)

if __name__ == '__main__':
    port = 11912
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        time.sleep(64 * 64 * 100)
