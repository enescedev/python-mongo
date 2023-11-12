from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('localhost', 27017)
    return client

def show_databases(client):
    db_list = client.list_database_names()
    print("Mevcut veritabanları:")
    for db in db_list:
        print(db)

def show_collections(client, db_name):
    db = client[db_name]
    collection_list = db.list_collection_names()
    print(f"Koleksiyonlar {db_name} veritabanında:")
    for col in collection_list:
        print(col)

def insert_data(client, db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]

    data = {
        "ID": int(input("ID: ")),
        "Name": input("Name: "),
        "Department": input("Department: "),
        "Code": int(input("Code: "))
    }

    result = collection.insert_one(data)
    print("Veri eklendi. Eklenen verinin ID'si:", result.inserted_id)

def delete_data(client, db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]

    criteria = {
        "Name": input("Silinecek kullanıcının adı: "),
        "Department": input("Silinecek kullanıcının departmanı: ")
    }

    result = collection.delete_one(criteria)
    if result.deleted_count == 1:
        print("Veri silindi.")
    else:
        print("Veri bulunamadı.")

def main():
    client = connect_to_mongodb()
    show_databases(client)
    
    db_name = input("Hangi veritabanı üzerinde işlem yapmak istersiniz: ")
    
    show_collections(client, db_name)
    collection_name = input("Hangi koleksiyon ile işlem yapmak istersiniz: ")
    
    operation = input("Yapmak istediğiniz işlemi seçin (veri_ekle / veri_sil): ")

    if operation == "veri_ekle":
        insert_data(client, db_name, collection_name)
    elif operation == "veri_sil":
        delete_data(client, db_name, collection_name)
    else:
        print("Geçersiz işlem.")

if __name__ == "__main__":
    main()