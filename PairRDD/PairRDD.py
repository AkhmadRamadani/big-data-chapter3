from pyspark import SparkContext
sc = SparkContext(appName="Log Analytics")

mylist = ["my", "pair", "rdd"]
myRDD = sc.parallelize(mylist)
myPairRDD = myRDD.map(lambda s: (s, len(s)))
myPairRDD.collect()

myPairRDD.keys().collect()

myPairRDD.values().collect()
