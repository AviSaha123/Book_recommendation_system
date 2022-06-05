from flask import Flask , render_template
import pickle

popularity_df = pickle.load(open('popularity_df', 'rb'))

app = Flask(__name__) 

@app.route('/')

def index():
    return render_template('index.html',
                           book_name = list(popularity_df['Book-Title'].values),
                           book_author=list(popularity_df['Book-Author'].values),
                           image_url=list(popularity_df['Image-URL-M'].values),
                           votes=list(popularity_df['Number_of_ratings'].values),
                            ratings = list(popularity_df['avg_ratings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')
    
if __name__ == '__main__':
    app.run(debug= True)
