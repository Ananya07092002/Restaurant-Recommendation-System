import random

class RestaurantRecommendationSystem:

    def __init__(self):
        self.restaurant_data = {
            "Italian": [
                {"name": "Tonino Ristorante", "rating": 4.4, "location": 65},
                {"name": "FIO - Cookhouse & Bar", "rating": 1, "location": 37},
                {"name": "Amalfi", "rating": 4.5, "location": 18},
                {"name": "San Gimignano Restaurant", "rating": 2.3, "location": 91},
                {"name": "Sorrento", "rating": 3.5, "location": 74},
                {"name": "Amici Cafe", "rating": 4.8, "location": 23},
            ],
            "Mexican": [
                {"name": "Just Mex It", "rating": 3.6, "location": 23},
                {"name": "Chili's", "rating": 2.8, "location": 57},
                {"name": "Rodeo: Cantina & Kitchen", "rating": 4.0, "location": 34},
                {"name": "Miss Margarita", "rating": 1.6, "location": 25},
                {"name": "California Burrito Mexican Grill", "rating": 5.0, "location": 63},
                {"name": "Zaga - Courtyard Dining", "rating": 0.5, "location": 82},
            ],
            "Indian": [
                {"name": "Masala Library by Jiggs Kalra", "rating": 2.5, "location": 28},
                {"name": "Pindi Restaurant", "rating": 4.3, "location": 98},
                {"name": "Baluchi - A Pan Indian Destination", "rating": 4.9, "location": 67},
                {"name": "Indian Acent", "rating": 3.9, "location": 49},
                {"name": "Veda Restaurant", "rating": 1.8, "location": 65},
                {"name": "The GT Road", "rating": 4.6, "location": 26}
            ],
             "Japanese": [
                {"name": "Mount Fuji", "rating": 2.7, "location": 47},
                {"name": "Wasabi by Morimoto", "rating": 1, "location": 59},
                {"name": "Guppy", "rating": 4.5, "location": 40},
                {"name": "Megu Restaurant", "rating": 3.9, "location": 92},
                {"name": "Kofuku", "rating": 4.9, "location": 83},
                {"name": "Yum Yum Cha", "rating": 5.0, "location": 19}
            ],
             "French": [
                {"name": "Bistro Francais", "rating": 4.5, "location": 29},
                {"name": "Le Cirque", "rating": 1, "location": 50},
                {"name": "Q Bistro Cafe and Patisserie", "rating": 2.5, "location": 18},
                {"name": "Chateau de Pondicherry", "rating": 5.0, "location": 98},
                {"name": "Le Bistro du Parc", "rating": 2.6, "location": 59},
                {"name": "Reve Bistro Moderne", "rating": 4.5, "location": 15}
            ],
             "Chinese": [
                {"name": "Hakka House Asian Fusion Food", "rating": 4.7, "location": 23},
                {"name": "Wok in the Clouds", "rating": 3.4, "location": 56},
                {"name": "House of Ming", "rating": 3.5, "location": 78},
                {"name": "Drums of Heaven", "rating":4.2, "location": 87},
                {"name": "Spicy Duck", "rating": 4.5, "location": 55},
                {"name": "Larry's China Restaurant", "rating": 3.6, "location": 88}
            ],
             "Korean": [
                {"name": "Seoul Restaurant", "rating": 3.4, "location": 22},
                {"name": "Busan Korean Restaurant", "rating": 1.5, "location": 47},
                {"name": "Gung The Palace", "rating": 3.8, "location": 99},
                {"name": "Kori's", "rating": 4.1, "location": 12},
                {"name": "Kim Korean", "rating": 2.2, "location": 34},
                {"name": "Kim Chi Korean Restaurant", "rating": 4.7, "location": 32}
            ],
             "Mediterranean": [
                {"name": "The Ivy", "rating": 4.5, "location": 21},
                {"name": "Olive Bar and Kitchen", "rating": 3, "location": 10},
                {"name": "Zawadah", "rating": 2.5, "location": 53},
                {"name": "Baris", "rating": 2.4, "location": 60},
                {"name": "Ladera", "rating": 4.4, "location": 79},
                {"name": "Fez", "rating": 3.5, "location": 58}
            ],
             "Spanish": [
                {"name": "Sevilla", "rating": 4.5, "location": 45},
                {"name": "Qla", "rating": 2, "location": 17},
                {"name": "Reve", "rating": 3.3, "location": 7},
                {"name": "Bohca", "rating": 5, "location": 25},
                {"name": "Chez Jerome", "rating": 3.5, "location": 52},
                {"name": "Rodeo", "rating": 4.1, "location": 38}
            ],
             "Thai": [
                {"name": "Thai High", "rating": 4.6, "location": 85},
                {"name": "Bo Tai", "rating": 2.7, "location": 31},
                {"name": "Neung Roi", "rating": 3.6, "location": 62},
                {"name": "Dao", "rating": 2.7, "location": 72},
                {"name": "Pa Pa Ya", "rating": 1.5, "location": 69},
                {"name": "ThaiCrate", "rating": 3.2, "location": 11}
            ]
        }

    def recommend_restaurants(self, food_type, user_location):
        try:
            cuisine_data = self.restaurant_data[food_type]

            for rest in cuisine_data:
                rest["location"] = 101.0 - abs(rest["location"] - float(user_location))

            sorted_cuisine_data = sorted(cuisine_data, key=lambda x: (x["rating"], x["location"]), reverse=True)
            recommendations = [restaurant["name"] for restaurant in sorted_cuisine_data]
            return recommendations

        except KeyError:
            raise ValueError(f"No restaurants found for the cuisine: {food_type}")

def main():

    recommendation_system = RestaurantRecommendationSystem()
    v=0
    while v==0:
        user_input = input("Enter the type of food you desire: ")
        if user_input=="":
            print("Food preference cannot be empty, please try again.")
        else:
            v = 1
    x = 0
    y = 0
    while x == 0:
        while y==0:
            location = input("Enter your location(x-axis coordinate): ")
            if location=="":
                print("Location cannot be empty, please try again.")
            else:
                y = 1
        try:
            float(location)
            if 0 <= float(location) <= 100:
                x = 1
            else:
                print("Please provide a number between 0 and 100.")
        except ValueError:
            print("Please provide a valid number.")

    try:
        recommendations = recommendation_system.recommend_restaurants(user_input, location)
        print(f"Recommended restaurants for {user_input}: ")
        x = 1
        for i in recommendations:
            print(str(x) + " - " + i)
            x += 1
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()