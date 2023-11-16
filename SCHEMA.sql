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
	ready BOOLEAN DEFAULT FALSE,
	created INT
);
