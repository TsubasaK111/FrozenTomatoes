import media
import frozen_tomatoes
these_movies = []

five_hundred_days_of_summer = media.Movie("500 Days of Summer",
                    "You should know upfront that this is not a love story ;) ",
                    "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
                    "https://www.youtube.com/watch?v=PsD0NpFSADM")

garden_state = media.Movie("Garden State",
                    "Contains: love, for lack of a better term. <br>Also: Natalie Portman! :D",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/Garden_State_Poster.jpg",
                    "https://www.youtube.com/watch?v=bCZVCU7vv78")

up_film = media.Movie("Up",
                    "How do you make a grown man cry within 5 minutes? Up.<br>Arguably the best Pixar film to date.",
                    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                    "https://www.youtube.com/watch?v=pkqzFUhGPJg")
goodwill_hunting = media.Movie("Goodwill Hunting",
                    "Robert Williams and Matt Damon Shenanigans!!!",
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                    "https://www.youtube.com/watch?v=z02M3NRtkAA")

donnie_darko = media.Movie("Donnie Darko",
                    "'A storm is coming. A storm that will swallow the children. And I will deliver them from the kingdom of Bane. I'll deliver the children back to their doorsteps. I'll send the monsters back to the underground. I'll send them back to a place where no one else can see them except for me, because I am Donnie Darko.'",
                    "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
                    "https://www.youtube.com/watch?v=ZZyBaFYFySk")

american_history_x = media.Movie("American History X",
                    "I believe that you often develop a hatred for something because it so accurately defines who you are. You are convinced that you are utterly trapped in your circumstance, and you try to take pride in that mindset. And oftentimes, love is what breaks that hatred, and leads to transcendence. Here is a tragic, beautiful example, one that I look back to whenever I am mired in hatred.",
                    "https://upload.wikimedia.org/wikipedia/en/0/0a/American_history_x_poster.jpg",
                    "https://www.youtube.com/watch?v=h4GZMt8rWbU")

pulp_fiction = media.Movie("Pulp Fiction",
                    "A classic. 'Nuff said.",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                    "https://www.youtube.com/watch?v=dZWPL9deY7I")
touching_the_void = media.Movie("Touching the Void",
                    "An impossible tale of survival, which just so happens to be all true.",
                    "https://upload.wikimedia.org/wikipedia/en/5/5f/Touching_the_Void.jpg",
                    "https://www.youtube.com/watch?v=dZWPL9deY7I")
these_movies.append(goodwill_hunting)
these_movies.append(five_hundred_days_of_summer)
these_movies.append(garden_state)
these_movies.append(up_film)
these_movies.append(donnie_darko)
these_movies.append(american_history_x)
these_movies.append(pulp_fiction)
these_movies.append(touching_the_void)
print(donnie_darko.__doc__)
print(donnie_darko.__module__)
print(donnie_darko.play_trailer.__name__)
frozen_tomatoes.open_movies_page(these_movies)
