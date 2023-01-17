import mysql.connector as sql

# import hashlib as hb
# def hash(l):
#     hashed_list = []
#     for i in l:
#         hashed_string = hb.sha256(i.encode ('utf-8')).hexdigest()
#         hashed_list.append(hashed_string)
#     return hashed_list

db_conn = sql.connect(host="localhost", user="root", password="onepieceisreal", database="sys")
cursor = db_conn.cursor()
db_conn.autocommit = True

# cursor.execute("UPDATE students SET DSAScore=84 WHERE Username='jakethesimp'")
# cursor.execute("UPDATE students SET DSAScore=80 WHERE Username='rifahjindal'")
# db_conn.commit()

def db(sql_query, retrieve):
    try:
        # db_conn = sql.connect(host="localhost", user="root", password="onepieceisreal", database="sys")
        # cursor = db_conn.cursor()
        cursor.execute(sql_query)
        if retrieve==1: 
            return cursor.fetchall()
        else: 
            #db_conn.commit()
            return
    except: 'Error'   
    
def returnInfo(username,password,type):
    sql_query1 = f"SELECT EXISTS(SELECT Username FROM {type} WHERE Username='{username}' AND Passwd='{password}')"
    isPresent = db(sql_query1,1)
    if(isPresent[0][0]==0):
        return "User not found!"
    sql_query2 = f"SELECT * from {type} WHERE Username='{username}' AND Passwd='{password}'"
    data = db(sql_query2,1)
    return data

def formatInfo(data,type):
    hashmap = {}
    hashmap['Name'] = data[0][0]
    hashmap['Username'] = data[0][1]
    hashmap['Password'] = data[0][2]
    hashmap['Email'] = data[0][3]
    hashmap['Gender'] = data[0][4]
    if type=='students':
        hashmap['DSA score'] = data[0][5]
        hashmap['DSAI score'] = data[0][6]
    else:
        hashmap['Company Name'] = data[0][5]
        hashmap['Company ID'] = data[0][6]
    return hashmap

def generateLeaderboard(topic):
    topic = topic+'Score'
    query = f"SELECT Username,{topic} from students ORDER BY {topic} DESC"
    data = db(query,1)
    return data
    
def updateLeaderboard(username1,username2,topic):
    topic = topic+'Score'
    query1 = f"SELECT {topic} from students WHERE Username='{username1}'"
    winnerScore = db(query1,1)
    winnerScore = winnerScore[0][0]
    winnerScore+=7
    query2 = f"SELECT {topic} from students WHERE Username='{username2}'"
    loserScore = db(query2,1)
    loserScore = loserScore[0][0]
    loserScore-=3
    print(winnerScore)
    print(loserScore)
    query3 = f"UPDATE students SET {topic}={winnerScore} WHERE Username='{username1}'"
    query4 = f"UPDATE students SET {topic}={loserScore} WHERE Username='{username2}'"
    db(query3,0)
    db(query4,0)
    
    


updateLeaderboard('jakethesimp','rifahjindal','DSA')

# topic = 'DSAI'
# leaderboard = generateLeaderboard(topic)
# print(leaderboard)

# type = 'recruiters'
# info = returnInfo('johndoe','ABEAB588ED6BB5FAF1254C123B12D4E8A1E91995D988CADD987C9FBA7800EF7E',type)
# info = formatInfo(info,type)
# print(info)
