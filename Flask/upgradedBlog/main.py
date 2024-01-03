from flask import Flask, render_template 
import requests

app = Flask(__name__) 

posts = requests.get('https://api.npoint.io/2317929deb05b627a909').json()

@app.route('/')
def get_all_post():
    print(posts)
    return render_template('index.html', all_posts = posts) 

@app.route('/about')
def go_to_about():
    return render_template('about.html')

@app.route('/contact')
def go_to_contact():
    return render_template('contact.html')

# @app.route('/posts/<int:id>')
# def one_post(id): 
#     for p in posts:
#         if p['id'] == id:
#             return render_template('post.html', content = p['body'])

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)