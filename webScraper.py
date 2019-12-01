from  urllib.request import urlopen
from bs4 import BeautifulSoup

def get_reviews_from_one_page(review_blocks, review_rating):
    for block in review_blocks: 
        review = block.find("p", {"class": "review-text"}).text  #getting the text of the review
        rating = int(block.findAll("div", attrs ={"class": "ratings active"})[0].attrs['style'].split()[1][:-1])/20 # 1 star == width: 20%
        review_rating.append((review, rating))


def get_reviews(url):
    pagin = 1
    review_rating = [] # list of tuples. Each tuple contains (review, rating)
    while True:
        page = urlopen (url + '-yorumlari?sayfa=%g'%pagin)
        soup = BeautifulSoup(page, "html5lib") 
        review_blocks = soup.find_all("li", {"class": "review-item"}) #getting all blocks of reviews (listed reviews)
        get_reviews_from_one_page(review_blocks, review_rating) 
        if len(review_blocks) < 20: # each page contains 20, so if a page is less than 20, break.
            break
        pagin+= 1 # incrementing to get the reviews from the the next page
    return review_rating

    

#Example: 

# url = 'https://www.hepsiburada.com/polaris-91-356071-m-gri-erkek-klasik-ayakkabi-p-HBV00000IU35R'
# reviews = get_reviews(url)
# print(reviews)
# print(len(reviews))
