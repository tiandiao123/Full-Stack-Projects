import os

class Movie():
	# the constructor function which is used to initialize movie attributes
	def __init__(self,movie_title,poster_url,trailer_youtube):
		# moview attributes: movie name, movie poster and movie youtube url
		self.title = movie_title
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_youtube
