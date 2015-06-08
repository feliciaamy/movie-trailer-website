import media
import fresh_tomatoes
from py_compile import compile

# Compile fresh_tomatoes with .pyc form
compile('fresh_tomatoes.py')

# Create favourite movies with media.Movie instance
# A Movie is (title, summary, picture_url, youtube_url, actors, rating)
toy_story = media.Movie('Toy Story',
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
                        'http://www.impawards.com/1995/posters/toy_story_ver1.jpg',
                        'https://www.youtube.com/watch?gl=SG&hl=en-GB&v=KYz2wyBy3kc',
                        'G',
                        8.3)
avatar = media.Movie('Avatar',
                    "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                    'http://www.impawards.com/2009/posters/avatar.jpg',
                    'https://www.youtube.com/watch?v=5PSNL1qE6VY',
                     'PG-13',
                     7.9)
hunger_games = media.Movie('The Hunger Games',
                           "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
                           'http://www.film.com/wp-content/uploads/2011/07/Hunger-Games-Teaser-Poster-Large.jpg',
                           'https://www.youtube.com/watch?v=4S9a5V9ODuY',
                           'PG-13',
                           6.8)
good_luck_chuck = media.Movie('Good Luck Chuck',
                              'In order to keep the woman of his dreams from falling for another guy, Charlie Logan has to break the curse that has made him wildly popular with single women: Sleep with Charlie once, and the next man you meet will be your true love.',
                              'http://www.impawards.com/2007/posters/good_luck_chuck_ver4_xlg.jpg',
                              'https://www.youtube.com/watch?v=79cWig36XJc',
                              'R',
                              5.6)
divergent = media.Movie('Divergent',
                        "In a world divided by factions based on virtues, Tris learns she's Divergent and won't fit in. When she discovers a plot to destroy Divergents, Tris and the mysterious Four must find out what makes Divergents dangerous before it's too late.",
                        'https://s-media-cache-ak0.pinimg.com/736x/ff/7c/5b/ff7c5b7a3100e0c9665dccea73553e9b.jpg',
                        'https://www.youtube.com/watch?v=sutgWjz10sM',
                        'PG-13',
                        6.8)
TFIOS = media.Movie('The Fault in Our Star',
                    'Two teens, both who have different cancer conditions, fall in love after meeting at a cancer support group.',
                    'http://upload.wikimedia.org/wikipedia/en/2/22/Fault_in_our_stars.jpg',
                    'https://www.youtube.com/watch?v=9ItBvH5J6ss',
                    'PG-13',
                    7.9)
inside_out = media.Movie('Inside Out',
                        "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house and school.",
                        'http://media.aintitcool.com/media/uploads/2015/nordling/insideoutposter.jpg',
                        'https://www.youtube.com/watch?v=_MC3XuMvsDI',
                        "PG",
                        9.1)
up = media.Movie('Up',
                "To avoid being taken away to a nursing home, an old widower tries to fly his home to Paradise Falls, South America, along with a boy scout who accidentally lifted off with him.",
                'http://www.movie-poster-artwork-finder.com/posters/up-poster-artwork-edward-asner-christopher-plummer-jordan-nagai.jpg',
                'https://www.youtube.com/watch?v=pkqzFUhGPJg&hl=en-GB&gl=SG',
                'PG',
                8.3)
tangled = media.Movie('Tangled',
                    "The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.",
                    'http://img3.wikia.nocookie.net/__cb20130828020844/disney/images/4/4b/Tangled_poster_c.jpg',
                    'https://www.youtube.com/watch?v=gsYKF8ecC8g',
                    'PG',
                    7.8)


# Create a list of the movies
movies = [toy_story,avatar,hunger_games,good_luck_chuck,divergent,TFIOS,inside_out,up,tangled]

# Transfer the movies information to the website in the form of html file
fresh_tomatoes.open_movies_page(movies)
