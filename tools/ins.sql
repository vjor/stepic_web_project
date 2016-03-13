INSERT INTO `myweb`.`qa_question`
        (`id`, `title`, `text`, `rating`, `author`, `likes_id`)
VALUES ('1', '1 quest', '1 вопрос', '1', 'myweb', '1');

INSERT INTO `myweb`.`qa_question`
        (`id`, `title`, `text`, `rating`, `author`, `likes_id`)
VALUES ('2', '2 quest', '2 вопрос', '1', 'myweb', '2');


INSERT INTO `myweb`.`qa_answer` 
	(`id`,`title`, `text`, `author`, `question_id`) 
VALUES ('1', 'Первый вопрос', '1 вопрос 1 отвт', 'myweb', '1');


INSERT INTO `myweb`.`qa_answer` 
	(`id`,`title`, `text`, `author`, `question_id`) 
VALUES ('1', 'Первый вопрос', '1 вопрос 2 answ' , 'myweb', '1');


INSERT INTO `myweb`.`qa_answer` 
	(`id`,`title`, `text`, `author`, `question_id`) 
VALUES ('2', 'Второй вопрос','2 вопрос 1 answ',  'авд', '2');


COMMIT