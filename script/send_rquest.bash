#!/bin/bash
#ssh
ssh -i KP_infrastructure.pem ec2-user@10.152.12.219  -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no

cd /opt/reuters/data/elasticsearch/unit_test/elasticsearch-6.2.1/

curl -s localhost:9220

# scp
scp -i IDENDIFILE SOURCE user@host:/path

# Create an ARCI index
curl -XPUT -H "Content-Type: application/json" http://localhost:9230/arci-test --data @arci.mapping.json

# Get ARCI index settings
curl -XGET http://localhost:9230/arci-test/_settings?pretty

# Send a word to an analyzer in ARCI
curl -XPOST -H "Content-Type: application/json" http://localhost:9230/arci-test/_analyze?pretty -d '{
    "analyzer":"rbl_ara",
    "text": "علما"
}'
