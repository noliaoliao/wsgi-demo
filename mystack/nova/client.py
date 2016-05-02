#!/usr/bin/env python

import MySQLdb
import md5
import uuid
import random
import string

class MySQLClient(object):
    def __init__(self, host='localhost', db='mystack', user='root',
                passwd='123456', port=3306):
        try:
            self.connection = MySQLdb.Connection(host = host, db = db,
                                            user = user, passwd = passwd,
                                            port = port)
            self.current = self.connection.cursor()

        except MySQLdb.Error,e:
             print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    def __del__(self):
        self.current.close()
        self.connection.close()
        print "__del__"
    
    def execute(self,sql):
        try:
            self.current.execute(sql)
            self.connection.commit()
        except:
            self.connection.rollback()

    def fetchone(self):
        return self.current.fetchone()

    def fetchall(self):
        return self.current.fetchall()
        
def createTable(client):
    sql = """crate table user(
                uid CHAR(36) NOT NULL PRIMARY KEY,
                username CHAR(30),
                userpasswd CHAR(32))"""
    client.execute(sql)

def insertData(client):
    id = uuid.uuid4().hex
    username = ''.join(random.sample(string.ascii_letters,8))
    passwd = ''.join(random.sample(string.ascii_letters,8))
    encode = md5.new()
    encode.update(passwd)
    userpasswd = encode.hexdigest()

    sql = "insert into user values(\""+id+"\",\""+username+"\",\""+userpasswd+"\")"
    client.execute(sql) 

def updateData(client):
    sql = "update user set userpasswd = \"null\" where username = \"lyh\""
    #print sql
    client.execute(sql)

def deleteData(client):
    sql = "delete from user where username = \"lyh\""
    #print sql
    client.execute(sql)

if __name__ == "__main__":
    client = MySQLClient(host='localhost', db='mystack', user='root', passwd='liao123')
    #createTable(client)
    insertData(client)
    #updateData(client)
    deleteData(client)
