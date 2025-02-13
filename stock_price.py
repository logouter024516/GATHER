from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
import time
load_dotenv()  # .env 파일 로드
MONGO_URI = os.getenv("MONGO_URI")
# MongoDB 클라이언트 설정
client = MongoClient(MONGO_URI)
userdb = client["user"]  # 데이터베이스 이름
user_collection = userdb["user"]

stockdb = client["stocks"]
stock_domestic_collection = stockdb["domestic"]
stock_international_collection = stockdb["international"]
gmtodt_collection = stockdb["gmtodt"]
def int_stock_price(stock_name,price,rate):
    return_price = int(price*rate)
    if return_price == 0:
        stock_international_collection.update_one({"company_name": stock_name}, {"$set": {"price": int(15)}})
        stock_international_collection.update_one({"company_name": stock_name}, {"$set": {"rate": rate}})
    else:
        stock_international_collection.update_one({"company_name":stock_name}, {"$set":{"price":int(return_price)}})
        stock_international_collection.update_one({"company_name": stock_name}, {"$set": {"rate": rate}})
    return return_price
def dom_stock_price(stock_name,price,rate):
    return_price = int(price*rate)
    if return_price == 0:
        stock_domestic_collection.update_one({"company_name": stock_name}, {"$set": {"price": int(50000)}})
        stock_domestic_collection.update_one({"company_name": stock_name}, {"$set": {"rate": rate}})
    else:
        stock_domestic_collection.update_one({"company_name":stock_name}, {"$set":{"price":int(return_price)}})
        stock_domestic_collection.update_one({"company_name": stock_name}, {"$set": {"rate": rate}})
def gmtodt_price():
    return_price = random.randint(900, 1500)
    gmtodt_collection.update_one({"codecheck":"code"}, {"$set":{"gmtodt":int(return_price)}})
while(True):
    sasungin = stock_international_collection.find_one({"company_name": "SASUNG"})["price"]
    pear = stock_international_collection.find_one({"company_name": "PEAR"})["price"]
    envidia = stock_international_collection.find_one({"company_name": "ENVIDIA"})["price"]
    hiot = stock_international_collection.find_one({"company_name": "HIOTGAMES"})["price"]
    qalmart = stock_international_collection.find_one({"company_name": "QALMART"})["price"]
    ppizer = stock_international_collection.find_one({"company_name": "PPIZER"})["price"]
    sasungdo = stock_domestic_collection.find_one({"company_name": "SASUNG"})["price"]
    og = stock_domestic_collection.find_one({"company_name": "OG"})["price"]
    jongshim = stock_domestic_collection.find_one({"company_name": "jongshim"})["price"]
    lyundai = stock_domestic_collection.find_one({"company_name": "lyundai"})["price"]
    gmtodt = gmtodt_collection.find_one({"codecheck": "code"})["gmtodt"]
    print(sasungin, pear, envidia, hiot, qalmart, ppizer, sasungdo, og, jongshim, lyundai)
    rate = random.randint(80, 130) / 100
    sasungin = int_stock_price("SASUNG",sasungin, rate)
    rate = random.randint(80, 130) / 100
    pear = int_stock_price("PEAR",pear, rate)
    rate = random.randint(80, 130) / 100
    envidia = int_stock_price("ENVIDIA",envidia, rate)
    rate = random.randint(80, 130) / 100
    hiot = int_stock_price("HIOTGAMES",hiot, rate)
    rate = random.randint(80, 130) / 100
    qalmart = int_stock_price("QALMART",qalmart, rate)
    rate = random.randint(80, 130) / 100
    ppizer = int_stock_price("PPIZER",ppizer, rate)
    rate = random.randint(80, 130) / 100
    sasungdo = dom_stock_price("SASUNG",sasungdo, rate)
    rate = random.randint(80, 130) / 100
    og = dom_stock_price("OG",og, rate)
    rate = random.randint(80, 130) / 100
    jongshim = dom_stock_price("jongshim",jongshim, rate)
    rate = random.randint(80, 130) / 100
    lyundai = dom_stock_price("lyundai",lyundai, rate)
    rate = random.randint(80, 130) / 100
    gmtodt = gmtodt_price()
    time.sleep(60)

