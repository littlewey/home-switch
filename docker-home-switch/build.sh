
rm -fr ./docker-resource/
mkdir docker-resource
cp ../*.py docker-resource
docker build -t home-switch:latest .
