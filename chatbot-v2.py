#Thomas Livshits
#CS 370

#----------------------------------------------------------Imports-------------------------------------------------------------------------
import sqlite3 #DB
import json
from datetime import datetime
import time
#----------------------------------------------------------End-----------------------------------------------------------------------------
timeframe = '2018-06' #Reddit Data-set used ( 06/2018 )
sql_transaction = []
start_row = 0
cleanup = 1000000

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()
#----------------------------------------------------------Create Table--------------------------------------------------------------------
def create_table():
	c.execute("""CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)""") #create table if none 
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------Format json data----------------------------------------------------------------
def format_data(data):
	data = data.replace("\n"," newlinechar ").replace("\r"," newlinechar ").replace('"',"'") #removes \n and \r from comments(data)
	return data
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------Set up the transaction only executes if it is over 1000-------------------------
def transaction_bldr(sql): #sets up transaction to only execute if it is over 1000, makes it run quicker if there is a stack 
	global sql_transaction
	sql_transaction.append(sql)
	if len(sql_transaction) > 1000:
		c.execute('BEGIN TRANSACTION')
		for s in sql_transaction:
			try:
				c.execute(s)
			except:
				pass
		connection.commit()
		sql_transaction = []
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------SQL inserts based on case-------------------------------------------------------
#UPDATE
def sql_insert_replace_comment(commentid,parentid,parent,comment,subreddit,time,score): #replaces comment if the score is higher
    try:
        sql = """UPDATE parent_reply SET parent_id = ?, comment_id = ?, parent = ?, comment = ?, subreddit = ?, unix = ?, score = ? WHERE parent_id =?;""".format(parentid, commentid, parent, comment, subreddit, int(time), score, parentid)
        transaction_bldr(sql)
    except Exception as e:
        print('s-UPDATE insertion',str(e))
#Insert - has Parent
def sql_insert_has_parent(commentid,parentid,parent,comment,subreddit,time,score): #insert comment if it has a parent
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(parentid, commentid, parent, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s-Parent insertion',str(e))

#Insert - No Parent
def sql_insert_no_parent(commentid,parentid,comment,subreddit,time,score): #insert comment with no parent
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}",{},{});""".format(parentid, commentid, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s-No_Parent insertion',str(e))
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------Checking if data length is acceptable-------------------------------------------
def acceptable(data): #checks if comment is acceptable (had less then 1000 words but more than 0
	if len(data.split(' ')) > 1000 or len(data) < 1:
		return False
	elif len(data) > 32000: #less then 32000 chars
		return False
	elif data == '[deleted]': #not deleted
		return False
	elif data == '[removed]': #not removed
		return False
	else:
		return True
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------Looking for Parent of a comment-------------------------------------------------
def find_parent(pid): #matches comment to a parent using the comment_id == parent_id
	try:
		sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
		c.execute(sql)
		result = c.fetchone()
		if result != None:
			return result[0]
		else:
			return False
	except Exception as e:
		#print("find_parent",e)
		return False
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------Checking Existing Score to compare it with new score----------------------------
def find_existing_score(pid): #find the score of  comment to check with a new score
	try:
		sql = "SELECT score FROM parent_reply WHERE parent_id = '{}' LIMIT 1".format(pid)
		c.execute(sql)
		result = c.fetchone()
		if result != None:
			return result[0]
		else:
			return False
	except Exception as e:
		#print("find_parent",e)
		return False
#----------------------------------------------------------End-----------------------------------------------------------------------------
#----------------------------------------------------------MAIN runs the code----------------------------------------------------------	
if __name__ == "__main__":
	create_table() #create table if none exists 
	row_counter = 0 #how many rows
	paired_rows = 0 #how many parent/child pairs
	with open("/run/media/tlivshits/Extra Space/Downloads/RC_{}/data".format(timeframe), buffering=1000, encoding = 'utf-8') as f: #opens file in external hard drive
		for row in f: #goes through each  row
			row_counter += 1

			if row_counter > start_row:
				try:
					row = json.loads(row)
					parent_id = row['parent_id'].split('_')[1] #gets the parent ID, might not work for other months
					comment_id = row['id'] #gets the comment ID, might not work for other months
					body = format_data(row['body']) #the body
					created_utc = row['created_utc'] #creation stamp
					score = row['score'] #score
					subreddit = row['subreddit'] #subreddit
					parent_data = find_parent(parent_id) #finds parent
					existing_comment_score = find_existing_score(parent_id) #gets score
					if existing_comment_score:
						if score > existing_comment_score:
							if acceptable(body):
								sql_insert_replace_comment(comment_id,parent_id,parent_data,body,subreddit,created_utc,score)
                                
					else:
						if acceptable(body):
							if parent_data:
								if score >= 2:
									sql_insert_has_parent(comment_id,parent_id,parent_data,body,subreddit,created_utc,score)
									paired_rows += 1
							else:
								sql_insert_no_parent(comment_id,parent_id,body,subreddit,created_utc,score)
				except Exception as e:
					print(str(e))
                            
			if row_counter % 100000 == 0:
				print('Total Rows Read: {}, Paired Rows: {}, Time: {}'.format(row_counter, paired_rows, str(datetime.now())))
#clean up for comments with no match
			if row_counter > start_row:
				if row_counter % cleanup == 0:
					print("Cleanin up!")
					sql = "DELETE FROM parent_reply WHERE parent IS NULL"
					c.execute(sql)
					connection.commit()
					c.execute("VACUUM")
					connection.commit()
#----------------------------------------------------------End--------------------------------------------------------------                
