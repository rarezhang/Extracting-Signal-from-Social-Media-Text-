import MySQLdb



# connect python with mysql
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd='qwer1234',
                     db='TWITTER',   # name of the db
                     local_infile = 1) 
# create a Cursor object
## Cursor can execute all the queries
cur = db.cursor()


#############################################################################################
# pre-process the table 

# create table 
## prediction+'|'+tweet_id+'|'+created_at+'|'+text+'|'+location+'|'+time_zone
'''
DROP TABLE IF EXISTS twitter;
'''

"""
CREATE TABLE twitter 
( 
prediction INT(1) NOT NULL,
tweet_id BIGINT NOT NULL, 
created_at VARCHAR(30) NOT NULL, 
text VARCHAR(200), 
location CHAR(2), 
time_zone VARCHAR(80) 
);
"""


# load data infile
### better run this code in mysql
### mysql --local-infile -uroot -p
"""
LOAD DATA LOCAL INFILE '/home/wenli/Projects/tweetsnlp/data/test_pred' 
INTO TABLE twitter        
FIELDS TERMINATED BY '|'  
LINES TERMINATED BY '\n';
"""



# change data type of created_at
"""
UPDATE twitter SET created_at = substring(created_at, 1, 19);
ALTER TABLE twitter MODIFY created_at DATETIME;
"""



# build indexes: tweet_id, created_at, location, prediction 
### better run this code in mysql
### mysql --local-infile -uroot -p
#### DROP INDEX tweet_id ON twitter;
"""
ALTER IGNORE TABLE twitter ADD UNIQUE INDEX tweet_id (tweet_id); # unique index, remove duplicates
CREATE INDEX created_at on twitter (created_at);
CREATE INDEX location on twitter (location);
CREATE INDEX prediction on twitter (prediction);
"""

#############################################################################################
# show columns
'''
sql = "show columns in twitter;"
'''
#############################################################################################
# run the qurey 
cur.execute(sql)

'''
for row in cur.fetchall():
    print row
'''
