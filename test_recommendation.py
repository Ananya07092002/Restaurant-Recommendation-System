import unittest
from restaurant_recommendation import RestaurantRecommendationSystem

class TestRestaurantRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.recommendation_system = RestaurantRecommendationSystem()

    def test_valid_recommendation(self):
        recommendations = self.recommendation_system.recommend_restaurants("Italian", 1)
        self.assertEqual(recommendations, ['Amici Cafe', 'Amalfi', 'Tonino Ristorante', 'Sorrento', 'San Gimignano Restaurant', 'FIO - Cookhouse & Bar'])
        
    def test_invalid_foodtype(self):
        with self.assertRaises(ValueError):
            self.recommendation_system.recommend_restaurants("dkjcnwae", 47)

    def test_empty(self):
        with self.assertRaises(ValueError):
            self.recommendation_system.recommend_restaurants("", 0)

    def test_invalid_userlocation(self):
        with self.assertRaises(ValueError):
            self.recommendation_system.recommend_restaurants("French", "2e")

if __name__ == "__main__":
    unittest.main()