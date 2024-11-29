from pymongo import MongoClient

# MongoDB configuration
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "ETracking"

def get_database():
    """Connect to MongoDB and return the database instance."""
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]
