**Movie Recommendations System**

***Collaborative-based recommendation system***: A family of algorithms known as collaborative filtering offers numerous methods for locating comparable users or things as well as numerous methods for determining ratings based on the ratings of comparable users. Depending on their decisions, you end up choosing a collaborative filtering strategy.

***Content-based recommendation system***: Recommending movies based on the content, title, genre, director, movie description, and a few other features. This type of recommendation system works on the premise that if a person enjoyed one movie, they could also enjoy one that is similar to it. This project implements a Content-based recommendation system.

***Cosine similarity***: It is a metric used to measure the similarity between two non-zero vectors in a multi-dimensional space. The text in the data is represented as vectors, where each dimension corresponds to the presence or frequency of a particular term in the text. Cosine similarity is used to measure the similarity between two pieces of text based on their term frequencies. 

The cosine similarity between two vectors, A and B, is calculated as follows:

  Cosine Similarity(A,B)= $\frac{A.B}{∥A∥⋅∥B∥}$

where,

$A⋅B$ represents the dot product of vectors $A$ and $B$.

$∥A∥$ and $∥B∥$ are the magnitudes of the vectors $A$ and $B$.


**Steps for execution:**

* Download the two CSV files(‘tmdb_5000_credits.csv’ and ‘tmdb_5000_movies.csv’) provided in the dataset zip file in the same folder as that of recsystem.py

* The path in the Python code file for these CSV files is mentioned as Downloads/file_name. Update it if needed.

* Dataset link: 
  
    https://www.kaggle.com/datasets/abdelrhamanfakhry/movies-data-for-ml-dl-recommendation-system

* Have Python installed in the system. We recommend using Jupyter Lab(Anaconda).

* Install streamlit using the command - ```pip install streamlit```
  
    Documentation for reference: https://docs.streamlit.io/

* Run the command -

  ```streamlit run recsystem.py```
  
* If the terminal is not opened in the same path as the Python file, please include the full path of the file in the command.

    Example - streamlit run Downloads/recsystem.py
  

**Preview of the application home screen**
<img width="1440" alt="image" src="https://github.com/sivanijosyula/MovieRecommendationSystem/assets/119761687/a36feba7-18cd-412c-9eb0-e299981084a7">


