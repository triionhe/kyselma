DROP TABLE users, questions, answers, questionaires, quiz_links;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	nick TEXT,
	created TIMESTAMP DEFAULT NOW()
);
CREATE TABLE questions (
	id SERIAL PRIMARY KEY,
	question TEXT,
	neg_answer TEXT,
	pos_answer TEXT,
	created TIMESTAMP DEFAULT NOW()
);
CREATE TABLE answers (
	id SERIAL PRIMARY KEY,
	user_id INT,
	question_id INT,
	answer INT,
	created TIMESTAMP DEFAULT NOW()
);
CREATE TABLE questionaires (
	id SERIAL PRIMARY KEY,
	questionset INT[] DEFAULT '{}',
	creator_id INT,
	created TIMESTAMP DEFAULT NOW()
);
CREATE TABLE quiz_links (
	id SERIAL PRIMARY KEY,
	quiz_id INT,
	link TEXT,
	created TIMESTAMP DEFAULT NOW()
);
INSERT INTO users (nick) VALUES ('Raili Niemi');
INSERT INTO users (nick) VALUES ('Tea Jalava');
INSERT INTO users (nick) VALUES ('Eero Metsäranta');
INSERT INTO questions (question, neg_answer, pos_answer)
	VALUES ('Mikä ikä?', '0', '100'),
		('Mikä vointi?', 'huono', 'hyvä'),
		('Ulkoiletko?', 'viime vuonna', 'joka päivä'),
		('kys?', 'ei vielä', 'ei koskaan');
INSERT INTO answers (user_id, question_id, answer)
	VALUES (1, 1, 570),
		(1, 2, 670),
		(1, 3, 888),
		(1, 4, 999),
		(2, 1, 360),
		(2, 2, 230),
		(2, 3, 120),
		(2, 4, 123),
		(3, 1, 470),
		(3, 2, 570),
		(3, 3, 321),
		(3, 4, 785);
INSERT INTO questionaires (questionset,	creator_id)
	VALUES ('{1,2,3,4}', 1);
INSERT INTO quiz_links (quiz_id, link)
	VALUES (1, 'kysdemo');
