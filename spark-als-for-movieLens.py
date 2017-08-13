from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkContext, SparkConf
from datetime import datetime

conf = SparkConf().setAppName("sparkApp").setMaster("local")
sc = SparkContext(conf=conf)

starttime = datetime.now()


print "start: ", starttime.strftime('%Y-%m-%d %H:%M:%S') 

# Load and parse the data
data = sc.textFile("/home/spark/Desktop/ml-1m/ratings.dat")
ratings = data.map(lambda l: l.split('::'))\
    .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

# Build the recommendation model using Alternating Least Squares
rank = 10
numIterations = 10
model = ALS.train(ratings, rank, numIterations)

# Evaluate the model on training data
testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))


#for p in predictions.collect() :
# print p

endtime = datetime.now()
print "amount of rating: ", ratings.count()
print "start: ", starttime.strftime('%Y-%m-%d %H:%M:%S')
print "end  : ", endtime.strftime('%Y-%m-%d %H:%M:%S')
print "Runtime: ",(endtime - starttime)


# Save and load model
#model.save(sc, "target/tmp/myCollaborativeFilter")
#sameModel = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")
