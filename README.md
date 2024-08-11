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

ASIA-NORTHEAST3
https://dialogflow-fulfillment-jr6kniykka-du.a.run.app

타사제품 비교

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "product.comparison", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "최신 아이폰이 제 갤럭시 S24보다 얼마나 좋은지 비교해줘요.", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "product.comparison", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "SM-S711NZOWKOO와 SM-S921NZAFKOO는 어떻게 다른가요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "product.comparison", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "SM-S911NLGEKOO와 SM-S921NZAFKOO는 어떻게 다른가요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "product.comparison", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "폰 바꿀때가 됐어. S24 시리즈 중 하나를 사고싶은데 제품끼리 비교좀 해줘", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

스펙 설명

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "galaxy.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Product Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "S24, S24+, S24U의 카메라 스펙은 각각 어떻게 되나요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "galaxy.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Product Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "SM-S711NZOWKOO에 대해 알려줘", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "galaxy.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Product Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "SM-S921NZAFKOO에 대해 알려줘", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "galaxy.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Product Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "갤럭시 S24 울트라에 탑재된 카메라 사양 알려주세요.", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "solution.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "SM-S921NZAFKOO에 대해 알려줘", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

출시일

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/solution/get_release_date \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "release_date.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "갤럭시 S23의 출시일은 언제인가요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```

타사제품 회피

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/solution/get_release_date \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "release_date.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "갤럭시 S23과 아이폰15 프로의 출시일은 언제인가요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```


US-CENTRAL1
https://dialogflow-fulfillment-jr6kniykka-uc.a.run.app

```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-uc.a.run.app/product/comparison \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "product.comparison", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "최신 아이폰이 제 갤럭시 S24보다 얼마나 좋은지 비교해줘요.", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```
