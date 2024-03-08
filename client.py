import threading
import grpc
import chat_pb2 as chat
import chat_pb2_grpc as rpc
import time


address = 'localhost'
port = 11912

class Client:
    def __init__(self, username):
        self.username = username
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = rpc.ChatServerStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        self.__start_chat()

    def __listen_for_messages(self):
        for note in self.conn.ChatStream(chat.Empty()):
            print("\n[{}] {}: {}".format(time.ctime(note.timestamp), note.name, note.message)) 

    def send_message(self, message):
        if message != '':
            n = chat.Note()
            n.name = self.username
            n.message = message
            n.timestamp = int(time.time())  # Adicione esta linha
            self.conn.SendNote(n)


    def sync_time(self):
        client_time = time.time()
        response = self.conn.SyncTime(chat.TimeRequest(client_id=self.username, client_time=client_time))
        print("Tempo sincronizado: ", response.server_time)

    def __start_chat(self):
        print("Conversa iniciada. Digite 'sair' para encerrar a conversa.")
        while True:
            message = input("\n Digite sua mensagem: ")
            if message.lower() == 'sair':
                break
            self.send_message(message)

if __name__ == '__main__':
    username = input("Qual é o seu nome de usuário? ")
    client = Client(username)
