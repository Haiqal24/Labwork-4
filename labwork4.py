"""
    Program Purpose: To analyst working for a flower shop that offers a wide variety of floral arrangements and bouquets
    Programmer: Haiqal
    Date: 8 March 2024
"""
def calculate_total_units_sold(units_sold):

    return sum(units_sold)

def find_highest_sales_flower(flower_names, units_sold):
    #Determine the flower with the highest sales.#
    highest_sales_index = units_sold.index(max(units_sold))
    return flower_names[highest_sales_index]

def find_above_average_flowers(flower_names, customer_reviews):
    #Identify flowers with average customer reviews above 3
    above_average_flowers = [flower_names[i] for i in range(len(customer_reviews)) if customer_reviews[i] > 3]
    return above_average_flowers

def calculate_average_review_score(customer_reviews):
    #Calculate average customer reviews score for all flowers
    if not customer_reviews:
        return None
    return sum(customer_reviews) / len(customer_reviews)

def find_below_average_sales(flower_names, units_sold, customer_reviews):
    #Identify flowers below-average sales
    if not units_sold:
        return None
    average_units_sold = sum(units_sold) / len(units_sold)
    below_average_flowers = [(flower_names[i], units_sold[i], customer_reviews[i]) for i in range(len(units_sold)) if units_sold[i] < average_units_sold]
    return below_average_flowers

# Provided dataset
flower_names = ["Rose","Lily","Daffodil","Sunflower","Daisy","Orchid","Carnation","Hydrangea","Peony","Gerbera","Chrysanthemum","Freesia","Gardenia","Lavender","Anemone","Peony","Marigold","Tulips","Zinnia","Dahlia"]
units_sold = [150, 200, 100, 75, 250,150,120,80,200,100,90,70,110,60,40,130,85,95,55,75]
customer_reviews = [4.5, 3.8, 2.2, 4.0, 3.5,5.0,3.0,4.0,4.6,3.9,4.9,3.0,2.9,3.4,4.0,3.7,2.5,4.5,3.3,4.7]

# Task 1: Total Units Sold Calculation
total_units_sold = calculate_total_units_sold(units_sold)
print()
print("Total Units Sold for all flowers:", total_units_sold)

# Task 2: Highest Sales Identification
highest_sales_flower = find_highest_sales_flower(flower_names, units_sold)
print()
print("Flower with the highest sales:", highest_sales_flower)
print()
# Task 3: Above-Average Customer Reviews Identification
above_average_flowers = find_above_average_flowers(flower_names, customer_reviews)
print("Flowers with above-average customer reviews:", above_average_flowers)

# Task 4: Average Customer Review Score Calculation
average_review_score = calculate_average_review_score(customer_reviews)
if average_review_score is not None:
    print()
    print("Average Customer Review Score:", average_review_score)
else:
    print("Error: No customer reviews available.")

# Task 5: Below-Average Sales Identification
below_average_sales = find_below_average_sales(flower_names, units_sold, customer_reviews)
if below_average_sales:
    print()
    print("Flowers with below-average sales:- ")
    print()
    for flower in below_average_sales:
        print("(Type flower) :", flower[0], "- (Units Sold):", flower[1], "- (Customer Reviews):", flower[2])
else:
    print("Error: No sales data available.")

