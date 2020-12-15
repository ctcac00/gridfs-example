#!/usr/bin/env python
from pymongo import MongoClient
import gridfs

mongodb_uri = "mongodb://localhost:27017"
print("-----------------------------")
print("Connecting to MongoDB at uri %s") % (mongodb_uri)
print("-----------------------------")

# We start by creating a GridFS instance to use
db = MongoClient(mongodb_uri).gridfs_example
fs = gridfs.GridFS(db)

# The simplest way to work with gridfs is to use its key/value interface (the put() and get() methods)
# To write data to GridFS, use put()
print("-----------------------------")
print("Writing file to GridFS")
print("-----------------------------")
a = fs.put(b"hello world")

# put() creates a new file in GridFS, and returns the value of the file document's "_id" key
# Given that "_id" we can use get() to get back the contents of the file
print("-----------------------------")
print("Reading file from GridFS")
print("-----------------------------")
print("file content - %s") % fs.get(a).read()

# get() returns a file-like object, so we get the file's contents by calling read()
# In addition to putting a str as a GridFS file, we can also put any file-like object (an object with a read() method)
# GridFS will handle reading the file in chunk-sized segments automatically
# We can also add additional attributes to the file as keyword arguments
print("-----------------------------")
print("Writing a new file to GridFS with some metadata")
print("-----------------------------")
b = fs.put(fs.get(a), filename="foo", bar="baz")

print("-----------------------------")
print("Getting the new file from GridFS")
print("-----------------------------")
out = fs.get(b)
print("File content - %s") % out.read()

print("File metadata:")

print("Filename = %s") % out.filename
print("Bar = %s") % out.bar
print("Upload date = %s") % out.upload_date

# The attributes we set in put() are stored in the file document, and retrievable after calling get()
# Some attributes (like "filename") are special and are defined in the GridFS specification - see that document for more details.