DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "donald_trump_tweets"
URL_WITH_DATA_PREFIX = 'http://trumptwitterarchive.com/data/realdonaldtrump/'
URL_WITH_DATA_SUFFIX = '.json'
TWEETS_YEARS = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']
COLLECTION_NAMES = ['tweets_' + i for i in TWEETS_YEARS]
CORRECT_INSERTION_TEXT = ' OK'
ALREADY_INSERTED_TEXT = ' Already added'
REQUEST_GET_METHOD = 'GET'
RETURNED_DATA_TO_SERVER_SEPARATOR = ' '
RUSSIA_WORD_FOR_SEARCH_IN_TWEETS = 'Russia'
URL_FOR_RESULTS_BY_YEAR_SUFFIX = '/by-year'
URL_FOR_RESULTS_BY_DAY_SUFFIX = '/by-day'
URL_FOR_RESULTS_FOR_RUSSIA_IN_TWEETS_SUFFIX = '/russia'
