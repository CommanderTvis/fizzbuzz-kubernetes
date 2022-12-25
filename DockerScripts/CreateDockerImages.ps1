docker login

docker build --tag gor8808/buzz-docker:latest ./../services/buzz
docker push gor8808/buzz-docker:latest

docker build --tag gor8808/fizz-docker:latest ./../services/fizz
docker push gor8808/fuzz-docker:latest

docker build --tag gor8808/concat-docker:latest ./../services/concat
docker push gor8808/concat-docker:latest

docker build --tag gor8808/main-docker:latest ./../services/main
docker push gor8808/main-docker:latest