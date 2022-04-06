# import statement
import sqlite3

# make connection
connection = sqlite3.connect("Tweets.db")

# create cursor object
cur_obj = connection.cursor()

# DATA DEFINITION LANGUAGE
# CREATE QUERY
create_query = '''
CREATE TABLE tweet (
    tweetID INTEGER NOT NULL PRIMARY KEY,
    Text VARCHAR(280),
    creationDate DATETIME,
    User VARCHAR(20),
    Likes INTEGER,
    Retweets INTEGER,
    Comments INTEGER
);
'''
# Execute the create query
#cur_obj.execute(create_query)
#once commit will change the database, just execute will save to memory only
#connection.commit()
#connection.close()


# DATA MANIPULATION LANGUAGE
# INSERT QUERY

# With question mark placeholders
record = (2, 'this is not a tweet', '2021-01-02', '@Alice')
insert_query = '''
    INSERT INTO tweet(tweetID, Text, CreationDate, User)
    VALUES (?,?,?,?)
'''

# cur_obj.execute(insert_query,record)
# connection.commit()
# connection.close()




# MULTIPLE RECORDS AT ONCE
records = [
(3, 'hello world', '2022-02-25', '@Eve'),
(4, 'hello universe', '2022-02-26', '@Beth'),
(5, 'This is Patrick', '2021-12-24', '@Star')
]

insert_query3 = '''
    INSERT INTO tweet(tweetID,Text,creationDate,User)
    VALUES (?,?,?,?);
'''
# use .executemany for multiple records
#############
cur_obj.executemany(insert_query3,records)
connection.commit()
# connection.close()



# UPDATE QUERY
new_data = [
    (4,5,10,2),
    (10,15,20,3),
    (5000000,0,1,5)
]
update_query = '''
    UPDATE tweet
    SET Likes = ?, Comments = ?, Retweets = ?
    WHERE tweetID = ?;
'''
#cur_obj.executemany(update_query, new_data)
#connection.commit()
#connection.close()



# SELECT QUERY
select_query = '''
    SELECT *
    FROM tweet;
'''

result = cur_obj.execute(select_query)
for row in result:
    print(row)




# with question mark placeholder
search_name = ['@Star']
select_query1 = '''
    SELECT *
    FROM tweet
    WHERE User = ?
'''
# passing search name as a tuple
result = cur_obj.execute(select_query1, search_name)

for row in result:
    print(row)



# built in string placeholder

search_name = '@Star'
select_query1 = '''
    SELECT *
    FROM tweet
    WHERE User = '%s'
'''
result = cur_obj.execute(select_query1 % search_name)
for row in result:
    print(row)


# named placeholder
name = '@Star'
id = 5

select_query3 = '''
    SELECT *
    FROM tweet WHERE User =:username
    AND tweetID =:tID;
'''
result = cur_obj.execute(select_query3,{'username':name,'tID':id} )
for row in result:
    print(row)



# fetchall
#
select_query4 = '''
     SELECT *
     FROM tweet
 '''
cur_obj.execute(select_query4)
for row in cur_obj.fetchall():
    print(row)
#


# fetchone
select_query5 = '''
    SELECT *
    FROM tweet
'''
cur_obj.execute(select_query5)
#fetch one at a time
print(cur_obj.fetchone())
print(cur_obj.fetchone())


connection.close()
