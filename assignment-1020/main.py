#Read  sensitive information from environment variable.
import os

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")

print("USERNAME:",username)
print("PASSWORD:",password)
print("API_KEY:",api_key)