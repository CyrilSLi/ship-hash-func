from random import choice
from time import time
import math

item_ids = (
    "cmdci0w8v00fopc01j0izg77i", # Aug 11th Accommodation
    "cmdchz45j00fkpc01g8ekc1tv", # Aug 7th Accommodation
    "cmd7in0r4000kro01x3l2c1v8" # Travel Stipend
)
def gen_user_id():
    return "".join(choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(25))
base_price = 1000

def createHourlyRandom(userId, itemId, hour):
    combined = f"{userId}-{itemId}-{hour}"
    hash = 0
    for char in combined:
        hash = ((hash << 5) - hash) + ord(char)
        hash = hash % 2**31 # Equivalent of hash = hash & hash in JS
    return abs(hash) / 2147483647

# minPercent = 100
# maxPercent = 110
# percentRange = maxPercent - minPercent
def calculateRandomizedPrice(userId, itemId, currentHour, basePrice = base_price):
    random = createHourlyRandom(userId, itemId, currentHour)
    priceMultiplier = (100 + (random * 10)) / 100
    randomizedPrice = math.ceil(basePrice * priceMultiplier)
    return max(1, randomizedPrice)

userId = gen_user_id()
for itemId in item_ids:
    curr_hour = 0
    prices = []
    while curr_hour < 1000000:
        curr_price = calculateRandomizedPrice(userId, itemId, curr_hour)
        price = curr_price
        while curr_price == price:
            curr_hour += 1
            curr_price = calculateRandomizedPrice(userId, itemId, curr_hour)
        print(f"Item ID: {itemId}, Hour: {curr_hour}, Current Price: {curr_price}, Previous Price: {price} ")
