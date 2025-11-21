
import sys

if len(sys.argv) > 1:
    email = sys.argv[1:] 
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    email = ["horkerikavya@gmail.com"]
    print("Email address:",email)