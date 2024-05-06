import csv
import pymongo
from tqdm import tqdm
from forex_python.converter import CurrencyRates
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer