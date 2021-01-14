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

def add_user():
    name = input("User Name:")
    cell_number = input("Cell Number Type:")
    email = input("User Email:")
    type = input("User Type:")
    address = input("User Address:")

    return {
        "Add": {"Name": name, "Cell Number": cell_number, "Email": email, "Type": type, "Address": address}}


def Server_Connect(message,Objtype=None):
    iter = 0
    while message.lower().strip() != 'exit' or message.strip() != '4':

        # if iter == 0:
        #     client_socket.send(message.encode())

        client_socket.send(message.encode())
          # send message
        data = client_socket.recv(1024).decode()
        # which_menu = client_socket.recv(16).decode()# receive response
        print('Received from server: ' + data)  # show in terminal
        # print("Menu flag \n",which_menu)
        # if message.strip() == "":
        #     print("Wrong input")
        #     print("------------")
        if "user" in data.strip().lower():

            data = client_socket.recv(1024).decode()
            print(data)
            choice = input("->")

            if choice.strip() == "2":
                print("2 True")
                client_socket.send(choice.encode())
                print(json.loads(client_socket.recv(1024)))

            if choice.strip() == "3":
                # data = input("->")
                client_socket.send(choice.encode())
                print("Search Results: Here are the Details\n", json.loads(client_socket.recv(1024)))



            if choice.strip() == "1":
                add_json = json.dumps(add_user())
                client_socket.send(add_json.encode())
                # print(add_json)
                print("Data Saved:", json.loads(client_socket.recv(1024)))

        if choice.strip().lower() == "exit" or message.strip().lower() == "4" :
            client_socket.close()
            break
            # else:
            #     message = input("Press Enter to see the Menu\n")
            #     continue
            # iter = iter + 1
            message = input("-------------->Press Enter to see the Menu<--------------------")

    client_socket.close()


client_socket = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
client_socket.connect((host, port))
# print(s.recv(1024).decode('utf-8'))
# arr = input("What")  #client_preference()
# data = json.dumps({'Greet':"Hi there",'Data':arr})
# s.send(data.encode())
print("Recieved Data: ",client_socket.recv(1024).decode())
# recieved = client_socket.recv(1024).decode()
# recieved = recieved.split(" ")
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
