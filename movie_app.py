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

# print(f'{df}')

def show_genre():
    print(f'\nHere are the list of IDs with their corresponding genre.\n')
    for key, value in genre_dict.items():
        print(f'{key}: {value}')

show_genre()

def get_genre():
    user_genres = []
    while True:
        # gets input and removes spaces
        genre_input = input("\nEnter the ID's you are interested in seperated by commas. [eg. 18, 80]\n").replace(" ", "")

        # uses regular expressions to remove and letters in string
        genre_input_no_letters = re.sub(r'[^0-9,]', '', genre_input)

        # converts into list using
        genre_list = genre_input_no_letters.split(',')

        # removes duplicate numbers
        genre_list_unique = list(set(genre_list))

        # loops through list
        for num in genre_list_unique:
            # checks if the string is digits only
            if num.isdigit():
                # converts to int and stores into temp var
                genre_id = int(num)
                # checks if the id is in dictionary
                if genre_id in genre_dict:
                    # appends into new list
                    user_genres.append(genre_id)
                else:
                    print(f'ID: {genre_id} does not exist.')
            else:
                print(f'Do not enter letters/special characters.')
        # checks if list is empty
        if not user_genres:
            print("No valid genre received.")
            # restarts the loop - readability
            continue
        else:
            # print(user_genres)
            return user_genres

get_genre()

def adult_content():
    while True:
        adult_input = input("\nDo you want to include adult content? (y/n)\n").strip().lower()
        if adult_input == "y":
            return True
        elif adult_input == "n":
            return False
        else:
            print("Please only input 'y' or 'n'.")
        
adult_content()
