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

# minPercent = 90
# maxPercent = 110
# percentRange = maxPercent - minPercent
currentHour = math.floor(time() / (60 * 60)) # Python timestamp is in seconds
def calculateRandomizedPrice(userId, itemId, basePrice = base_price):
    random = createHourlyRandom(userId, itemId, currentHour)
    priceMultiplier = (90 + (random * 20)) / 100
    randomizedPrice = math.ceil(basePrice * priceMultiplier)
    return max(1, randomizedPrice)

cycles = int(input("How many cycles to run? (default 1000000): ") or "1000000")
print("Using base price", base_price)
for itemId in item_ids:
    prices = []
    for _ in range(cycles):
        userId = gen_user_id()
        prices.append(calculateRandomizedPrice(userId, itemId))
    print("max price:", max(prices), "min price:", min(prices), "avg price:", sum(prices) / len(prices))
    graph = []
    for i in range(round(base_price * 0.9), round(base_price * 1.1), round(base_price * 0.01)):
        graph.append(sum(1 for p in prices if p > i and p <= i + round(base_price * 0.01)) // (cycles // 200000))
    print("Price graph:\n" + "\n".join("█" * (g - min(graph) + 2) for g in graph))
