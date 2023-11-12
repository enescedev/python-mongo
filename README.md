# python-mongo

use admin

db.createUser({
    user: "admin",
    pwd: "admin",
    roles: ["readWrite", "dbAdmin"]
})

use demo;

#Tek bir belge ekleme komutunun yapısı ve örnekleri. Örnek: 
db.users.insert({ id: 0, name: "Selim", department: "OSS", code: 200 })

db.users.insertMany([
    { id: 1, name: "Enes", department: "HR", code: 200 },
    { id: 2, name: "Leyla", department: "HR", code: 200 },
    { id: 3, name: "David", department: "SE", code: 200 }
])

db.users.find({})

db.users.updateOne([
		{ name: "Enes"},
		{
			$set: { department: "OSS" }	
		}
])

db.users.updateOne(
    { Name: "Leyla" },
    { $set: { Code: 700 } }
)

db.users.find({name: "Leyla"})

----

> db.users.updateOne(     { name: "Leyla" },     { $set: { code: 700 } } )
{ "acknowledged" : true, "matchedCount" : 0, "modifiedCount" : 0 }
> db.inventory.find({})
{ "_id" : ObjectId("65512c37155fb940a97a7c90"), "id" : 0, "name" : "Selim", "department" : "OSS", "code" : 200 }
{ "_id" : ObjectId("65512c4a155fb940a97a7c91"), "id" : 1, "name" : "Enes", "department" : "HR", "code" : 200 }
{ "_id" : ObjectId("65512c4a155fb940a97a7c92"), "id" : 2, "name" : "Leyla", "department" : "HR", "code" : 200 }
{ "_id" : ObjectId("65512c4a155fb940a97a7c93"), "id" : 3, "name" : "David", "department" : "SE", "code" : 200 }
>