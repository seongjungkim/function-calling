#

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

```bash
git remote add tpcg https://source.developers.google.com/p/tpcg-datacollector/r/function-calling
git remote add git-func https://github.com/seongjungkim/function-calling
```

```bash
git remote set-url tpcg https://source.developers.google.com/p/tpcg-datacollector/r/function-calling
```

```bash
git remote -v                                        
git-func https://github.com/seongjungkim/function-calling (fetch)
git-func https://github.com/seongjungkim/function-calling (push)
tpcg    https://source.developers.google.com/p/tpcg-datacollector/r/function-calling (fetch)
tpcg    https://source.developers.google.com/p/tpcg-datacollector/r/function-calling (push)
```

```bash
git branch -v
  main   a7b2a80 Initialize
* master c66ac0c Suggestions 관련 수정
```

```bash
git status
git add routers/chatbot.py README.md routers/dummy.py
git commit -m "dummy.py 파일 추가"
git push -u tpcg master
```

### For function calling at tpcg-datacollector project

```bash
PROJECT_ID=tpcg-datacollector
REGION=asia-northeast3
APP=function-calling
TAG=gcr.io/$PROJECT_ID/$APP
```

### For function calling at sam-poc project

```bash
PROJECT_ID=samsung-poc-425503
REGION=asia-northeast3
APP=function-calling
TAG=gcr.io/$PROJECT_ID/$APP
```

```bash
gcloud builds submit --project=$PROJECT_ID --tag $TAG
```

```bash
gcloud run deploy $APP \
--project $PROJECT_ID \
--image $TAG \
--platform managed \
--region $REGION \
--allow-unauthenticated
```

### For Dialogflow fulfillment at sam-poc project (with VPC)

```bash
PROJECT_ID=samsung-poc-425503
REGION=asia-northeast3
APP=dialogflow-fulfillment
TAG=gcr.io/$PROJECT_ID/$APP
```

```bash
gcloud run deploy $APP \
--project $PROJECT_ID \
--image $TAG \
--platform managed \
--region $REGION \
--network default \
--subnet default \
--allow-unauthenticated
```

## Test

```bash
curl -X POST https://function-calling-phdovlv6aa-du.a.run.app/get-weather \
-d '{"location": "서울"}'
```