# python-mongo

## Gereksinimler
apt install python3
apt install python3-pip
pip install pymongo

## mongocli
use admin

db.createUser({
    user: "admin",
    pwd: "admin",
    roles: ["readWrite", "dbAdmin"]
})

use demo;

db.users.insert({ Name: "Selim", Department: "OSS", Code: 100 })

db.users.insertMany([
    { Name: "Enes", Department: "HR", Code: 200 },
    { Name: "Leyla", Department: "HR", Code: 300 },
    { Name: "David", Department: "SE", Code: 400 }
])

db.users.find({})

db.users.updateOne(
    { Name: "Leyla" },
    { $set: { Code: 700 } }
)

db.users.find({Name: "Leyla"})

---

db.users.updateOne(     { Name: "Leyla" },     { $set: { Code: 700 } } )

db.users.find({})

---

use demo

db.users.deleteOne({ "_id": ObjectId("") })

db.users.drop()

db.dropDatabase()