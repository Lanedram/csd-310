/*
    Title: db_init.sql
    Author: Lanedra Moore
    Date: Aug 5, 2023
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(store_id, locale)
    VALUES('3484', '7373 LONG JOHN RD, WHATTA, BOOK, 44454');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Spiderman Edition 1', , 'Peter Parker','Follow spiderman through his majestic endurances');

INSERT INTO book(book_name, author, details)
    VALUES('The Incredible Hulk', 'Bruce Banner', 'HULK SMASH!');

INSERT INTO book(book_name, author, details)
    VALUES('Asgardian Angels: Thor', 'Thunder God Thor', 'Detailed experience of Thors battles');

INSERT INTO book(book_name, author, details)
    VALUES('Black Widow','Natasha Romanov', 'Unravel the Black Widows wildest findings');

INSERT INTO book(book_name, author, details)
    VALUES('The Man of Steel', 'Tony Stark','Iron Mans comparison of himself to Superman');


INSERT INTO book(book_name, author, details)
    VALUES('Capt. Always Do Right', 'Steve Rogers', 'The Legendary Task of being the most honorable hero');


INSERT INTO book(book_name, author, details)
    VALUES('The Scarletts Witch Mindset Book',  'Wanda Maximoff', 'Unleashing your inner power and setting your mind free');


INSERT INTO book(book_name, author, details)
    VALUES('The Black Panthers Moral Guide', 'TChalla', 'Family, Freedom, and Ancestry');


INSERT INTO book(book_name, author, details)
    VALUES('The Winters Soldiers Redemption', 'James Barnes', 'What to do when you get a second chance');


/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Stan', 'Lee');

INSERT INTO user(first_name, last_name)
    VALUES('Jack', 'Kirby');


INSERT INTO user(first_name, last_name)
    VALUES('Gerry', 'Duggan');


/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) VALUES (2, 8);

INSERT INTO wishlist(user_id, book_id) VALUES (1, 3);

INSERT INTO wishlist(user_id, book_id) VALUES (3, 5);
