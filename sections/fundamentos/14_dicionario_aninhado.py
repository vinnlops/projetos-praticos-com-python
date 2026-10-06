import pprint

filmsDict = {
    "inception": {
        "yearReleased": 2010,
        "imbRating": 8.8,
        "genre": ["Action", "Adventure", "Sci-Fi"]
    },
    "interstellar": {
        "yearReleased": 2014,
        "imbRating": 8.6,
        "genre": ["Adventure", "Drama", "Sci-Fi"]
    },
    "the_dark_knight": {
        "yearReleased": 2008,
        "imbRating": 9.0,
        "genre": ["Action", "Crime", "Drama"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

print(filmsDict["interstellar"]["genre"])

filmsDict["inception"]["director"] = "Christopher Nolan"
print(filmsDict["inception"])

del filmsDict["the_dark_knight"]["imbRating"]
print(filmsDict["the_dark_knight"])