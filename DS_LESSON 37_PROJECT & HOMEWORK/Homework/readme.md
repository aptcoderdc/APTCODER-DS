# Movie Recommendation System

## Overview
This project implements a movie recommendation system using content-based filtering and user preferences. The system analyzes movie descriptions and user ratings to suggest movies that are similar to ones the user has liked.

## Files
- `movie_recommendation.py`: Python script containing the code for the recommendation system.
- `movies.csv`: Sample dataset containing movie information including title, genre, director, and description.
- `ratings.csv`: Sample dataset containing user ratings for movies.

## Dependencies
- Python 3
- pandas
- scikit-learn

## Usage
1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install pandas scikit-learn`.
3. Place the `movies.csv` and `ratings.csv` files in the same directory as the `movie_recommendation.py` script.
4. Run the script using `python movie_recommendation.py`.
5. Enter a user ID when prompted to receive personalized movie recommendations based on the user's preferences.

## How It Works
1. The system first loads the movie data and user ratings from the CSV files.
2. It then converts the movie descriptions into numerical vectors using TF-IDF vectorization.
3. Cosine similarity is calculated between all pairs of movies based on their descriptions.
4. For a given user, the system identifies movies the user has rated and finds similar movies based on those ratings and the calculated cosine similarity.
5. The system recommends movies to the user that they have not yet rated but are similar to movies they have liked.

## Example
Suppose a user with ID 1 has rated "The Shawshank Redemption" and "The Godfather" highly. The system will recommend similar movies to these based on their descriptions and the user's preferences.

## Future Improvements
- Incorporate more advanced recommendation algorithms such as collaborative filtering.
- Enhance the user interface for better interaction and visualization.
- Explore larger and more diverse datasets for improved recommendations.