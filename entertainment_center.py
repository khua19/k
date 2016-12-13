import fresh_tomatoes
import media


shestheman = media.Movie("She's the Man", "She's actually a girl.", "https://upload.wikimedia.org/wikipedia/en/6/60/She%27s_the_man_poster.jpg","https://www.youtube.com/watch?v=D4OhwrMidSU")

highschoolmusical = media.Movie("High School Musical", "High schools are not actually like this.", "https://upload.wikimedia.org/wikipedia/en/a/a5/HSMposter.jpg", "https://www.youtube.com/watch?v=ukDLkkvZYFk")

theedgeofseventeen = media.Movie("The Edge of Seventeen", "I want to see this movie.", "https://upload.wikimedia.org/wikipedia/en/7/76/The_Edge_of_Seventeen_2016_film_poster.jpg", "https://www.youtube.com/watch?v=EB6Gecy6IP8")


movies = [shestheman, highschoolmusical, theedgeofseventeen]

fresh_tomatoes.open_movies_page(movies)
