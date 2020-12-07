from flask import Flask, render_template, redirect
import pymongo
import scraper_mars

# Create an instance of Flask
app = Flask(__name__)
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db

@app.route("/")
def home():
    mars = db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraping():
    main_dict = scraper_mars.scrape()
    db.mars.update({}, main_dict, upsert=True)
     
     # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)