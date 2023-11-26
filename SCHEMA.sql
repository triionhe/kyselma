DROP TABLE users, questions, answers, questionaires, quiz_links;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	nick TEXT,
	created INT
);
CREATE TABLE questions (
	id SERIAL PRIMARY KEY,
	question TEXT,
	neg_answer TEXT,
	pos_answer TEXT,
	created INT
);
CREATE TABLE answers (
	id SERIAL PRIMARY KEY,
	user_id INT,
	question_id INT,
	answer INT,
	created INT
);
CREATE TABLE questionaires (
	id SERIAL PRIMARY KEY,
	questionset INT[] DEFAULT '{}',
	creator_id INT,
	created INT
);
CREATE TABLE quiz_links (
	id SERIAL PRIMARY KEY,
	quiz_id INT,
	link TEXT,
	created INT
);
INSERT INTO users (nick, created) VALUES ('Raili Niemi', 57 );
INSERT INTO users (nick, created) VALUES ('Tea Jalava', 36 );
INSERT INTO users (nick, created) VALUES ('Eero Metsäranta', 47 );
INSERT INTO questions (question, neg_answer, pos_answer, created)
	VALUES ('Mikä ikä?', '0', '100', 99 ),
		('Mikä vointi?', 'huono', 'hyvä', 99 ),
		('Ulkoiletko?', 'viime vuonna', 'joka päivä', 99 ),
		('kys?', 'ei vielä', 'ei koskaan', 99 );
INSERT INTO answers (user_id, question_id, answer, created)
	VALUES (1, 1, 570, 99 ),
		(1, 2, 670, 99 ),
		(1, 3, 888, 99 ),
		(1, 4, 999, 99 ),
		(2, 1, 360, 99 ),
		(2, 2, 230, 99 ),
		(2, 3, 120, 99 ),
		(2, 4, 123, 99 ),
		(3, 1, 470, 99 ),
		(3, 2, 570, 99 ),
		(3, 3, 321, 99 ),
		(3, 4, 785, 99 );
INSERT INTO questionaires (questionset,	creator_id, created)
	VALUES ('{1,2,3,4}', 1, 666);
INSERT INTO quiz_links (quiz_id, link, created)
	VALUES (1, 'kysdemo', 666);
