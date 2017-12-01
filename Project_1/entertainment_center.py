import os
import fresh_tomatoes
import media

# Moon Light movie: Movie name, poster url and trailer youtube url
moonlight = media.Movie("MOON LIGHT",
	"https://assets.mubi.com/images/notebook/post_images/22267/images-w1400.jpg?1474980339",
	"https://www.youtube.com/watch?v=9NJj12tJzqc")

# Spider Man movie: Movie name,poster url and trailer youtube url
spiderman = media.Movie("Spider Man",
	"https://www.technobuffalo.com/wp-content/uploads/2017/07/SpiderManPoster.jpg",
	"https://www.youtube.com/watch?v=DiTECkLZ8HM")


# Mother movie: movie name, poster url and trailer youtube url
Mother = media.Movie("The Mother",
	"https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Mother-Movie-New-Poster-2.jpg?ssl=1",
	"https://www.youtube.com/watch?v=XpICoc65uh0")

movies = [moonlight,spiderman,Mother]

fresh_tomatoes.open_movies_page(movies)