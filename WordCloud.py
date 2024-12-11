from wordcloud import WordCloud

import matplotlib.pyplot as plt

# Sample text
text = "Python is a great programming language. Python is popular for data science. Python is versatile."

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()