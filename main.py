import webapp2
import MySQLdb
import passwords
import random

conn = MySQLdb.connect(unix_socket = passwords.SQL_HOST,
user = passwords.SQL_USER,
passwd = passwords.SQL_PASSWD,
db = "gclouddatabase")


class MainPage(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("cookie_name") == None:
            id = "%032x" % random.getrandbits(128)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Session (sessionID) VALUES (%s);"%id)
            self.response.set_cookie("cookie_name",id, max_age=1800)
            self.response.headers["Content-Type"] = "text/html"
            self.response.write("Your cookie has been set")

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
