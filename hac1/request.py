import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'book_title':'', 'book_image_url':'', 'book_desc':'', "book_genre":'', "book_authors":'',"book_pages":'',"book_review_count":1,"book_rating_count":1})

print(r.json())