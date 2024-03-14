--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT ts.title
	FROM tv_shows ts
	WHERE ts.id NOT IN (
		SELECT DISTINCT tsg.show_id
			FROM tv_show_genres tsg
			JOIN tv_genres tg
				ON tg.id = tsg.genre_id
			WHERE tg.name = 'Comedy'
		)
	ORDER BY ts.title;