delimiter $$
CREATE PROCEDURE block_user()
BEGIN
    SET @max_num_2 = (SELECT count(user_id) FROM user);
    SET @x1 = 1;
    loop_label: LOOP    
        IF @x1 > @max_num_2 THEN
            LEAVE loop_label;
        END IF;

        UPDATE user
        JOIN loan
        ON loan.user = user.user_id
        SET late = IF( user.borrow_number > 2 OR loan.due_date < CURRENT_DATE, True , False) 
        WHERE user_id = @x1;
        
        
		UPDATE user
		SET late = IF(borrow_number = 0, False, late)
		WHERE user_id = @x1;
		
        SET @x1 = @x1 + 1;
        
        ITERATE loop_label;
    END LOOP loop_label;
END$$
delimiter ;

delimiter $$
CREATE PROCEDURE add_loan1(userx INT, bookx INT)
main_label:BEGIN
     SET @late_check= (SELECT late FROM user WHERE user_id = userx) ;
	 SET @error1 = " Usuário em situação irregular.";
     IF @late_check = 1 THEN
		SELECT @error1;
        LEAVE main_label;
     END IF;   
     SET @CD = CURRENT_DATE;
     SET @DD = date_add(current_date, INTERVAL 30 DAY);
     INSERT INTO loan (start_date, due_date, book, user)
     VALUES (@CD, @DD, bookx, userx);

END$$
delimiter ;

delimiter $$
CREATE PROCEDURE check_borrow()
BEGIN
    SET @max_num_1= (SELECT count(user_id) FROM user);
    SET @y1 = 1;
    loop_label: LOOP    
        IF @y1 > @max_num_1 THEN
            LEAVE loop_label;
        END IF;
		SET @countage = (SELECT COUNT(user) from loan where user = @y1);
		UPDATE user
		SET borrow_number = @countage
		where user_id = @y1;
       
		SET @y1 = @y1 + 1;
        
        ITERATE loop_label;
    END LOOP loop_label;
END$$
delimiter ;

delimiter $$

CREATE PROCEDURE search_user(search_term VARCHAR(30))
BEGIN
    SET @search_term_1 = NULL;
    SET @search_term_1 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT * FROM user
	WHERE (first_name LIKE CONCAT("%",search_term,"%") 
	OR last_name LIKE CONCAT("%",search_term,"%") 
	OR contact LIKE CONCAT("%",search_term,"%")
	OR address LIKE CONCAT("%",search_term,"%")
	OR user_id = @search_term_1 
	OR borrow_number = @search_term_1);
    
END$$

delimiter ;

delimiter $$
CREATE PROCEDURE search_book(search_term VARCHAR(30))
BEGIN
    SET @search_term_2 = NULL;
    SET @search_term_2 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT book.book_id, book.book_name, book.genre, author.author_name, branch.branch_name, branch.address FROM book
	JOIN author ON author.author_id = book.author
	JOIN publisher ON publisher.publisher_id = book.publisher
	JOIN branch ON branch.branch_id = book.branch
	WHERE (book_name LIKE CONCAT("%",search_term,"%") 
	OR book.genre LIKE CONCAT("%",search_term,"%") 
	OR branch.branch_name LIKE CONCAT("%",search_term,"%")
	OR branch.address LIKE CONCAT("%",search_term,"%")
    OR author.author_name LIKE CONCAT("%",search_term,"%")
	OR book_id = @search_term_2);
	
    
END$$
delimiter ;


delimiter $$

CREATE PROCEDURE search_worker(search_term VARCHAR(30))
BEGIN
    SET @search_term_3 = NULL;
    SET @search_term_3 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT worker.worker_first_name, worker.worker_last_name, branch.branch_name, worker.work, worker.worker_contact, worker.worker_address, worker.worker_id FROM worker
	JOIN job ON worker.worker_id = job.worker_id
	JOIN branch ON job.branch_id = branch.branch_id
    WHERE (worker.worker_first_name LIKE CONCAT("%",search_term,"%") 
	OR worker.worker_last_name LIKE CONCAT("%",search_term,"%") 
	OR worker.worker_contact LIKE CONCAT("%",search_term,"%")
	OR worker.worker_address LIKE CONCAT("%",search_term,"%")
	OR worker.work LIKE CONCAT("%",search_term,"%")
    OR branch.branch_name LIKE CONCAT("%",search_term,"%")
    OR worker.worker_id = @search_term_3);
    
END$$

delimiter ;



delimiter $$

CREATE PROCEDURE search_publisher(search_term VARCHAR(30))
BEGIN
    SET @search_term_4 = NULL;
    SET @search_term_4 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT * FROM publisher
	WHERE (publisher_contact LIKE CONCAT("%",search_term,"%")
    OR publisher_name LIKE CONCAT("%",search_term,"%")
    OR publisher_id = @search_term_4);
    
END$$

delimiter ;


delimiter $$

CREATE PROCEDURE search_loan(search_term VARCHAR(30))
BEGIN
    SET @search_term_5 = NULL;
    SET @search_term_5 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT loan.loan_id,loan.start_date, loan.due_date, book.book_name, book.book_id, user.last_name, user.user_id FROM loan
    JOIN book
    ON loan.book = book.book_id
    JOIN user
    ON loan.user = user.user_id
	WHERE (loan.start_date LIKE CONCAT("%",search_term,"%")
    OR loan.due_date LIKE CONCAT("%",search_term,"%")
    OR book.book_name LIKE CONCAT("%",search_term,"%")
    OR user.last_name LIKE CONCAT("%",search_term,"%")
    OR loan.loan_id = @search_term_5
    OR book.book_id = @search_term_5
    OR user.user_id = @search_term_5);
    
END$$

delimiter ;

delimiter $$

CREATE PROCEDURE search_author(search_term VARCHAR(30))
BEGIN
    SET @search_term_6 = NULL;
    SET @search_term_6 = (SELECT CAST(search_term AS UNSIGNED));
    SELECT * FROM author
    WHERE (author_name LIKE CONCAT("%",search_term,"%")
    OR author_id = @search_term_6);
    
END$$

delimiter ;

delimiter $$
CREATE PROCEDURE return_book(book_num INT, branch_num INT)
BEGIN
    DELETE FROM loan 
	WHERE book = book_num;
    
    UPDATE book
	SET branch = branch_num
    WHERE book_id = book_num;
    
    
END$$
delimiter ;


SET @CD = CURRENT_DATE;
SET @DD = date_add(current_date, INTERVAL 30 DAY);
select @min;
select @max;