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
                if i == "Size":
                    f.write(str(a) + "\n")
                else:
                    f.write(str(a) + ",")
            f.close()

    def Details(self):
        return ("here are your details",self.data_dict())

    def view_furniture(self):
        with open("myfile.txt", "r") as f:
            all_file = f.readlines()
            f.close()

        return all_file

    def search_furniture(self,id):
        flag = True
        with open("myfile.txt", "r") as f:
            lines = f.read().splitlines()
            last_line= lines[-1]
            iter = len(lines)-1
            while flag == True:
                curr_list = lines[iter]
                # print(curr_list)
                iter = iter - 1
                if id in curr_list:
                    print("if")
                    return curr_list
                    break
                elif curr_list == last_line:
                    print("elif")
                    return "No match found"

if __name__ == "main":
    print("Helllo World")
    user1 = User("Noma","this")
    print(user1.data_dict)