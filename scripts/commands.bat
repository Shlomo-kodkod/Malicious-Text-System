docker build -t kodkod1docker/malicious-text-system:v13 .
docker push kodkod1docker/malicious-text-system:v13


cd infra

oc apply -f secrets.yaml
oc apply -f deployment.yaml
oc apply -f service.yaml
oc apply -f route.yaml

