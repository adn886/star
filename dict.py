x =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"brown"
}

print(x["brand"])
x["son"]="jem"
print(x.get("color"))
print(x["year"])
print(x)
for a in x:
    print(a)  #gives keys
    print(x[a]) #gives values
print(x.popitem()) # removes random item
print(x.values())
for l,m in x.items():
    print(l,m)
if "son" in x:
    print("exists",x["son"])
else:
    print("not exists")
print(dict.fromkeys(x))
x.update({"dob":"123"})
print(x)
print(x.setdefault("dob","123"))
print("######################################### GIT::::::")
print(x.values())
print(x.keys())
