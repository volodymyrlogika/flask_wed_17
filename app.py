from flask import Flask, render_template
from sql_queries import BlogDB

app = Flask(__name__)

db = BlogDB("blog.db")

@app.route("/")
def index():
    categories = db.get_all_categories()
    posts = db.get_all_posts()
    print(posts)
    return  render_template("index.html", 
                            title = "Сайт про програмування",
                            posts = posts,
                            categories = categories)



@app.route("/logika")
def hello_logika():
    categories = db.get_all_categories()
    return render_template("post.html", categories = categories)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу