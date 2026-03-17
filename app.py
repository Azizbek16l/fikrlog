import hashlib

from flask import Flask, render_template, request, session, redirect
from articles import Article

app = Flask(__name__)
app.secret_key = "thisisverysecret"

# Authentication & Authorization
# AuthN & AuthZ
# Cookie
# hashing, sha256
users = {
    "admin": "ac9689e2272427085e35b9d3e3e8bed88cb3434828b43b86fc0596cad4c6e270"
    # parol: admin1234
}


articles = Article.all()


@app.route("/")
def blog():

    return render_template("blog.html", articles=articles)


@app.get("/admin")
def admin_page():
    if "user" in session:
        return "you alerady authenticated "

    return render_template("login.html")


@app.route("/logout")
def logout():
    del session["user"]
    return "logged out"


@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username not in users:
        return render_template("login.html", error="username/password incorrect")

    hashed = hashlib.sha256(password.encode()).hexdigest()

    if users[username] != hashed:
        return render_template("login.html", error="usernam/password incorrect")

    session["user"] = username
    return "you are authenticated"

"""
sessiya va cookie uchun kerak bolgandi 


@app.route("/set-session")
def set_session():
    session["user_id"] = 1
    return "session set"


@app.route("/get_session")
def get_session():
    return f"user_id {session['user_id']}"


@app.route("/first-time")
def first_time():
    if "seen" not in request.cookies:
        response = make_response("you are new here")
        response.set_cookie("seen", "1")
        return response

    seen = int(request.cookies["seen"])

    response = make_response(f"i have seen you berfore {seen} times")
    response.set_cookie("seen", str(seen + 1))
    return response

"""


@app.route("/blog/<slug>")
def article(slug: str):
    if slug not in articles:
        return 'articles not found',404
    article = articles[slug]
    return render_template("article.html", article=article)


@app.route("/publish")
def publish():
    if "user" not in session:
        return redirect("/admin")
    
    return render_template("publish.html")

    
if __name__ == "__main__":
    app.run(port=4200, debug=True)
