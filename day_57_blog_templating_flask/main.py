from flask import Flask, render_template
from post import Post

app = Flask(__name__)


all_posts_info = Post()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_posts_info.all_posts)


@app.route('/<post_num>')
def get_posts(post_num):
    current_post = all_posts_info.get_current_post(int(post_num))
    return render_template('post.html', post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
