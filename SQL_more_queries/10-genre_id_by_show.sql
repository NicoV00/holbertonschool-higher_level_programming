-- Import the database dump from hbtn_0d_tvshows to your MySQL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = show_id ORDER BY title, genre_id;