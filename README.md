Restaurant Recommendation System

-> Overview

This is a simple restaurant recommendation system implemented in Python. The system recommends restaurants based on the user's food preference and location. The program uses a predefined dataset of restaurants categorized by different cuisines.

-> Files

restaurant_recommendation.py: This file contains the implementation of the RestaurantRecommendationSystem class, which handles restaurant recommendations based on user input.

test_recommendation.py: This file contains a test version of the RestaurantRecommendationSystem class for validation purposes. It includes the same restaurant dataset.

README.md: This file contains information and a detailed guide to setup and run the code and also gives an overview about the recommendation system and the algorithm it uses. 

-> Setup:

Follow these instructions to set up and run the program:

1. Clone the Repository:
git clone <repository-url>
cd restaurant-recommendation-system

2. Run the Program:
python restaurant_recommendation.py

******* For simplicity, this system assumes that all the users and restuarants exist on the 1-dimensional x-axis between the bounds 0 and 100 units. *******

3. Follow the Prompts:
Enter the type of food you desire when prompted. 
Enter your coordinate on the x-axis when prompted.

4. View Recommendations:
The program will display a list of recommended restaurants ranked on the basis of your preference and your location.

-> Data Structure

The restaurant data is structured as a dictionary, where each cuisine is a key mapping to a list of dictionaries representing individual restaurants. Each restaurant dictionary contains the name, rating, and location of the restaurant.

-> Recommendation Algorithm

The recommendation algorithm considers both the rating and proximity of the restaurants. It calculates a weighted score for each restaurant based on these factors and provides recommendations in according to this score.

-> Test Cases

The test_recommendation.py file provides a test version of the recommendation system. It includes various cuisines with multiple restaurants having different ratings and locations to ensure the robustness of the recommendation algorithm.

-> Additional Notes

The system handles invalid inputs gracefully, providing appropriate error messages and prompts. It can handle invalid inputs like unavailable food types, empty entries, invalid location, out-of-bound locations, etc.
The code structure separates concerns, making it easy to understand and maintain.
Feel free to modify the restaurant data or expand the program based on your requirements.




