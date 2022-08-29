def user_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "username": item["username"],
        "email": item["email"],
        "city": item["city"],
    }


def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]
