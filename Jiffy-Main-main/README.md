# Word Embeddings for Financial Domain
  This repository contains the code for the creation and implementation of word embeddings for the financial domain.
  The dataset was created by scraping articles from Investopedia and the word embeddings model was created using         **Word2Vec**.
  All models generated are in the `models` directory and all the csv files needed are in the `csv` directory.
  
  
## Installation
To install all the necessary packages, navigate to the `Jiffy-Main` folder and run the following command in the terminal <br />
`pip install -r requirements.txt`

## Webscraping
The webscraping part was implemented using the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library in Python which is useful for pulling and parsing content out of HTML and XML files. The website used to scrape the data from is [Investopedia](https://www.investopedia.com/).
The file `scrap_term_definitions.py` has the code for scraping the paragraph content of all the financial term definitions available in Investopedia and `scrap_articles.py` is for scraping all the articles related to finance.


## Data Preprocessing
The `dataset` folder consists of all the scraped content which is the dataset on which the model is trained upon. It contains the topic related articles and the alphabetical term definitions scarped from Investopedia.

### Cleaning
The cleaning procedure is done in `clean.py`. It uses the [NLTK](https://www.nltk.org/) library for Python which has a lot of useful tools for Natural Language Processing tasks. The steps involved in cleaning are:
  * Remove punctuation using the `string` module
  * Remove stopwords using the NLTK library
  * Lemmatization using POS tag of all the words using WordNetLemmatizer from NLTK library

### Preprocessing
The cleaned corpus is then preprocessed in the `preprocess.py` file where the corpus is stored in a list of lists format to be given as input to the Word2Vec model.


## Word2Vec
The Word2Vec model was implemented using the [Gensim](https://radimrehurek.com/gensim/) module for NLP. The Word2Vec algorithm uses a neural network model to learn word associations from a large corpus of text. Words are distributed in a vector space depending on the context in which it is used.  
The file `word2vec.py` contains the implementation of the word2vec model. In the model used here a window size of 5, hidden layer dimension of 300 was used on a CBOW model. In order to train your own custom corpus and build a model, place all your text files in a single or multiple folder. Place this folder inside the dataset directory and run the `word2vec.py` file. Change the name of the model and the resultant trained model will be stored in the models directory.
 `predict.py` has code for the desired predictions we want. This can be for obtaining the similarity measure or the *n* most similar words. For example using our model `word2vec.txt` when the word vector of *company* was subtraced from the word vector of *business* the resultant vector was of the word *enterpreunership*.

## GloVe
The GloVe algorithm was used to train the custom corpus to create the model `glove.txt`. This was trained by creating a corpus that was fed into the GloVe model implemented by Stanford Univeristy which can be found [here](https://github.com/stanfordnlp/GloVe). In order to create the corpus, simply run the `corpus.py` file.

All the models used can be found in the `/models` directory.
## Comparison
The Word2Vec and GloVe model results were compared by checking the similarity measure between certain input words. 
![comparison](https://github.com/SV-1509/Jiffy-Main/blob/main/img/w2v%20vs%20glove.png?raw=true)

As observed, the GloVe model produced slightly better accuracy than the Word2Vec model. However for building the helper module both these models were taken into account.

## FinHelper Module
The end product involves the user searching a word and the model returning the function matches for that particlar word. Here, the combination of both Word2Vec and GloVe was used for providing results.
The file `finhelper.py` when run, takes an input word from the user and returns the function/functions that is most similar in context to the input word. The following steps are involved in the process.

#### FinancePy Functions
All the FinancePy functions, its syntax and corresponding function description is obtained from [FinancePy documantation](https://github.com/domokane/FinancePy). This is contained in the `/csv/financepy.csv`. Each row corresponds to a single function, its syntax and its function description. This file was cleaned and null values removed for better results.

#### FinHelper Module
This is the helper module that interacts with the user to provide a function match for any input word. It has the following steps
  * Creating kedictionary ywords to be inputted into the model. The last term in the function name was taken, and split appropriately for obtaining meaningnful words to be given as input to the model.
  * Creating the helper dictionary. The keywords generated are+v2 fed into both the Word2Vec and GloVe models and top 5 similar words are obtained.  Coresponding words are matched to functions and are stored in a dictionary. Run the `make_helper_dictionary.py` file to create this dictionary mapping. `helper_dictionary.csv` and `helper_dictionary_2.csv` are the dictionaries corresponding to Word2Vec and GloVe models. The results are combined by running the file `combine_csv.py` to give the final dictionary `helper_dictionary_3.csv`.
  * `description.csv` contains a similar word to fucntion mapping, where the semantically important words in the fucntion description are used as the mapping criterion. The helper modules uses this dictionary along with the `helper_dictionary_3.csv` to give more accurate search results
  * `finhelper.py` references the input word from the user to find a match in the helper dictionary and/or the description dictionary and return possible matches. The user can interactively choose which function he/she needs and receive its syntax and function description.
  * An interactive environment using tkinter is provided where the user can call the finhelper module and enter a word. FinHelper returns results, and the user can copy the syntax to his/her clipboard for easy use.




