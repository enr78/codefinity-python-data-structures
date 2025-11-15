marvel_movies = {
    'Avengers: Endgame',
    'Black Panther',
    'Iron Man',
    'The Dark Knight',
    'Spider-Man: No Way Home',
    'Guardians of the Galaxy',
    'Justice League'
}

# Write your code here
# runs an error if it does not exist in data set
marvel_movies.remove("The Dark Knight") 
# DOES NOT RUN ERROR if it does not exist in data set
marvel_movies.discard("Justice League")

# Testing
print("Updated set:", marvel_movies)