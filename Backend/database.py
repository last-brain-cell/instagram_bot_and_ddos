from model import Todo

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = collection.find_one({'title': title})
    return document
