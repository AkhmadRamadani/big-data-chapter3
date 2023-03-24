from pyspark import SparkContext
sc = SparkContext(appName="Log Analytics")
myaccum = sc.accumulator(0)
myrdd = sc.parallelize(range(1,100))
myrdd.foreach(lambda value: myaccum.add(value))
print(myaccum.value)
