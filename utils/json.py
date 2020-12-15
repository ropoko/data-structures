import json

# JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# Deserialize x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])

# --------------------------------- = --------------------------------- #

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Serialize:
y = json.dumps(x)

# the result is a JSON string:
print(y)