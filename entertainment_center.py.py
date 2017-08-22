import fresh_tomatoes
import media


vivegam = media.Movie("VIVEGAM",
                      " ",
                      "https://goo.gl/4GF4Uf",
                      "https://youtu.be/uM7zTAMFRxc")

bahubali = media.Movie("BAHUBALI 2",
                       " ",
                       "https://goo.gl/WG15KS",
                       "https://youtu.be/94BzBOpv42g")

fury = media.Movie("FURY",
                   " ",
                   "http://bit.ly/2uUJObE",
                   "https://youtu.be/09w9MTtZDEM")


argo = media.Movie("ARGO",
                    "",
                    "https://goo.gl/YzD4bs",
                    "https://youtu.be/T29kIOXpj6o")

ironman = media.Movie("Iron Man",
                      " ",
                      "https://goo.gl/S94jLf",
                      "https://youtu.be/YLorLVa95Xo")

singam3 = media.Movie("S 3",
                      " ",
                      "https://goo.gl/VdArbn",
                      "https://youtu.be/CP9DinMVFq8")

movies = [vivegam, bahubali, fury, argo, ironman, singam3]
fresh_tomatoes.open_movies_page(movies)
