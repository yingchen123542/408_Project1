--create tables for driver and user

CREATE TABLE IF NOT EXISTS User(
    userID INT, --odd number as ID
    findDriver BOOLEAN,
    userRating FLOAT,
    pickupLocation VARCHAR(150),
    dropoffLocation VARCHAR(150),
    PRIMARY KEY(userID)
);

INSERT INTO User VALUES(1, TRUE, 4.5, 'Orange', 'Irvine');
INSERT INTO User VALUES(3, FALSE, 4.0, 'LAX', 'SNA');
INSERT INTO User VALUES(5, TRUE, 4.2, 'Garden Grove', 'Chapman');
INSERT INTO User VALUES(7, FALSE, 4.1, 'SNF', 'JFK');
INSERT INTO User VALUES(9, TRUE, 3.1, 'HAHA', 'HAHAHA');


CREATE TABLE IF NOT EXISTS Driver(
    driverID INT, --even number as ID
    driveMode BOOLEAN,
    currentRating FLOAT,
    userID INT,
    FOREIGN KEY(userID) REFERENCES User(userID)

);

INSERT INTO Driver VALUES(2, TRUE, 4.5, 1);
INSERT INTO Driver VALUES(4, FALSE, 4.0, 3);
INSERT INTO Driver VALUES(6, TRUE, 4.2, 5);
INSERT INTO Driver VALUES(8, FALSE, 4.1, 7);
INSERT INTO Driver VALUES(10, TRUE, 3.1, 9);

SELECT * FROM User;
SELECT * FROM Driver;

