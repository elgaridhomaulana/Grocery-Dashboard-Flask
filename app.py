from flask import Flask, render_template, request
from data import df_content_based, df_top50, cos_sim_title_desc, df_review, review, meta
import random
import pandas as pd
from plots import overall_counts, vote_helpful, good_word_reviews, bad_word_reviews, neutral_word_reviews
from plots import series_month_line, series_month_bar, series_day_line, series_day_bar
from plots import good_word_sum, bad_word_sum, neutral_word_sum
from predictions import predictions


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form
        product = product.to_dict()
        idx_product_search = df_content_based[df_content_based['title'].str.contains(product['search_product'])].index
        jumlah_produk = len(idx_product_search)
        return render_template('search_product.html', df_content_based=df_content_based, idx=random.sample(list(idx_product_search), int(0.5*jumlah_produk)), nama_produk=product['search_product'], jumlah_produk=jumlah_produk)

    return render_template('index.html', random_five=random.sample(list(df_top50.index), 5), data_top50=df_top50, df_content_based=df_content_based, 
    random_twenty=random.sample(range(1, len(df_content_based)), 25))

@app.route('/detail')
def detail():
    indeks =request.args.get('index')
    indeks=int(indeks)
    round_rating= round(df_content_based['overall'].loc[indeks], 1)
    review_idx = df_review[df_review['title'] == df_content_based['title'].loc[indeks]].index
    random_review_idx = random.sample(list(review_idx), 3)
    index_to_search = df_content_based[df_content_based['title'] == df_content_based['title'].loc[indeks]].index[0]    
    similar_index = pd.Series(cos_sim_title_desc[index_to_search]).sort_values(ascending=False).head(7).index
    similar_df = df_content_based.loc[similar_index]

    return render_template('detail.html', data=df_content_based, index=indeks, similar_df=similar_df, index_similar=similar_df.index[1:],
    round_rating=round_rating, review_idx=random_review_idx, df_review=df_review)

@app.route('/data')
def explore_data():
    return render_template('data.html', review=review, meta=meta)
    

@app.route('/plots')
def plots():
    data = overall_counts()
    data2 = vote_helpful()
    good_review = good_word_reviews()
    bad_review = bad_word_reviews()
    neutral_review = neutral_word_reviews()
    series_month_lines = series_month_line()
    series_month_bars = series_month_bar()
    series_day_lines = series_day_line()
    series_day_bars = series_day_bar()
    good_sum = good_word_sum()
    bad_sum = bad_word_sum()
    neutral_sum = neutral_word_sum()

    return render_template('plots.html', data=data, data2=data2,
    good_review=good_review, bad_review=bad_review, neutral_review=neutral_review,
    series_month_lines=series_month_lines, series_month_bars=series_month_bars,
    series_day_lines=series_day_lines, series_day_bars=series_day_bars,
    good_sum=good_sum, bad_sum=bad_sum, neutral_sum=neutral_sum)

@app.route('/predict_review', methods=['GET', 'POST'])
def predict_review():
    if request.method == 'POST':
        text = request.form
        text = text.to_dict()
        output, proba = predictions(text['text-review'])
        return render_template('result.html', review_text=text['text-review'], result_predict=output[0], probability_good=round(proba[0][1], 3), probability_bad=round(proba[0][0],3))

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

