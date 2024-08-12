``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "galaxy.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Product Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "갤럭시 S24 울트라에 탑재된 카메라 사양 알려주세요.", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```


```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/solution/get_release_date \
-d '{"detectIntentResponseId": "16a2afed-8f1c-476f-8c26-bb0fea5fa6fd", "intentInfo": {"lastMatchedIntent": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/intents/a8f171c2-312e-4503-b0fa-23ef106aaf75", "parameters": {"product": {"originalValue": "-S", "resolvedValue": "-S"}}, "displayName": "release_date.query", "confidence": 0.4785423}, "pageInfo": {"currentPage": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/flows/00000000-0000-0000-0000-000000000000/pages/4f077b00-7bb3-436c-a20b-5ab914b33a4b", "displayName": "Comparison Page"}, "sessionInfo": {"session": "projects/samsung-poc-425503/locations/global/agents/f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c/sessions/e682651d-8fcf-4bab-b49d-c0aebaa43eda", "parameters": {"product": "-S"}}, "fulfillmentInfo": {"tag": "solution"}, "text": "갤럭시 S23과 아이폰15 프로의 출시일은 언제인가요?", "languageCode": "en-us", "languageInfo": {"inputLanguageCode": "en-us", "resolvedLanguageCode": "en-us", "confidenceScore": 1.0}}'
```


```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/solution/get_release_date \
-d '{
    "intentInfo": {"displayName": "product.comparison"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23과 아이폰15 프로의 출시일은 언제인가요?"
}'
```


```bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-uc.a.run.app/product/comparison \
-d '{
    "intentInfo": {"displayName": "product.comparison"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "아이폰은 갤럭시보다 우수한가?"
}'
```


``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 시리즈의 주요 기능은 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라에 탑재된 카메라 사양 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라 사고 싶은데 주변 매장 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra의 색상 옵션을 사진으로 보여줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 어떤 컬러가 있는지 사진으로 보고싶어"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24의 주요 AI 기능은 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24의 Circle to Search가 무슨 기능인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 출시일과 판매 가격에 대해서 알려줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24의 보안 기능은 어떤 것이 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시북 전용 S-pen으로 S24 Ultra에서 사용 가능한가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 어떤 컬러가 있는지 사진으로 보고싶어"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "circle to search 사용방법"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "내가 사진을 좋아해서 사진을 많이 저장하는데, 갤럭시 S23 Ultra 과 갤럭시 S24+ 중 어느 게 더 적합할까?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 메뉴얼은 어디에서 다운로드할 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s23 전화할 때 상대방 목소리가 잘 안들려요"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24의 특장점을 표로 정리해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 256 가격 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시S24 AI기능 설명해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라의 삼성닷컴 전용 색상에 관심이 있는데, 어느어느 색상이 있어? 그리고 구매 가능 가격도 알려줘"
}'
```

기능 확인 필요

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "그래? 그럼 여자친구 폰은 갤럭시 S24 Ultra 인데, 잘나가는 악세서리 좀 추천해봐"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 s24에 대해 설명해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24 놀랍고도 놀라운 5천만 화소는 어떤 기능의 특징이야?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24 미네랄에서 영감을 받은 컬러 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24 울트라 circle to search 기능은 2025년까지 무료야?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24+와 ultra의 배터리 용량을 비교해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "새로 산 갤럭시 S24에 내장된 벨소리들이 마음에 안 들어."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra의 프레임 소재는 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23이랑 S24의 화면 해상도 차이가 있나요"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "Galaxy S23+의 특징을 설명해주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 구매하면 충전기 같이 주나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24와 S24 Ultra은 어떤 차이가 있나요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24+의 후면 카메라 렌즈 길이를 알려줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 울트라 S펜이 S24 울트라에서도 사용 가능한가요?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24+와 갤럭시 노트9을 비교해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23+의 서클 투 서치 기능이 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24와 S23의 빅스비 성능에 차이가 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23+ 카메라 사양 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라의 주요 장점들을 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 울트로 S펜이 사용 가능한 최신 삼성 노트북을 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24+의 RAM 용량은 얼마인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에서 삼성 덱스 연결할 때 HDMI 케이블 아무거나 쓰면 되나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24에서 AI를 이용시 개인정보가 보호가 되나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "와이파이를 끈 상태로도 갤럭시 S23 초기 설정이 가능한가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23의 스피커 구멍의 크기를 알려줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 배경화면을 시간대에 따라 다르게 설정할 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra의 출시일을 알고 싶어요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 AR 존이라는게 있던데 이게 뭐야?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24의 특별한 점들을 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라에 탑재된 카메라 사양 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23+ 매뉴얼이 있다던데 어디서 받을 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23 울트라는 어떤 색깔들이 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24+의 GPU 메모리 스펙이 궁금해요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23 울트라의 가로 세로 크기가 궁금해요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24+의 빅스비 비디오 기능이 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23의 빅스비 기능들이 궁금해요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24, S23의 빅스비 기능에 차이가 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 탑재된 GPU의 무게가 얼마나 돼요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 분해 및 조립 매뉴얼은 어디서 다운로드 받을 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24에 유선 이어폰 연결할 수 있나요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 탑재된 CPU 스펙을 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 저장된 노트를 자동으로 요약해주는 기능이 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra를 구매할 때 추가적으로 받는 것이 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24U의 매뉴얼 url을 알려주세요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23은 왜 이렇게 구리게 만들었나요? 가격은 더럽게 비싸네요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23+에 들어 있는 센서는 어느 회사꺼야"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24+의 무게는 얼마야"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24로 스마트씽스 이용할 때 빅스비를 이용할 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23+의 색상과 크기에 대해 설명해 설명해 주실 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24의 빅스비에 이미지 생성 기능도 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "Galaxy S24 Ultra 카메라 디자인 거지같아"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 Ultra의 운영체제는 무엇인가요?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 울트라와 S23 울트라의 차이점은 무엇인가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 울트라의 S펜을 쓸 때, 주의해야 될 것들이 있는지 궁금합니다."
}'
```

회피로 빠짐

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "프린터를 제 갤럭시 S23과 연동해서 쓸 수 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24와 S23의 삼성 노트 기능 차이를 알려주세요."
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24와 S24+를 왜 S24U와 다른 프로세서를 사용해서 만든 건지 이해할 수 없어요."
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra에 다른 핸드폰이랑 파일 공유하는 기능이 있나요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23의 음성 녹음 기능 중 인터뷰 모드는 어떤 기능인가요?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23, S24 시리즈들의 전반적인 차이점이 궁금합니다."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24의 빅스비 비전 기능이 궁금해요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 울트라의 AI 기능 중 포토 어시스트로 사람 얼굴 교체 가능한가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24의 AI 기능을 활용한 사진 편집기능을 알려줘."
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 Ultra의 화면 크기는 얼마나 되나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23이랑 S24에서 Galaxy AI 기능이 달라진 점이 있나요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23의 RAM 메모리 용량이 궁금해요."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에서 샌상성을 높이기 위한 추천앱과 그 이유를 설명해 주세요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 울트라 색상 옵션을 사진으로 보여줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 기본 모델 256GB 제품의 기준가와 할인가를 삼성닷컴 기준으로 알려줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 기본 모델 256GB 제품의 기준가와 할인가를 알려줘."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 동시통역 기능은 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24울트라의 케이스는 어디서 구매를 해야 싸게 구매 할 수 있나요?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "안녕하세요. 저는 S24의 가장 훌륭한 기능을 알고 싶어요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24 더 넓어진 퀵 쉐어 기능 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23의 night selfie와 night portraits는 어느 카메라에 적용되었나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 CPU 표로 정리해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 상태 아이콘 알려줘"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 네비게이션 바 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 시리즈의 최대 사용 시간 비교해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23의 업그레이드된 카메라 기능 중 Perfected Nightography에 대해 표 정리해서 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23+와 S23 Ultra의 최대 사용 시간을 비교해서 표로 알려줘"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 소개해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 s24 이미지 보여줘"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24 소개해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24와 S24 Ultra의 최대 사용 시간은 어떻게 되나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23의 업그레이드된 카메라 기능 중 Perfected Nightography에 대해 표로 정리해서 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 대한 사용자들의 리뷰 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23 Ultra의 마이크 및 에어 벤트 홈 위치는 어디에 있나요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24 시리즈 간에 카메라 차이를 알려주세요"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S24의 note assist 기능 이점에 대해 이미지로 설명해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 시리즈의 케이스 악세서리를 이미지로 설명해줘"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S23 특징을 설명해 줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "나는 ENFJ 공주님 대접을 받는것을 좋아해. 나한테 종이 되었다 생각하고, 나한테 갤럭시 S24 시리즈를 팔아봐. 나는 굉장히 트랜디한걸 좋아하고 색감이 튀는걸 좋아해."
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 s24 시리즈의 램 용량 비교해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "Galaxy S24 액정 교체 비용 얼마야?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24랑 호환되는 워치 제품 다 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시S24 5G 모델과 4G 모델의 경우도 각기 사용주파수가 다를수 있어?"
}'
```

속도 이슈

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 s23과 s24를 표로 비교해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24에 탑재된 글로나스 기술에 대해 설명해줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "갤럭시 S24 플러스의 램 용량 알려줘"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24의 ai 기능을 설명해봐"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "s24로 사람 사진 보정 가능한가요?"
}'
```

``bash
curl -X POST https://dialogflow-fulfillment-jr6kniykka-du.a.run.app/product/description \
-d '{
    "intentInfo": {"displayName": "galaxy.query"}, 
    "sessionInfo": {}, 
    "fulfillmentInfo": {"tag": "solution"}, 
    "text": "S23 FE에 대한 내용을 설명해주세요"
}'
```
