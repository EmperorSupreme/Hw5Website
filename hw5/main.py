import flask
app = flask.Flask(__name__)

favorite =["One Piece", "Avatar the Last Airbender","Naruto","Rick and Morty", "Doraemon"]
Images = [
    "https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
    "https://images.wallpapersden.com/image/wxl-smite-x-aang-avatar-4k_71723.jpg",
    "https://cdn.shopify.com/s/files/1/0501/2756/9071/products/product-image-569702902_2048x2048_fe1fbbee-1de1-4b64-bc1b-e717041b7da6_900x.jpg?v=1602443357",
    "https://images.wallpapersden.com/image/wxl-rick-and-morty-in-outer-space_72696.jpg",
    "https://eskipaper.com/images/doraemon-15.jpg",

]

@app.route('/')
def index():
    return flask.render_template("index.html", 
    len = len(favorite), favorite = favorite, Images =Images )
  
   

app.run(use_reloader = True, debug = True)