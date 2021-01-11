# 
# # arr = ['a','b','c']
# #
# # for  i,a in enumerate(arr):
# #     print(i,a)
# 
# 
# arr_new  = {"this":1,"that":1}
# 
# # print(len(arr_new))
# # for key,value in arr_new.items():
# #     print(key," ",value)
# #     for i, a in enumerate(items):
# 
# from furniture import  Furniture
# f1 = Furniture("sdasd","dasdas","dasdsda","dasdsad","dasdas","dasdada")
# # # f1.Details()
# # # print(f1.data_dict())
# # # f1.file_handling(f1.data_dict())
# print(f1.search_furniture("5zXoWt8Vx"))
# # 
# print(f1.view_furniture())

# a = input("dasdsad")
# print(a=="")
# a = 0
# while True:
#     a = a+1
#     print(a)
#     if a in [4,2,3]:
#      break
# with open("myfile.txt", "r") as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     print(last_line)
#
#     curr_list = lines[len(lines)-1]
#     if last_line == curr_list :
#         print("This",curr_list)
from user import User

user1 = User("Noma","abc@gmail.com","0900078601")
print(user1.data_dict())
user1.file_handling(user1.data_dict())
user1.Details()






