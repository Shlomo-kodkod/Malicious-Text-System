docker build -t kodkod1docker/malicious-text-system:v12 .
docker push kodkod1docker/malicious-text-system:v12


cd infra

oc apply -f secrets.yaml
oc apply -f deployment.yaml
oc apply -f service.yaml

oc expose service  malicious-text-system --port=8085 --target-port=8085 --name=malicious-text-system