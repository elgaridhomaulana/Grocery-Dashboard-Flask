import plotly
import plotly.graph_objects as go
import plotly.express as px
from data import review, good_word_review, neutral_word_review, bad_word_review, series_day, series_month
from data import good_word_summary, neutral_word_summary, bad_word_summary
import json
import pandas as pd

def overall_counts():
    group_overall = review['overall'].value_counts()
    fig = go.Figure([go.Bar(x=group_overall.index, y=group_overall.values, marker={'color':'green'})])
    fig.update_layout(title_text='Count Overall', yaxis_title='Count', xaxis_title='Overall')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def vote_helpful():

    fig = go.Figure(data=[go.Bar(x=['No Vote', '100 percent', '0 percent', '50 percent', '66.67 percent', '75 percent', '33.33 percent'], 
    y=[86403, 32333, 10608, 7107, 2906, 1757, 1317], marker={'color':'green'})])

    fig.update_layout(title_text='Vote Helpful Count', yaxis_title='Count', xaxis_title='Percentage Helpful')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def good_word_reviews():
    x = good_word_review.index
    y = good_word_review
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Good Rating Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def bad_word_reviews():
    x = bad_word_review.index
    y = bad_word_review
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Bad Rating Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def neutral_word_reviews():
    x = neutral_word_review.index
    y = neutral_word_review
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Neutral Rating Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def series_month_line():
    x = series_month.index
    y = series_month
    fig = go.Figure(data=go.Scatter(x=x, y=y))

    fig.update_layout(title_text='Count review by month', yaxis_title='Month', xaxis_title='Review')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def series_month_bar():
    x = series_month.index
    y = series_month
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Count review by month', yaxis_title='Month', xaxis_title='Review')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def series_day_line():
    x = series_day.index
    y = series_day
    fig = go.Figure(data=go.Scatter(x=x, y=y))

    fig.update_layout(title_text='Count review by day', yaxis_title='Day', xaxis_title='Review')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def series_day_bar():
    x = series_day.index
    y = series_day
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Count review by day', yaxis_title='Day', xaxis_title='Review')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def good_word_sum():
    x = good_word_summary.index
    y = good_word_summary
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Good Summary Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def bad_word_sum():
    x = bad_word_summary.index
    y = bad_word_summary
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Bad Summary Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def neutral_word_sum():
    x = neutral_word_summary.index
    y = neutral_word_summary
    fig = go.Figure(data=[go.Bar(x=x, 
    y=y, marker={'color':'green'})])

    fig.update_layout(title_text='Neutral Summary Word Count', yaxis_title='Count', xaxis_title='Words')
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json