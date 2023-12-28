from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__) 

def request_url(url):
    all_posts = requests.get(url).json()
    post_obj = []
    for p in all_posts:
        post = Post(p["id"], p["title"], p["subtitle"], p["body"])
        post_obj.append(post) 
    return post_obj

all_posts = request_url("https://api.npoint.io/c790b4d5cab58020d391")

@app.route('/')
def index():
    return render_template("index.html", posts=all_posts)

@app.route('/posts/<int:index>')
def show_post(index):   
    requested_post = None
    for p in all_posts:
        if p.id == index:
            requested_post = p
    return render_template('post.html', post = requested_post)


if __name__ == '__main__':
    app.run(debug=True)

