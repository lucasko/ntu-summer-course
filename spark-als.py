from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext


class sparkALS():
 sc = None
 sqlCtx = None

 def __init__(self): 
  conf = SparkConf().setAppName("ntu-speech").setMaster("local")
  self.sc = SparkContext(conf=conf)
  self.sqlCtx = SQLContext(self.sc)
 
 def CF(self , traingLIST , testingLIST ):
  df = self.sqlCtx.createDataFrame(traingLIST, ["user", "item", "rating"])
  
  als = ALS(rank=10, maxIter=5, seed=0)
  model = als.fit(df)  # Training
  
  test = self.sqlCtx.createDataFrame( testingLIST , ["user", "item"])
  predictions = sorted(model.transform(test).collect(), key=lambda r: r[0])

  resultLIST = list()
  for p in predictions:
  	resultLIST.append(  [ p[0], p[1], p[2]  ] )
  return resultLIST



if __name__ == '__main__':

 trainingLIST =[ [0, 0, 4.0],   [0, 1, 2.0],   [1, 1, 3.0],   [1, 2, 4.0],   [2, 1, 1.0],   [2, 2, 5.0] ]
 testLIST = [ [0, 2],  [1, 0],  [2, 0] ]
 spark = sparkALS()
 resultLIST = spark.CF( trainingLIST , testLIST )

 for userId , itemId , prediction in resultLIST :
  print "userId=%s , itemId=%s ,prediction=%s " % ( userId , itemId , prediction )


