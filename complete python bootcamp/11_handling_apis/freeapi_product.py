import requests

def random_product_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        product_data = data["data"]
        product = product_data["brand"]
        category = product_data["category"]
        return product, category
    
    else:
        raise Exception("Faild to fetch product")
    
def main():
    try:
        product, category = random_product_freeapi()
        print(f"product: {product} \nCategory: {category}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()