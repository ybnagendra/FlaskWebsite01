from flask import  Flask, render_template

app= Flask(__name__)

all_posts=[
    {
        'title':'Post 1',
        'content':'This is the content of post1. lalala',
        'Author':'Nagendra'
    },
    {
        'title':'Post 2',
        'content':'This is the content of post2. lalala'
    },
    {
        'title':'Post 3',
        'content':'This is the content of post3. lalala',
    },
    {
        'title':'Post 4',
        'content':'This is the content of post4. lalala',
        'Author':'Nagendra'
    },
    {
        'title':'Post 5',
        'content':'This is the content of post5. lalala',
        'Author':'Nagendra'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html',post=all_posts)     # post/anyname


if __name__=="__main__":
    app.run(debug=True)
