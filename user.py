import shortuuid

class User():
    def __init__(self,Name=None,cellNumber=None,email=None, type=None, address=None):
        self.userID = shortuuid.ShortUUID().random(length=10)
        self.Name = Name
        self.cellNumber = cellNumber
        self.email = email
        self.type = type
        self.address = address

    def data_dict(self):
        return {"id": self.userID, "Name": self.Name, "Cell Number": self.cellNumber, "Email" : self.email, "Type" : self.type, "Address" : self.address}

    def file_handling(self,dict):
        with open("UserData.txt", "a") as f:
            for i, a in dict.items():
                print(i)
                if i == "Address":
                    f.write(str(a) + "\n")
                else:
                    f.write(str(a) + ",")
            f.close()

    def Details(self):
        return ("here are your details",self.data_dict())

    def view_users(self):
        with open("UserData.txt", "r") as f:
            all_file = f.readlines()
            f.close()
        return all_file

    def search_user(self,id):
        with open("UserData.txt", "r") as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print(last_line)
            iter = len(lines) - 1
            while True:
                index = 0
                curr_list = lines[index]
                print(iter)
                index = index + 1

                if id in curr_list:
                    return curr_list
                    break
                elif iter == index:
                    return "No match found"

if __name__ == '__main__':
    print("Helllo World")
    user1 = User("Noma","this")
    # user1.file_handling(user1.data_dict())
    print(user1.search_user("Dbz7ptwpqF"))