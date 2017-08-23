import fresh_tomatoes
import media


Thaandavam = media.Movie("Thaandavam",
                      " ",
                      "http://bit.ly/2xsh0nQ",
                      "http://bit.ly/2w3CJmq")

AYM = media.Movie("AYM ",
                       " ",
                       "http://bit.ly/2xbYJf0",
                       "http://bit.ly/2wEN8aI")

Irumugan = media.Movie("Irumugan",
                   " ",
                   "http://bit.ly/2vXtiqa",
                   "http://bit.ly/2cctHIZ")


Thupakki = media.Movie("Thupakki",
                    "",
                    "http://bit.ly/2v5pWm8",
                    "http://bit.ly/2w3EnVn")

twentyfour = media.Movie("24",
                      " ",
                      "http://bit.ly/2xcGlTd",
                      "http://bit.ly/2vfxhLU")

Enthiran = media.Movie("Enthiran",
                      " ",
                      "http://bit.ly/2v5c7UZ",
                      "http://bit.ly/2vokXZ3")

movies = [Thaandavam, AYM, Irumugan, Thupakki, twentyfour, Enthiran]
fresh_tomatoes.open_movies_page(movies)
