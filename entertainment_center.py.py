import fresh_tomatoes

import media

Thaandavam = media.Movie("Thaandavam",
                         " ",
                         "http://bit.ly/2xsh0nQ",
                         "https://youtu.be/ZuBrAl9JBtg")


Aym = media.Movie("AYM ",
                   " ",
                   "http://bit.ly/2ipWH7E",
                   "https://youtu.be/7Oz-8Vj_JfY")


Irumugan = media.Movie("Irumugan",
                       " ",
                       "http://bit.ly/2ipFw6l",
                       "https://youtu.be/L_0jexAQsB0")

Thuppakki = media.Movie("Thupakki ",
                        " ",
                        "http://bit.ly/2vfqMsw",
                        "https://youtu.be/2S0Fk2Dh9Mk")


twentyfour = media.Movie("24",
                         " ",
                         "http://bit.ly/2xcGlTd",
                         "https://youtu.be/tBkngXt7LLs")


Enthiran = media.Movie("Enthiran",
                       " ",
                       "http://bit.ly/2v5",
                       "https://youtu.be/FjWbHV2oMVk")


movies = [Thaandavam, Aym, Irumugan, Thuppakki, twentyfour, Enthiran]
fresh_tomatoes.open_movies_page(movies)
