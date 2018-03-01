import numpy as np
import lda
import lda.datasets
#我们共有395篇文章，4258个单词
# document-term matrix
X = lda.datasets.load_reuters()
print("type(X): {}".format(type(X)))
print("shape: {}\n".format(X.shape))
print(X[:5, :5])
# the vocab
vocab = lda.datasets.load_reuters_vocab()
print("type(vocab): {}".format(type(vocab)))
print("len(vocab): {}\n".format(len(vocab)))
print(vocab[:5])
# titles for each story
titles = lda.datasets.load_reuters_titles()
print("type(titles): {}".format(type(titles)))
print("len(titles): {}\n".format(len(titles)))
print(titles[:5])
#训练模型
model = lda.LDA(n_topics=10, n_iter=100, random_state=1)   #模型参数解释：n_topics=10主题模型10个，n_iter迭代100次
model.fit(X)          # model.fit_transform(X) is also available
#主题单词的分布
topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
print("shape: {}".format(topic_word.shape))
print(vocab[:3])   #取前3个单词
print(topic_word[:,:3])
for n in range(5):
    sum_pr = sum(topic_word[n, :])
    print("topic: {} sum: {}".format(n, sum_pr))   #相当于传参的结构.format

#计算每个主题的前5个单词，我们一共有20个主题
n = 5
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

#前面10篇最有可能的主题
doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))
for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print("doc: {} topic: {}".format(n, topic_most_pr))

#画出每个主题中单词的分布
import matplotlib.pyplot as plt
f, ax = plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 1, 2, 3, 4]):
    ax[i].stem(topic_word[k, :], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-50, 4350)
    ax[i].set_ylim(0, 0.08)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))
ax[4].set_xlabel("word")
plt.tight_layout()
plt.show()

#对每个词语的类别判定
'''
import matplotlib.pyplot as plt

f, ax = plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([1, 3, 4, 8, 9]):
    ax[i].stem(doc_topic[k, :], linefmt='r-',
               markerfmt='ro', basefmt='w-')
    ax[i].set_xlim(-1, 21)
    ax[i].set_ylim(0, 1)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("Document {}".format(k))

ax[4].set_xlabel("Topic")

plt.tight_layout()
plt.show()
'''