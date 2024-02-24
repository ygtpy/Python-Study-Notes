

import json



data = '{"firstName":"Yiğit","lastName":"x"}'

# json halindeki bir datayı json a çevirme
y = json.loads(data)

type(y)

print(y["firstName"])
print(y["lastName"])



customer = {
    "firstName":"yigit",
    "email":"yigitali@gmail.com"
    }

# bir sözlügü yada herhangi bir listeyi,ereyi, stringi json tipine donusturme
customerJson = json.dumps(customer)

print(customer)


print(json.dumps("yigit"))