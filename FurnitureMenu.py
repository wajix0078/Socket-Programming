import json


def furniture_menu(conn,address):
    from MainMenu import main_menu
    furniture_menu = ''' Furniture Managment System
               1. Add Furniture 
               2. View Furniture
               3. Search Furiture
               4. Back to Main Menu 
               '''

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        try:
            conn.send(bytes(furniture_menu, 'utf-8'))
            data = conn.recv(1024).decode()

            if data.lower().strip() == "1":
                data = "Adding Furniture to the System:"
                conn.send(data.encode())
                data = conn.recv(1024)
                data = json.loads(data.decode())
                new_data = data["Add"]
                f1 = Furniture(new_data['Name'], new_data['Type'], new_data['Category'], new_data['WoodType'],
                               new_data['Color'], new_data['Size'])
                f1.file_handling(f1.data_dict())
                notify = json.dumps(f1.Details())
                conn.send(notify.encode())
                print(data["Add"])

            elif data.lower().strip() == "2":
                # data = "All the furniture in the System:"
                # conn.send(data.encode())
                f1 = Furniture()
                data = f1.view_furniture()
                data = json.dumps(data)
                conn.send(data.encode())

            elif data.lower().strip() == "3":
                data = "Provide Id of furniture:"
                conn.send(data.encode())
                client_data = conn.recv(1024)
                f1 = Furniture()
                data = f1.search_furniture(client_data.decode())
                data = json.dumps(data)
                conn.send(data.encode())


            # elif data.lower().strip() == "exit" or data.lower().strip() == "4":
            #     main_menu(conn=conn, address=address)
            #     break

            elif data.lower().strip() == "":
                print("data recieved")
                data = "Wrong choice...Try again with mentioned choice"
                conn.send(data.encode())
                continue
        except ConnectionAbortedError:
            print("Client Exited")
            break


    conn.close()
