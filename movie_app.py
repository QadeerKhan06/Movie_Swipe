# imports
import pandas as pd
import re

# load dataset -- dataset from kaggle: "A Saga of Cinematic Data"
df = pd.read_csv('my_movies.csv')

# print(f'{df.head()}')

# print(df['original_language'].unique())

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

lang_dict = {
    "en": "English",
    "hi": "Hindi",
    "ja": "Japanese",
    "ko": "Korean",
    "it": "Italian",
    "pt": "Portuguese",
    "es": "Spanish",
    "zh": "Chinese",
    "fr": "French",
    "ru": "Russian",
    "tr": "Turkish",
    "sv": "Swedish",
    "ar": "Arabic",
    "de": "German",
    "cn": "Chinese (non-standard, usually 'zh')",
    "da": "Danish",
    "bn": "Bengali",
    "fa": "Persian (Farsi)",
    "th": "Thai",
    "pl": "Polish",
    "te": "Telugu",
    "sr": "Serbian",
    "hu": "Hungarian",
    "nl": "Dutch",
    "sh": "Serbo-Croatian (deprecated)",
    "et": "Estonian",
    "uk": "Ukrainian",
    "id": "Indonesian",
    "cs": "Czech",
    "no": "Norwegian",
    "ro": "Romanian",
    "ga": "Irish (Gaelic)",
    "gl": "Galician",
    "fi": "Finnish",
    "el": "Greek",
    "bs": "Bosnian",
    "is": "Icelandic",
    "la": "Latin",
    "tn": "Tswana",
    "nb": "Norwegian Bokmål",
    "he": "Hebrew",
    "km": "Khmer",
    "eu": "Basque"
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


def adult_content():
    while True:
        adult_input = input("\nDo you want to include adult content? (y/n)\n").strip().lower()
        if adult_input == "y":
            return True
        elif adult_input == "n":
            return False
        else:
            print("Please only input 'y' or 'n'.")

def get_language():
    user_lang = []
    while True:
        language_check = input("\nDo you want the movie to be in any specific language? (y/n)\n").strip().lower()

        language_choice = ""

        if language_check == "y":

            language_choice = input("\nWhich language(s) would you like? (eng, fr, jap)\n").strip().lower()

            # uses regular expressions to remove and letters in string
            lang_input_no_num = re.sub(r'\d+', '', language_choice)

            # converts into list using split
            lang_list = lang_input_no_num.split(',')

            # removes duplicate numbers
            lang_list_unique = list(set(lang_list))

            for str in lang_list_unique:
            # checks if the string is digits only
                # checks if the id is in dictionary
                if str in lang_dict:
                    # appends into new list
                    user_lang.append(str)
                else:
                    print(f'Language: {str} does not exist in our catalogue.')
        
            return user_lang

        elif language_check == "n":
            return []
        else:
            print("Please only input 'y' or 'n'.")

def get_min_rating():
    while True:
        min_rating = input("What is the minimum rating you would like? (0-10), Or press ENTER to skip.").strip()
        # if input is empty returns none because user doesnt desire a minimum rating
        if min_rating == "":
            return None
        try:
            # converts input into a float, not an integer because gives user more flexability
            min_rating = float(min_rating)
            # checks if input is within the given range
            if min_rating > 10 or min_rating < 0:
                print("Please enter a valid number. (0-10) Or optionally press ENTER if you do not desire a minimum rating requirement")
                continue
            else:
                return min_rating
        except ValueError:
            print("Invalid input please enter a valid number. (0-10).")

def get_year_range():
    while True:
        usr_year_range = input("Enter a range in years you would like to filter by. (e.g. 1990-2005) Or press ENTER to skip").strip()
        # if input is empty return none, because user doesnt desire a certain range
        if usr_year_range == "":
            return None, None
        # checks if hyphen is in input to determine whether it is a range between 2 years or one given year
        if "-" in usr_year_range:
            start_year, end_year = usr_year_range.split("-")
            # makes both into integers if isdigit is true
            if start_year.isdigit() and end_year.isdigit():
                start_year = int(start_year)
                end_year = int(end_year)
            else:
                print("Please only enter 2 valid years, seperated by a '-'.")
                continue
            # if range is given in reverse, swap them to make sure start year is the smaller year
            if start_year > end_year:
                start_year, end_year = end_year, start_year
            # checks to see if start or end year are outside the acceptable range
            if (start_year < 1900 or start_year > 2025) or (end_year < 1900 or end_year > 2025):
                print("Please enter a range within a valid year range (1900-2025)")
                continue
            # returns start and end year
            return start_year, end_year
        
        # checks to see if user didnt enter range, only a number, and makes sure its string only contains digits
        elif usr_year_range.isdigit():
            # makes var year an integer of user year range
            year = int(usr_year_range)
            # checks to see if year is outside acceptable year range
            if year > 2025 or year < 1900:
                print("Please enter a year within a valid year range (1900-2025)")
                continue
            # returns year
            return year, year
        # last case
        else:
            print("Invalid input. Please try again.")
            continue


def convert_genre_ids(genre_str):
    # remove sq brackets and empty spaces
    genre_str = genre_str.strip("[]").replace(" ", "")

    # split by comma and turn into list
    genre_list = genre_str.split(",")

    # return each item thats a digit as an integer
    return [int(i) for i in genre_list if i.isdigit()]


df["genre_ids_int"] = df["genre_ids"].apply(convert_genre_ids)
# print(f'{df}')

def filter_movies(df, user_genres, include_adult, language, ):
    
    # make copy of df
    filtered_df = df.copy()

    # checks if include adult is false
    if not include_adult:
        filtered_df = filtered_df[filtered_df['adult'] == False]

    # helper function
    def match_user_genres(row_genres):
        # checks every genre in row_genre
        for genre in row_genres:
            # if the genre is in user_genre return true
            if genre in user_genres:
                return True
        return False

    # apply helper function to entire dataset column "genre_ids_int"
    filtered_df = filtered_df[filtered_df['genre_ids_int'].apply(match_user_genres)]

    # returns filtered dataset
    return filtered_df


# get filters and store them
user_genres = get_genre()      
include_adult = adult_content()
filtered_df = filter_movies(df, user_genres, include_adult)
print(f"\nFound {len(filtered_df)} movies matching your filters.\n")

for index, row in filtered_df.head(10).iterrows():  # head(10) = only first 10 movies
    print(f"Title: {row['title']}")
    print(f"Genres: {convert_genres(row['genre_ids'])}")
    print(f"Release Date: {row['release_date']}")
    print("-" * 40)
