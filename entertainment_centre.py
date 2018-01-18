import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "Story of a boy whose toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg")

hunger_games = media.Movie("Hunger Games",
                        "https://www.youtube.com/watch?v=mfmrPu43DF8",
                        "The Hunger Games is a trilogy of young adult dystopian novels written by American novelist Suzanne Collins.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/3/39/The_Hunger_Games_cover.jpg/220px-The_Hunger_Games_cover.jpg")

iron_man = media.Movie("Iron Man",
                        "https://www.youtube.com/watch?v=8hYlB38asDY",
                        "Iron Man is a fictional superhero appearing in American comic books published by Marvel Comics. ",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Iron_Man_bleeding_edge.jpg/220px-Iron_Man_bleeding_edge.jpg")

imitation_game = media.Movie("Imitataion Game",
                        "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                        "The Imitation Game is a 2014 American historical drama film directed by Morten Tyldum and written by Graham Moore, loosely based on the biography Alan Turing: The Enigma by Andrew Hodges",
                        "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg")

social_network = media.Movie("Social Network",
                        "https://www.youtube.com/watch?v=lB95KLmpLR4",
                        "The Social Network is a 2010 American biographical drama film directed by David Fincher and written by Aaron Sorkin.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg")

now_you_see_me = media.Movie("Now You See Me",
                        "https://www.youtube.com/watch?v=KzJNYYkkhzc",
                        "Now You See Me is a 2013 American heist thriller film directed by Louis Leterrier and written by Ed Solomon, Boaz Yakin and Edward Ricourt.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Now_You_See_Me_Poster.jpg/220px-Now_You_See_Me_Poster.jpg")



movie_list = [toy_story,hunger_games,iron_man,imitation_game,social_network,now_you_see_me]
fresh_tomatoes.open_movies_page(movie_list)
