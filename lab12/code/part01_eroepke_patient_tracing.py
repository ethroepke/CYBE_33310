# Lab 12 
# Using Private Set Intersection (PSI) subfield
# of Multi-Party Computation (MPC)
#
# This program will read in the movement data on an individual
# who has contracted COVID-19.  You will compare those
# hashes to see if you have come in contact with the individual.
# It should not reveal the individual's information, just the location
# and time you were both in the same place.
# 
# This is a very simplified version of what actually happened in 
# COVID-19 contact tracing, but it demonstrates the basic concepts.
# 
# Syntax: python3 part01_patient_tracing_skel.py 


import hashlib
import json

def hashData(data):
# We are using SHA-256 as the OPPRF 
    return hashlib.sha256(data.encode()).hexdigest()

# Read the hashed patient data from the file
# In our case this is only one person, but in the real world it would be multiple 
# people with multiple locations and timestamps who had contracted COVID-19
with open("hashedPatientData.json", "r") as file:
    hashedPatientData = json.load(file)

# Simulated student locations with timestamps (in plaintext)
# These would have been tracked by your application during your normal
# daily activities
studentData = [
    {"location": "MUPandaExpress", "time": "2024-11-12T11:00:00"},  
    {"location": "Coover1041LabA", "time": "2024-11-12T13:30:00"},
    {"location": "Durham171Lecture", "time": "2024-11-12T09:30:00"}
]

# Hash the student's locations
hashedStudentData = {
    hashData(f"{entry['location']}|{entry['time']}"): entry 
    for entry in studentData
}

# TODO:
# Find common hashed locations
# The data is given in json so you only need to compare the keys for each line of json file read and
# the studentData you have been given.  
# You will want to explore the python command set to test for membership (intersections)
commonHashes = set(hashedPatientData.keys()).intersection(hashedStudentData.keys())

# TODO:
# Retrieve original locations and times from the student's data
commonLocations = [hashedStudentData[commonHash] for commonHash in commonHashes]

# Output the results
print("Common locations found:", commonLocations)
