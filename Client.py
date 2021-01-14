import socket  # Import socket module
import json


def add_fruniture():
    name = input("Furniture Name:")
    type = input("Furniture Type:")
    category = input("Furniture Category:")
    wood_type = input("Furniture Wood type:")
    color = input("Furniture color:")
    size = input("Furniture size:")

    return {
        "Add": {"Name": name, "Type": type, "Category": category, "WoodType": wood_type, "Color": color, "Size": size}}


def Server_Connect(message):
    while message.lower().strip() != 'exit' or message.strip() != '4':

        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        # if message.strip() == "":
        #     print("Wrong input")
        #     print("------------")

        if message.strip() == "2":
            data = input("->")
            client_socket.send(data.encode())
            print("Search Results: Here are the Details\n", json.loads(client_socket.recv(1024)))

        if message.strip() == "3":
            data = input("->")
            client_socket.send(data.encode())
            print("Search Results: Here are the Details\n", json.loads(client_socket.recv(1024)))

        if message.strip().lower() == "exit" or message.strip().lower() == "4" :

            client_socket.close()
            break

        if message.strip() == "1":
            add_json = json.dumps(add_fruniture())
            client_socket.send(add_json.encode())
            # print(add_json)
            print("Data Saved:", json.loads(client_socket.recv(1024)))

        # else:
        #     message = input("Press Enter to see the Menu\n")
        #     continue

        message = input("-------------->Press Enter to see the Menu<--------------------")

    client_socket.close()

if __name__  == "__main__":

    client_socket = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345  # Reserve a port for your service.
    client_socket.connect((host, port))
    # print(s.recv(1024).decode('utf-8'))
    # arr = input("What")  #client_preference()
    # data = json.dumps({'Greet':"Hi there",'Data':arr})
    # s.send(data.encode())
    print(client_socket.recv(1024).decode())
    message = input(" -> ")
    while True:
        if message.strip() in ["1", "2", "3", "4", "exit"]:
            try:
                Server_Connect(message.strip())
            except ConnectionAbortedError:
                "Host Machine(Server) Exited"

            break
        else:
            print("Try Avaliable Options")
            pass
