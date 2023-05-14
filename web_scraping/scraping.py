import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import time
from pathlib import Path
import json



def fscraping(file_path):
    """
        It is helps to extract the data from given url.\n
        :param: file_path
        :return: data
    """
    try:

        with open(file_path, 'r') as f: # load the json file data
            file = f.read()
        file = json.loads(file)

        for key, value in file.items(): # extract the information from given url one-by-one
            for i in range(1, 36):
                # mentions list for storing the info.
                book_name_lst = []
                author_lst = []
                book_img_lst = []
                price_lst = []
                ratings_lst = []
                no_books_purchases_lst = []
                # get the url one-by-one:
                url_ = value+str(i)
                url = requests.get(url_)
                soup = bs(url.text, 'html.parser')

                # boxes:
                all_boxes = soup.findAll('div', class_="_4ddWXP")

                for box in all_boxes:
                    # for books:
                    all_book_names = box.findAll("a", class_= "s1Q9rs")
                    if len(all_book_names) !=0:
                        for book in all_book_names:
                            book_name_lst.append(book['title'])
                    else:
                        book_name_lst.append(None)

                    # for author:
                    all_author_names = box.findAll("div", class_= "_3Djpdu")
                    if len(all_author_names) !=0:
                        for author in all_author_names:
                            author_lst.append(author.text)
                    else:
                        author_lst.append(None)

                    # for books images:
                    all_book_imgs = box.findAll("img", class_= "_396cs4")
                    if len(all_book_imgs):
                        for img in all_book_imgs:
                            book_img_lst.append(img['src'])
                    else:
                        book_img_lst.append(None)

                    # for book price:
                    all_book_prices = box.findAll('div', class_='_30jeq3')
                    if len(all_book_prices):
                        for price in all_book_prices:
                            price_lst.append(price.text)
                    else:
                        price_lst.append(None)

                    # for book ratings:
                    all_book_ratings = box.findAll('div', class_='_3LWZlK')
                    if len(all_book_ratings) != 0:
                        for ratings in all_book_ratings:
                            ratings_lst.append(ratings.text)
                    else:
                        ratings_lst.append(None)

                    # for total no. of books purchase:
                    all_book_no_purchases = box.findAll('span', class_='_2_R_DZ')
                    if len(all_book_no_purchases) !=0:
                        for n in all_book_no_purchases:
                            no_books_purchases_lst.append(n.text)
                    else:
                        no_books_purchases_lst.append(None)

                # store all result as dict:
                dct = {
                    "book_title": book_name_lst,
                    "author": author_lst,
                    "img": book_img_lst,
                    "price": price_lst,
                    "ratings": ratings_lst,
                    "no_of_purchase": no_books_purchases_lst
                }
                # convert the dict to DataFrame
                df = pd.DataFrame(dct)
                df['url'] = url_ # mention the url
                df['genre'] = key # mention the genre/ category

                print(key)
                print(url_, '\n')

                # save the data in a directory as a .csv format:
                path = "../RawData/"+f"{str(time.strftime('%Y%m%d--%H%M%S'))}--{key}--{i}.csv"
                filepath = Path(path)
                df.to_csv(path, index=False)

    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':

    fscraping(file_path="../books_data.json")
