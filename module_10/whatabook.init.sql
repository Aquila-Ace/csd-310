# whatabook.init.sql
# Alex Bailey
# August 5, 2023
# Module 10.3 Individual Codes



# Create the database
CREATE DATABASE whatabook;



# Create user and grant privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


# Create tables
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
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



# Insert new store listing
INSERT INTO store(locale)
    VALUES('11035 T Plaza, Omaha, NE 68137');



# Insert new book listings
INSERT INTO book(book_name, author, details)
    VALUES('On A Pale Horse', 'Piers Anthony', 'Book One of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('Bearing An Hourglass', 'Piers Anthony', 'Book Two of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('With A Tangled Skein', 'Piers Anthony', 'Book Three of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('Wielding A Red Sword', 'Piers Anthony', 'Book Four of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('Being A Green Mother', 'Piers Anthony', 'Book Five of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('For Love Of Evil', 'Piers Anthony', 'Book Six of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('And Eternity', 'Piers Anthony', 'Book Seven of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('Under A Velvet Cloak', 'Piers Anthony', 'Book Eight of Incarnations of Immortality');

INSERT INTO book(book_name, author, details)
    VALUES('A Spell For Chameleon', 'Piers Anthony', 'The First Xanth Novel');



# Insert new user listings 
INSERT INTO user(first_name, last_name) 
    VALUES('Alex', 'Bailey');

INSERT INTO user(first_name, last_name)
    VALUES('Grace', 'Bradford');

INSERT INTO user(first_name, last_name)
    VALUES('Heather', 'Kuehl');



# Insert new wishlist listings
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Alex'), 
        (SELECT book_id FROM book WHERE book_name = 'A Spell For Chameleon')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Grace'),
        (SELECT book_id FROM book WHERE book_name = 'Being A Green Mother')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Heather'),
        (SELECT book_id FROM book WHERE book_name = 'On A Pale Horse')
    );
