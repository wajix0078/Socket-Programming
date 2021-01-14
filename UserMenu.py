from user import User
import json


def user_menu(conn,address):

    from MainMenu import main_menu

    user_menu = ''' User Menu
               1. Add User
               2. View User
               3. Search User
               4. Back to Main Menu 
               '''
    # which_menu = "user"
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        try:
            conn.send(bytes(user_menu, 'utf-8'))
            # conn.send(bytes(which_menu, 'utf-8'))
            data = conn.recv(1024).decode()

            if data.lower().strip() == "1":
                data = "Adding User to the System:"
                conn.send(data.encode())
                data = conn.recv(1024)
                data = json.loads(data.decode())
                new_data = data["Add"]
                f1 = User(new_data['Name'], new_data['Cell Number'], new_data['Email'], new_data['Type'],
                               new_data['Address'])
                f1.file_handling(f1.data_dict())
                notify = json.dumps(f1.Details())
                conn.send(notify.encode())
                print(data["Add"])

            elif data.lower().strip() == "2":
                # data = "All the furniture in the System:"
                # conn.send(data.encode())
                f1 = User()
                data = f1.view_users()
                data = json.dumps(data)
                conn.send(data.encode())

            elif data.lower().strip() == "3":
                data = "Provide Id of furniture:"
                conn.send(data.encode())
                client_data = conn.recv(1024)
                f1 = Furniture()
                data = f1.search_user(client_data.decode())
                data = json.dumps(data)
                conn.send(data.encode())

            elif data.lower().strip() == "4":
                data = "Moving to Main Menu:\n"
                conn.send(data.encode())
                main_menu(conn, address)

            # elif data.lower().strip() == "exit" or data.lower().strip() == "4":
            #     user_menu(conn=conn, address=address)
            #     break

            elif data.lower().strip() == "":
                print("data recieved")
                data = "Wrong choice...Try again with mentioned choice"
                conn.send(data.encode())
                continue
        except ConnectionAbortedError:
            print("Client Exited")
            break








