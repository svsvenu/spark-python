./sbin/start-master.sh

./bin/spark-class org.apache.spark.deploy.worker.Worker spark://Venus-MBP-2.attlocal.net:7077 -c 1 -m 512M

./bin/spark-class org.apache.spark.deploy.worker.Worker spark://192.168.1.103:7077 -c 1 -m 512M

bin/run-example SparkPi
