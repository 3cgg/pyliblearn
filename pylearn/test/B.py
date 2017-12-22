
'''
测试CRAB系统
http://blog.sina.com.cn/s/blog_5d4214c70101nmkf.html

'''

from scikits.crab import datasets
movies=datasets.load_sample_movies()

songs=datasets.load_sample_songs()

print (movies.data)
print(songs)
print(songs.data)

from scikits.crab.models import MatrixPreferenceDataModel
#build the model
model=MatrixPreferenceDataModel(movies.data)

#引入矩阵包和相似度包，计算相似度
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
#build the similarity
similarity=UserSimilarity(model,pearson_correlation)

#引入算法包，这里引入的是基于用户的协同过滤算法，当然这个算法要自己重写
from scikits.crab.recommenders.knn import UserBasedRecommender
#build the user based recommender
recommender=UserBasedRecommender(model,similarity,with_preference=True)

#这里是为用户5推荐商品，从结构可以看出系统为用户5推荐了3种相似度最高的物品，
#recommend items for the user 5
print(recommender.recommend(5))






