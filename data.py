import pickle

df_content_based = pickle.load(open('content_based_title_desc.sav', 'rb'))

df_top50 = df_content_based.sort_values(by=['score'], ascending=False).head(50)

cos_sim_title_desc = pickle.load(open('cos_sim_des_title.sav', 'rb'))

df_review = pickle.load(open('df_review.sav', 'rb'))

review = pickle.load(open('review.sav', 'rb'))

meta = pickle.load(open('meta.sav', 'rb'))

good_word_review = pickle.load(open('good_word_review.sav', 'rb'))
neutral_word_review = pickle.load(open('neutral_word_review.sav', 'rb'))
bad_word_review = pickle.load(open('bad_word_review.sav', 'rb'))

series_month = pickle.load(open('series_month.sav', 'rb'))
series_day = pickle.load(open('series_day.sav', 'rb'))

good_word_summary = pickle.load(open('good_word_sum.sav', 'rb'))
neutral_word_summary = pickle.load(open('neutral_word_sum.sav', 'rb'))
bad_word_summary = pickle.load(open('bad_word_sum.sav', 'rb'))

pipe = pickle.load(open('pipe.sav', 'rb'))