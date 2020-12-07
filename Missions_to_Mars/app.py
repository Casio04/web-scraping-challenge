from flask import Flask, render_template, redirect
import pymongo
import scraper_mars

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def scraping():
    mars_data = scraper_mars.scrape()

     # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)