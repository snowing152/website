from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "mysecretkey"

maksim_movies = {
    "id": 1,
    "username": "maksim",
    "data": "09.14.2024",
    "movies": ["Iron-Man🏳️‍🌈", "The-Boys💕", "Interstellar🫃🏿", "Avengers👨🏿‍❤️‍💋‍👨🏿", "Once in Hollywood💩"]
}
vadim_movies = {
    "id": 1,
    "username": "vadim",
    "data": "09.14.2024",
    "movies": ["Iron-Man🏳️‍🌈", "The-Girls💕", "IntersteLLAar🫃🏿", "Ovenngers👨🏿‍❤️‍💋‍👨🏿", "Once in Hollywood💩"]
}


@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html", name=session["username"])

    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        session["username"] = request.form["username"]
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("home"))


@app.route("/movie")
def movie():
    return render_template("index.html", movies=my_fav_movies)


@app.route("/movies/<username>")
def help(username):
    if username == "maksim":
        return render_template("index.html", movies=maksim_movies)
    if username == "vadim":
        return render_template("index.html", movies=vadim_movies["movies"])


app.run(port=8000, debug=True)
