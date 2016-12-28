from chopper import app, g
import sqlite3
import time


@app.before_task
def db_connect():
    g.db = sqlite3.connect('/tmp/example.db')
    print "db: %s" % str(id(g.db))
    print "func: %s" % str(g.func)


@app.after_task
def db_disconnect():
    g.db.close()


def test1(*args):
    time.sleep(2)
    print "hello %s" % str(args)


def test2(*args):
    time.sleep(2)
    print "hello %s" % str(args)


def test3(*args):
    time.sleep(2)
    print "hello %s" % str(args)


def test4(*args):
    time.sleep(2)
    print "hello %s" % str(args)


a = {
    'test1': test1,
    'test2': test2,
    'test3': test3,
    'test4': test4,
}

for func in a.values():
    app.put_tasks(func, 'a', 'b')

app.run()
