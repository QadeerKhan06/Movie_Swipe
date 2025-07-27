# imports
import pandas as pd

# load dataset -- dataset from kaggle: "A Saga of Cinematic Data"
df = pd.read_csv('my_movies.csv')

# print(f'{df.head()}')

# Create a genre to convert 'genre_ids' to the corresponding genre via TMDB genre id
genre_dict = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}

def convert_genres(genre_id):
    # remove spaces
    genre_id_no_spaces = genre_id.replace(" ", "")

    # remove sq brackets
    genre_id_no_brackets = genre_id_no_spaces.replace("[", "").replace("]", "")

    # converts string into a list
    genre_id_list = genre_id_no_brackets.split(',')

    # loop through the dictionary and convert the list of numbers into words
    genre_names = []
    for i in genre_id_list:
        if i.isdigit():
            genre_int = int(i)
            if genre_int in genre_dict:
                genre_names.append(genre_dict[genre_int])
            else:
                genre_names.append(f"Unknown({genre_int})")
                
    return genre_names

# convert_genres("[18, 80]")
df['genre_names'] = df['genre_ids'].apply(convert_genres)

print(f'{df}')