import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset of movies
movies = pd.DataFrame({
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama'],
    'director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino', 'Robert Zemeckis'],
    'description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 
                    'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 
                    'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', 
                    'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 
                    'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.']
})

# Sample dataset of user ratings
ratings = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3],
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Shawshank Redemption', 'Pulp Fiction', 'The Dark Knight'],
    'rating': [5, 4, 4, 5, 4]
})

# Merge ratings with movies
movie_ratings = pd.merge(movies, ratings, on='title')

# Convert the text data into numerical vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['description'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on similarity and user preferences
def recommend_movies(user_id, cosine_sim=cosine_sim):
    user_ratings = movie_ratings[movie_ratings['user_id'] == user_id]
    user_movie_indices = user_ratings.index.tolist()
    
    recommended_movies = []
    for idx in user_movie_indices:
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        recommended_movies.extend(movie_ratings['title'].iloc[movie_indices])
    
    return list(set(recommended_movies) - set(user_ratings['title']))

# Test the recommender system for a user
user_id = 1
recommended_movies = recommend_movies(user_id)
print(f"Recommended movies for user {user_id}:")
print(recommended_movies)
