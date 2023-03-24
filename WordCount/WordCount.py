from pyspark import SparkContext
sc = SparkContext(appName="Log Analytics")
from operator import add
lines = sc.textFile("README.md")
counts = lines.flatMap(lambda x: x.split(' ')) \
              .map(lambda x: (x, 1)) \
              .reduceByKey(add)
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
