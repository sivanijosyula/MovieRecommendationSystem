import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from collections import Counter

st.title("Movie recommendations system")

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.rename(columns={"id": "movie_id"})
df1 = pd.merge(movies, credits, on="movie_id")
data = df1[['movie_id', 'title_x', 'original_language', 'overview', 'popularity', 'vote_count', 'vote_average', 'budget', 'revenue', 'genres', 'cast', 'crew','release_date','runtime','keywords']]
data.set_index('movie_id')
data.dropna()

index = pd.Series(data.index, index=data['title_x'])

data['overview'] = data['overview'].astype(str)
data['genres'] = data['genres'].tolist()
data['genres'] = data['genres'].astype(str)
data['cast'] = data['cast'].astype(str)
data['crew'] = data['crew'].astype(str)
data['keywords'] = data['keywords'].astype(str)

termfreq_desc = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
freq_matrix_desc = termfreq_desc.fit_transform(data['overview'])
model_desc = linear_kernel(freq_matrix_desc, freq_matrix_desc)

def desc_recommendations(title):
    movind = index[title]
    rrec = list(enumerate(model_desc[movind]))
    srec = sorted(rrec, key=lambda x: x[1], reverse=True)
    srec = srec[1:31]
    movind = [i[0] for i in srec]
    return data['title_x'].iloc[movind]

termfreq_gen = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
freq_matrix_gen = termfreq_gen.fit_transform(data['genres'])
model_gen = linear_kernel(freq_matrix_gen, freq_matrix_gen)

def gen_recommendations(title):
    movind = index[title]
    rrec = list(enumerate(model_gen[movind]))
    srec = sorted(rrec, key=lambda x: x[1], reverse=True)
    srec = srec[1:31]
    movind = [i[0] for i in srec]
    return data['title_x'].iloc[movind]

termfreq_cast = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
freq_matrix_cast = termfreq_cast.fit_transform(data['cast'])
model_cast = linear_kernel(freq_matrix_cast, freq_matrix_cast)

def cast_recommendations(title):
    movind = index[title]
    rrec = list(enumerate(model_cast[movind]))
    srec = sorted(rrec, key=lambda x: x[1], reverse=True)
    srec = srec[1:31]
    movind = [i[0] for i in srec]
    return data['title_x'].iloc[movind]

termfreq_crew = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
freq_matrix_crew = termfreq_crew.fit_transform(data['crew'])
model_crew = linear_kernel(freq_matrix_crew, freq_matrix_crew)

def crew_recommendations(title):
    movind = index[title]
    rrec = list(enumerate(model_crew[movind]))
    srec = sorted(rrec, key=lambda x: x[1], reverse=True)
    srec = srec[1:31]
    movind = [i[0] for i in srec]
    return data['title_x'].iloc[movind]

termfreq_kwords = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')
freq_matrix_kwords = termfreq_kwords.fit_transform(data['keywords'])
model_kwords = linear_kernel(freq_matrix_kwords, freq_matrix_kwords)

def kwords_recommendations(title):
    movind = index[title]
    rrec = list(enumerate(model_kwords[movind]))
    srec = sorted(rrec, key=lambda x: x[1], reverse=True)
    srec = srec[1:31]
    movind = [i[0] for i in srec]
    return data['title_x'].iloc[movind]

def recommendation(title, category):
    desc_output = desc_recommendations(title)
    gen_output = gen_recommendations(title)
    cast_output = cast_recommendations(title)
    crew_output = crew_recommendations(title)
    kwords_output = kwords_recommendations(title)
    output = ""
    if category == "Blurb":
        output = desc_output.tolist()
    elif category == "Genre":
        output = gen_output.tolist()
    elif category == "Cast":
        output = cast_output.tolist()
    elif category == "Crew":
        output = crew_output.tolist()
    elif category == "Key words":
        output = kwords_output.tolist()
    else:
        out_list = [desc_output, gen_output, cast_output, crew_output, kwords_output]
        output = pd.concat(out_list)
        # total_output = pd.Series(list(set(desc_output)|set(gen_output)|set(cast_output)|set(crew_output)|set(kwords_output)))
        output = output.tolist()
    # res = sorted(output, key = output.count, reverse = True)
    res = [item for items, c in Counter(output).most_common() for item in [items] * c]
    # finalRes = list(set(res))
    finalRes = list(dict.fromkeys(res))
    finalRes = finalRes[0:35]
    return pd.DataFrame (finalRes, columns = ['Movie'])

title = st.selectbox("Select a movie",data['title_x'])
# st.write("Recommendations based on")
# ifGen = st.checkbox("General recommendations")
category = "General recommendations"
category = st.radio(
        "Recommendation category",
        ["General recommendations", "Blurb", "Genre", "Cast", "Crew", "Key words"],
        key="visibility",
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        horizontal=True,
    )

recs = recommendation(title, category)
# st.write("General recommendations")
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(recs)
