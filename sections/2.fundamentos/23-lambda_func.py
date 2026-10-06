power = lambda num: num ** 2

is_even = lambda x: x % 2 == 0

div_num = lambda x, y: x / y

reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(27))
print(is_even(30))
print(div_num(10, 2))
print(div_num(6, 2))
print(reverse_string("Python"))
print(reverse_string("Javascript"))


movies_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [8.5, 9.0, 7.5],
    "Inception": [8.5, 9.0, 7.5],
    "Jurassic Park": [8.5, 9.0, 7.5]
}

average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])