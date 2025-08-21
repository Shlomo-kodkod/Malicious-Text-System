docker build -t kodkod1docker/malicious-text-system:v13 .
docker push kodkod1docker/malicious-text-system:v13


cd infra

oc apply -f secrets.yaml
oc apply -f deployment.yaml
oc apply -f service.yaml

oc expose service  malicious-text-system --port=8085 --target-port=8085 --name=malicious-text-system

oc annotate  route malicious-text-system haproxy.router.openshift.io/timeout=2m --overwrite