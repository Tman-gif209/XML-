#Read in the movie.xml file.
import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root  = tree.getroot()

#list all the child tags of the movie element.
print("Number 1 - The movie elements are:")
for movie in root.iter("movie"):
    print(movie.attrib)

#I dont think that genre, decade and all the other tags are part of the movie element since if they wanted those tags the taks wouldve just told me to print all the tags but i have done what you have asked me to do.
for movie in root.iter():
    print(movie.tag)

# Use the itertext() function to print out the movie descriptions.
print("\n Number 2 - The movie descriptions are:")
for movie in root.iter():
    if movie.tag == 'description': 
       descriptions = "".join(movie.itertext())
       print(descriptions)

# Find the number of movies that are favourites and the number of
#movies that are not.
favourites = []
not_favourites = []

for movie in root.iter("movie"):
    if movie.attrib.get("favorite") == 'True':
        favourites.append(movie.attrib)
        number = len(favourites)

    else: 
        not_favourites.append(movie.attrib)
        amount = len(not_favourites)

print("\n Number 3:")
print(f"The total number of movies that are favourites is {number}.")
print(f"The total number of movies that are not favourites is {amount}.")