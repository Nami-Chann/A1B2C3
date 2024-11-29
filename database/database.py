import pymongo
from dbconfig import DB_URI, DB_NAME

# Initialize database connection
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']
config_data = database['config']  # New collection for configuration variables

# User-related functions
async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

# Configuration variable functions
def set_variable(key: str, value):
    """Set a configuration variable in the database."""
    config_data.update_one(
        {'_id': key},
        {'$set': {'value': value}},
        upsert=True
    )

def get_variable(key: str, default=None):
    """Retrieve a configuration variable from the database."""
    entry = config_data.find_one({'_id': key})
    return entry['value'] if entry else default

# Examples for using these functions
# set_variable('ADMINS', '12345 67890')
# admins = get_variable('ADMINS', '0')
