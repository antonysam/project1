import fresh_tomatoes
import media


Thaandavam = media.Movie("Thaandavam",
                      " ",
                      "http://bit.ly/2xsh0nQ",
                      "https://youtu.be/uM7zTAMFRxc")

AYM = media.Movie("AYM ",
                       " ",
                       "http://bit.ly/2xbYJf0",
                       "https://youtu.be/94BzBOpv42g")

Irumugan = media.Movie("Irumugan",
                   " ",
                   "http://bit.ly/2vXtiqa",
                   "https://youtu.be/09w9MTtZDEM")


Thupakki = media.Movie("Thupakki",
                    "",
                    "http://bit.ly/2v5pWm8",
                    "https://youtu.be/T29kIOXpj6o")

twentyfour = media.Movie("24",
                      " ",
                      "http://bit.ly/2xcGlTd",
                      "https://youtu.be/YLorLVa95Xo")

Enthiran = media.Movie("Enthiran",
                      " ",
                      "http://bit.ly/2v5c7UZ",
                      "https://youtu.be/CP9DinMVFq8")

movies = [Thaandavam, AYM, Irumugan, Thupakki, twentyfour, Enthiran]
fresh_tomatoes.open_movies_page(movies)
