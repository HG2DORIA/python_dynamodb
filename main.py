import boto3

def get_db_table():
    dynamodb_resource = boto3.resource("dynamodb")

    return dynamodb_resource.table("academia")

def register_account(user_email: str, user_name: str) -> dict:
    dynamodb_table = get_db_table()

    response = ddb_table.put_item(
        Item={
            "PK": user_email,
            "SK": "PROFILE#",
            "name": user_name,
        }
    )
       
    

    return response


