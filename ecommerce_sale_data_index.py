# -*- coding: utf-8 -*-
"""Ecommerce Sale Data Index

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d2iQuX1rG4rDuN_HjwOCnEStQRLaq-0V
"""

import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

import missingno as msno

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("/content/ecommerce_sales_analysis.csv")
df.head()

df.tail()

df.shape

df.info()

df.describe().T

df.describe().T.plot(kind='bar')

df.isnull().sum()

sns.heatmap(df.isnull())

df.duplicated().sum()

numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(12, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

df.columns.to_list()

import plotly.express as px

columns = ['product_id',
'product_name',
'category',
'price',
'review_score',
'review_count',
'sales_month_1',
'sales_month_2',
'sales_month_3',
'sales_month_4',
'sales_month_5',
'sales_month_6',
'sales_month_7',
'sales_month_8',
'sales_month_9',
'sales_month_10',
'sales_month_11',
'sales_month_12',]

for column in columns:

  if df[column].dtype == 'object' or df[column].dtype == 'category':
    column_counts = df[column].value_counts().reset_index()
    column_counts.columns = [column, 'count']

    fig = px.bar(
        column_counts,
        x=column,
        y='count',
        title=f'Distribution of {column}',
        labels={column: column, 'count': 'Count'},
        text='count'
    )

    fig.update_layout(
        xaxis_title=column,
        yaxis_title='Count',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_font=dict(size=18, family="Arial"),

        xaxis={'categoryorder':'total descending'}
    )

    fig.show()

  elif df[column].dtype == 'int64' or df[column].dtype == 'float64':

    fig = px.histogram(
        df,
        x=column,
        title=f'Distribution of {column}',
        labels={column: column, 'count': 'Count'},

    )

    fig.update_layout(
        xaxis_title=column,
        yaxis_title='Count',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_font=dict(size=18, family="Arial")
    )

    fig.show()

df

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import pandas as pd

stop_words_list = set(STOPWORDS)

counts = Counter(df["category"].dropna().apply(lambda x: str(x)))

wcc = WordCloud(
    background_color="black",
    width=1600, height=800,
    max_words=2000,
    stopwords=stop_words_list
)
wcc.generate_from_frequencies(counts)

plt.figure(figsize=(10, 5), facecolor='k')
plt.imshow(wcc, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()