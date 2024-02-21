from contact.contact import Contact


a = {
    "first_name": "dasdakj",
    "last_name": "",
    "phones": {"1234567", "21346512"},
    # "phones": set("1234567"),
    # "phones": set(),
    "email": "",
    "address": "address init",
    "birthday": "",
}
b = {
    "first_name": "UpdateName",
    "last_name": "UpdateLastName",
    "address": "New address",
    "phones": {"1111111", "2222222", "12345678"},
}
p = {"1111111", "9999999", "7777777"}
# a = Contact({"first_name": "Aleksandr"}, 123)
aaa = Contact(a, 123)
# print(a)

print(f"a: {aaa}")
print(aaa.id)
print(f"type a.first_name: {(aaa.first_name)}")
print(f"type a.first_name: {type(aaa.first_name)}\n")
print(f"a.last_name: {aaa.last_name}")
print(f"type a.last_name: {type(aaa.last_name)}\n")
# a.first_name = "ddac dde32e23"
# print(f"type a.first_name: {(a.first_name)}")
# print(f"type a.first_name: {type(a.first_name)}\n")


# print(f"a.first_name: {a.first_name}")
# print(f"type a.first_name: {type(a.last_name)}")
print(f"a.address: {aaa.address}")
print(f"type a.address: {type(aaa.address)}")
aaa.address = "asdqwe"
print(f"a.address: {aaa.address}")
print(f"type a.address: {type(aaa.address)}")

# aaa.update(b)
aaa.update_all(b)
print("!!!!!!!------update-----")
print(f"type aaa.first_name: {(aaa.first_name)}")
print(f"type aaa.first_name: {type(aaa.first_name)}\n")
print(f"aaa.last_name: {aaa.last_name}")
print(f"type a.last_name: {type(aaa.last_name)}\n")
print(f"aaa.phones: {aaa.phones}")
print(f"type aaa.phones: {type(aaa.phones)}\n")


aaa.add_phones(p)
aaa.edit_phone("9999999", "00000000")
print(f"aaa.phones: {aaa.phones}")
aaa.del_phone("2222222")
print(f"aaa.phones: {aaa.phones}")
# print(a.id)
# a.id = 1111
# print(a.id)
