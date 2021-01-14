from FurnitureMenu import furniture_menu
from UserMenu import user_menu

def main_menu(conn, address):
    main_menu = ''' Welcome to Furniture Management System
                Where do you want to go ?
                1. Furniture Menu
                2. User Menu
                3. Customized Furniture Menu
                4. Exit
                '''
    which_menu = "main"
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        try:
            conn.send(bytes(main_menu, 'utf-8'))
            # conn.send(bytes(which_menu, 'utf-8'))
            data = conn.recv(1024).decode()
            if data.lower().strip() == "1":
                data = "Moving to Furniture Menu:\n"
                conn.send(data.encode())
                furniture_menu(conn,address)

            elif data.lower().strip() == "2":
                data = "Moving to User Menu:\n"
                conn.send(data.encode())
                user_menu(conn,address)

            elif data.lower().strip() == "3":
                data = "Moving to Customizedd Menu:\n"
                # conn.send(data.encode())
                # furniture_menu(conn, address)

        except:
            print("Client exited")
            break