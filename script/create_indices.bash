#!/bin/bash
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/arci --data @arci.mapping
echo "Create arci"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/diidw --data @diidw.mapping
echo "Create diidw"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/biosis --data @biosis.mapping
echo "Create biosis"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/rsci --data @rsci.mapping
echo "Create rsci"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/bci --data @bci.mapping
echo "Create bci"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/medline --data @medline.mapping
echo "Create medline"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/cscd --data @cscd.mapping
echo "Create cscd"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/kjd --data @kjd.mapping
echo "Create kjd"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/drci --data @drci.mapping
echo "Create drci"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/inspec --data @inspec.mapping
echo "Create inspec"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/wos --data @wos.mapping
echo "Create wos"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/bioabs --data @bioabs.mapping
echo "Create bioabs"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/ccc --data @ccc.mapping
echo "Create ccc"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/superunif --data @superunif.mapping
echo "Create superunif"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/zoorec --data @zoorec.mapping
echo "Create zoorec"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/fsta --data @fsta.mapping
echo "Create fsta"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/cabi --data @cabi.mapping
echo "Create cabi"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/scielo --data @scielo.mapping
echo "Create scielo"
curl -XPUT -H "Content-Type: application/json" http://localhost:9220/gci --data @gci.mapping
echo "Create gci"
