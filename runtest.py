############################
# Programming test
# 29/04/2016
# author: Dennis Decoene
#
# Make sure the mysql root user has access from all hosts!
############################

import getpass
import json
import os
import time
import urllib2

import MySQLdb

import settings

def writeToMsyql(readjson):
    try:
        m = MySQLdb.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER, passwd=settings.MYSQL_PWD,
                            db=settings.MYSQL_DB)

        curs = m.cursor()

        for post in readjson:
            for key in post.keys():
                print '%s: %s' % (key, post[key])

            sql = 'INSERT INTO posts (id, userId, body, title) VALUES (%s,%s,%s,%s);'

            try:
                curs.execute(sql, (
                    post['id'], post['userId'], '%s %s' % (post['body'], settings.EXTRA_STRING), post['title']))

            except MySQLdb.Error, e:

                m.rollback()

                try:
                    print "----- MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except IndexError:
                    print "----- MySQL Error: %s" % str(e)
            else:
                m.commit()

    except MySQLdb.Error, e:
        try:
            print "----- MySQL Error [%d]: %s" % (e.args[0], e.args[1])
        except IndexError:
            print "----- MySQL Error: %s" % str(e)


def writeToFiles(readjson):
    for post in readjson:
        try:
            userdir = os.path.join(os.path.dirname(__file__), 'userId_%s' % post['userId'])
            # print userdir

            if not os.path.exists(userdir):
                os.mkdir(userdir)

            filename = os.path.join(userdir, 'post_%s.json' % post['id'])
            print filename

            try:
                with open(filename, "w") as outfile:
                    json.dump(post, outfile, indent=4)
            except e:
                print "----- File '%s' gave error: %s", (filename, str(e))

        except os.error, e:
            print "----- Error: %s" % (str(e))


if __name__ == "__main__":
    start_time = time.time()

    data = urllib2.urlopen(settings.JSON_SOURCE).read()
    readJson = json.loads(data)
    print readJson

    writeToMsyql(readJson)

    writeToFiles(readJson)

    print "\n\n-----------------------------------"
    print "Run as user: %s" % (getpass.getuser())
    print "Run Time: %s seconds ---" % (time.time() - start_time)
    print "-----------------------------------"
