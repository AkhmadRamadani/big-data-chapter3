from pyspark import SparkContext
sc = SparkContext(appName="Log Analytics")
broadcastVar = sc.broadcast(list(range(1, 100)))
broadcastVar.value 	