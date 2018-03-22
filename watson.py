import json, os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3 as ToneAnalyzer
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator
from dotenv import load_dotenv

# load service credentials from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), "crd.env"))

ta_username = os.environ.get("TA_USERNAME")
ta_password = os.environ.get("TA_PASSWORD")

# initialize watson service
tone_analyzer = ToneAnalyzer(username=ta_username, password=ta_password, version='2016-05-19')

tr_username = os.environ.get("TR_USERNAME")
tr_password = os.environ.get("TR_PASSWORD")

language_translator = LanguageTranslator(username=tr_username, password=tr_password)

def get_language_translator_results(data):
	''' translates results i.e. tweets from Arabic to English. 
	Note if tweets are already in English, this function takes no effect '''
	return language_translator.translate(text=data,source='ar',target='en')

def get_tone_analyser_results(data):
	''' analyses data (json obj) using watson tone analyser '''

	# pass the data i.e. tweets to watson service
	results = tone_analyzer.tone(text=data)

	# return an object from a string representing a json object 
	results = json.dumps(results, indent=2)

	# return string representing a json object from an object
	results = json.loads(str(results))

	return results

def display_emotion_tone(data):
	''' takes tone analyser results (json obj) and  '''
	# results will be stored here
	answers = []

	# loop through watson's output
	for index, catagory in enumerate(data['document_tone']['tone_categories']):

		# we are only interested in these tones
		target = ['Joy', 'Anger', 'Confident', 'Agreeableness', 'Emotional Range', 'Sadness']

		for tone in catagory['tones']:
			if tone['tone_name'] in target :

				# store type as a KEY
				_type = str(tone['tone_name']) 

				# here we would like to call the tone 'Emotional' rather than 'Emotional Range'
				if _type == "Emotional Range":
					_type = "Emotional"
					
				# store score as a VALUE
				_score = (str(round(tone['score'] * 100,1)) + "%")
				temp = {str(_type) : str(_score)}
				answers.append(temp)
	
	return answers
