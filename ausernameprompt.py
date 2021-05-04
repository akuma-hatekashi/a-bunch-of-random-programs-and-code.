#!/usr/bin/env python

#get the username from a prompt (python 3)
from pip._vendor.distlib.compat import raw_input

username = raw_input("Login(note that it is caps sensitive):\n ")

#list of allowed users
user1 = ("Jack")
user2 = ("Jill")

#control that the user belongs to the list of allowed users

if username == user1:

print "Access granted"

elif username == user2:

print "Welcome to the system"

else:

print "Access denied"

Could be:

# Allowed users
allowed_users = ['Jack', 'Jill']

# Check
for u in allowed_users:
if username == u:
print("Welcome!")
else:
print("Access denied")
