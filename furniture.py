#(Entity Furniture)
import shortuuid

class Furniture():
    def __init__(self, name="None", type="basic", category="None", wood_type="None", color="None", size="None"):
        self.id = shortuuid.ShortUUID().random(length=10)
        self.type = type
        self.category = category
        self.name = name
        self.wood_type = wood_type
        self.color = color
        self.size = size

    def Details(self):
        return ("here are your details",self.data_dict())

    def data_dict(self):
        return {"id": self.id, "Name": self.name, "Type": self.type, "Category": self.category, "WoodType": self.wood_type, "Color": self.color, "Size": self.size}

    def file_handling(self,dict):
        with open("myfile.txt", "a") as f:
            for i, a in dict.items():
                print(i)
                if i == "Size":
                    f.write(str(a) + "\n")
                else:
                    f.write(str(a) + ",")
            f.close()

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



if __name__ == '__main__':
    f1 = Furniture("Pattio","Chair","Beach Pattio", "Deodar", "Baige", "Large", "None")
    f1.Details()

