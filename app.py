from flask import Flask, render_template, url_for, request
import watson, os, json, twitter_scraper

# initialize Flask App
app = Flask(__name__)
app.debug = True
port = int(os.getenv('PORT', 8000))

# create a page route
@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')


@app.route('/data', methods=['POST'])
def _index():

	# get the hashtag from the client-side
	hashtag = request.form['hashtag']
	latitude = request.form['lat']
	longitude = request.form['lng']

	if latitude == "" or longitude == "":
		tweets = twitter_scraper.get_tweets(str(hashtag))
	else:
		geocode = latitude + "," + longitude + ",100km"
		tweets = twitter_scraper.get_tweets(str(hashtag), geocode=geocode, location=True)

	# pass the request to, tweets scraper and then watson
	try:
		english_tweets = watson.get_language_translator_results(tweets)
		results = watson.get_tone_analyser_results(english_tweets)
		data = watson.display_emotion_tone(results)

	except:
		return

	# return the data to the client-side
	return json.dumps(data)

if __name__ == '__main__' :
	# if running the app on IBM Cloud
	app.run(host='0.0.0.0', port=port, debug=True)
	# if running locally
	# app.run()


