1. Mysql create query 사용해 table 생성

2. DockerFile을 이용한 이미지 빌드
   docker build --tag localhost:5000/job-maker:v1

3. Private hub에 push
   docker push localhost:5000/job-maker:v1

4. Kubernetes replica create
   kubectl create -f job-worker-rc.yaml
