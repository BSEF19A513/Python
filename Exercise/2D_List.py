# 2-D List
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for items in row:
#         print(items)

# Dictionary exercise

phone = input("Phone: ")
digits_mapping = {
    "1":"One ",
    "2":"Two ",
    "3":"Three ",
    "4":"Four "
}
output = ""
for digits in phone:
    output += digits_mapping.get(digits)
print(output)