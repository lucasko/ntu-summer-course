### NTU SUMMER COUESE
```sh
ntu:ntu

ifconfig

windows : putty

ssh@192.168.30.131

wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.0/elasticsearch-2.3.0.tar.gz

./downlaod.sh

cd elasticsearch-2.3.0

./bin/plugin install mobz/elasticsearch-head

tar xvf elasticsearch-2.3.0.tar.gz

vim config/elasticsearch.yml 
  cluster.name: lucas
  node.name: node-1
  network.host: 0.0.0.0

./bin/elasticsearch

http://192.168.30.131:9200/_plugin/head/

```
