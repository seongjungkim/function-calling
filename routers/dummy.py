import sys

# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/SimpleResponse.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/SimpleResponseSsml.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/SimpleResponseSsml.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/SimpleResponseTts.json

welcome_json = {
    "id": "d052d79c458d4769a452756f2edaa6ca",
    "result": {
        "source": "dialogflow",
        "score": 1.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "Gemini 1.5 Pro는 폭넓은 작업을 망라하여 크기를 조정할 수 있도록 최적화된 중간 규모의 멀티모달 모델입니다. \r\n이 모델은 실험적인 1백만 개의 토큰을 포함하는 새로운 컨텍스트 창을 제공하며 Google AI Studio에서 시험 사용할 수 있습니다. Google AI Studio는 Gemini 모델을 사용해 개발할 수 있는 가장 빠른 방법이며, 개발자가 애플리케이션에 Gemini API를 손쉽게 통합할 수 있도록 지원합니다. Gemini 1.5 Pro는 180여 개 국가 및 지역에서 38개 언어로 제공됩니다.",
                    "displayText": "Gemini 1.5 Pro는 폭넓은 작업을 망라하여 크기를 조정할 수 있도록 최적화된 중간 규모의 멀티모달 모델입니다. \r\n이 모델은 실험적인 1백만 개의 토큰을 포함하는 새로운 컨텍스트 창을 제공하며 Google AI Studio에서 시험 사용할 수 있습니다. Google AI Studio는 Gemini 모델을 사용해 개발할 수 있는 가장 빠른 방법이며, 개발자가 애플리케이션에 Gemini API를 손쉽게 통합할 수 있도록 지원합니다. Gemini 1.5 Pro는 180여 개 국가 및 지역에서 38개 언어로 제공됩니다."
                }
            ]
        },
        "suggestions": [
            {
                "title": "simple response"
            },
            {
                "title": "browse carousel"
            },
            {
                "title": "basic card"
            },
            {
                "title": "Never mind"
            }
        ],
        "payload": {
            "intentName": "Default Welcome Intent",
            "currentPage": "Start Page",
            "parameters": {}
        }
    },
    "status": {
        "code": 200,
        "errorType": "success"
    },
    "genAi": True,
    "eventTags": []
}

assistant_guide_json = {
    "id": "b61b74b83ed144edb39cf27bb7a99322",
    "result": {
        "source": "dialogflow",
        "score": 1.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "Gemini 챗봇은 광범위한 분야에 대화형 인공지능으로, 주로 질문 및 답변(Q\u0026A)과 정보 요약에 최적화되어 있습니다. \n사용자가 제공한 정보가 구체적이고 명확할수록, Gemini는 더 정확하고 유용한 답변을 제공할 수 있습니다.\n\n예를 들어, 좋은 질문은 \n\"이름, 나이, 과거병력, 복용중인 약물, 현재 불편한 곳을 포함한 환자 정보를 한 문단으로 요약해주세요.\"\n와 같이 특정 상황을 명확하게 설명합니다. \n반면, 불명확한 질문은 \"요약해주세요\"와 같이 너무 포괄적인 질문을 말합니다.\n\n질문은 구체적이고 명확하며, 한 번에 하나의 요청을 보내는 것이 좋습니다.\n\n\n답변을 이전 질문 (혹은 정보)를 참조하지 않고 새로 시작하려면, Reset 혹은 초기화라고 입력해주세요.\n원하지 않는 이전 내용을 포함한다면 Reset 혹은 초기화라고 입력해주세요.\n\n\n채팅 간 최근 4번의 채팅까지 현재 인지 및 참조해서 답변하도록 설계되어있습니다. (Reset의 경우 초기화) \n\n\n질문의 경우, 한글과 영어 두가지 모두 사용가능합니다.\n다만 답변의 경우, 영어로 답변하는 경향이 커, 한글로 받고 싶으시다면 추가로 \"Translate it in Korean\" 혹은 \"한글로 번역해주세요.\" 라고 입력해주세요. \n\n\n\n질문예시 1 :\nMedical Information : \n나이 : 55세 \n인종 : 백인\n성별 : 여성\n병력 : 5년 전 진단된 유방암, 현재 관해 중\n현재 약물 : 매일 타목시펜 20mg과 레트로졸 2.5mg을 복용중\n\n위 환자가 오른쪽 상단 가슴의 강한 통증을 느끼고 있습니다.\n환자의 정보와 통증 정도를 보았을때 가장 의심스러운 질병은 어떤 것인가요?\n\n질문예시 2 :\nWhat causes you to get ringworm?\n\n질문예시 3:\nQuestion 1: Which medication causes the maximum increase in prolactin level?\n(A) Risperidone\n(B) Clozapine\n(C) Olanzapine\n(D) Aripiprazole\n\n*질문예시 4:\nQ1) 환자는 52세 남성으로, 기존 질환인 2형 당뇨와 고혈압으로 인해 합병증이 의심되는 증상을 보이고 있습니다. 최근에는 피로감이 증가하고 시력 문제를 호소했습니다. 어떤 검사를 권장하나요?\nQ2) 심혈관 합병증 위험을 추가로 평가하기 위해 어떤 질문을 해야 할까요?\nQ3) 내용을 제 노트에 간단히 요약해 줄 수 있을까요?\n\n질문예시 4의 순서와 같이 진행할 경우에, 답변받은 내용과 입력한 내용에 대해서 노트의 형식으로 요약받을 수도 있습니다.",
                    "displayText": "Gemini 챗봇은 광범위한 분야에 대화형 인공지능으로, 주로 질문 및 답변(Q\u0026A)과 정보 요약에 최적화되어 있습니다. \n사용자가 제공한 정보가 구체적이고 명확할수록, Gemini는 더 정확하고 유용한 답변을 제공할 수 있습니다.\n\n예를 들어, 좋은 질문은 \n\"이름, 나이, 과거병력, 복용중인 약물, 현재 불편한 곳을 포함한 환자 정보를 한 문단으로 요약해주세요.\"\n와 같이 특정 상황을 명확하게 설명합니다. \n반면, 불명확한 질문은 \"요약해주세요\"와 같이 너무 포괄적인 질문을 말합니다.\n\n질문은 구체적이고 명확하며, 한 번에 하나의 요청을 보내는 것이 좋습니다.\n\n\n답변을 이전 질문 (혹은 정보)를 참조하지 않고 새로 시작하려면, Reset 혹은 초기화라고 입력해주세요.\n원하지 않는 이전 내용을 포함한다면 Reset 혹은 초기화라고 입력해주세요.\n\n\n채팅 간 최근 4번의 채팅까지 현재 인지 및 참조해서 답변하도록 설계되어있습니다. (Reset의 경우 초기화) \n\n\n질문의 경우, 한글과 영어 두가지 모두 사용가능합니다.\n다만 답변의 경우, 영어로 답변하는 경향이 커, 한글로 받고 싶으시다면 추가로 \"Translate it in Korean\" 혹은 \"한글로 번역해주세요.\" 라고 입력해주세요. \n\n\n\n질문예시 1 :\nMedical Information : \n나이 : 55세 \n인종 : 백인\n성별 : 여성\n병력 : 5년 전 진단된 유방암, 현재 관해 중\n현재 약물 : 매일 타목시펜 20mg과 레트로졸 2.5mg을 복용중\n\n위 환자가 오른쪽 상단 가슴의 강한 통증을 느끼고 있습니다.\n환자의 정보와 통증 정도를 보았을때 가장 의심스러운 질병은 어떤 것인가요?\n\n질문예시 2 :\nWhat causes you to get ringworm?\n\n질문예시 3:\nQuestion 1: Which medication causes the maximum increase in prolactin level?\n(A) Risperidone\n(B) Clozapine\n(C) Olanzapine\n(D) Aripiprazole\n\n*질문예시 4:\nQ1) 환자는 52세 남성으로, 기존 질환인 2형 당뇨와 고혈압으로 인해 합병증이 의심되는 증상을 보이고 있습니다. 최근에는 피로감이 증가하고 시력 문제를 호소했습니다. 어떤 검사를 권장하나요?\nQ2) 심혈관 합병증 위험을 추가로 평가하기 위해 어떤 질문을 해야 할까요?\nQ3) 내용을 제 노트에 간단히 요약해 줄 수 있을까요?\n\n질문예시 4의 순서와 같이 진행할 경우에, 답변받은 내용과 입력한 내용에 대해서 노트의 형식으로 요약받을 수도 있습니다."
                }
            ]
        },
        "payload": {
            "intentName": "chatbot_guide",
            "currentPage": "Start Page",
            "parameters": {}
        }
    },
    "status": {
        "code": 200,
        "errorType": "success"
    },
    "eventTags": []
}

test_json = {
    "result": {
        "source": "dialogflow",
        "score": 0.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": " As a medical chatbot, I am designed to provide information and answer questions related to medical topics. If you have a specific medical question or concern, I can try to help you find the information you need.",
                    "ssml": "",
                    "displayText": " As a medical chatbot, I am designed to provide information and answer questions related to medical topics. If you have a specific medical question or concern, I can try to help you find the information you need."
                }
            ]
        },
        "suggestions": [
            {
                "title": "simple response"
            },
            {
                "title": "browse carousel"
            },
            {
                "title": "basic card"
            },
            {
                "title": "Never mind"
            }
        ]
    },
    "status": {
        "code": 200
    },
    "genAi": True,
    "eventTags": []
}

# https://developers.google.com/assistant/df-asdk/simple-responses?hl=ko

simple_response_json = {
    "result": {
        "source": "dialogflow",
        "score": 0.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "간단한 응답은 채팅 풍선의 형태를 취하며 소리에 텍스트 음성 변환(TTS) 또는 음성 합성 마크업 언어 (SSML)를 사용합니다.\r\n\r\nTTS 텍스트는 기본적으로 채팅 풍선 콘텐츠로 사용됩니다. 텍스트의 시각적 측면이 필요에 맞는 경우 채팅 풍선의 표시 텍스트를 지정할 필요가 없습니다.\r\n\r\n대화 디자인 가이드라인을 검토하여 이러한 시각적 요소를 작업에 통합하는 방법을 알아볼 수도 있습니다.",
                    "ssml": "",
                    "displayText": " 간단한 응답은 채팅 풍선의 형태를 취하며 소리에 텍스트 음성 변환(TTS) 또는 음성 합성 마크업 언어 (SSML)를 사용합니다.\r\n\r\nTTS 텍스트는 기본적으로 채팅 풍선 콘텐츠로 사용됩니다. 텍스트의 시각적 측면이 필요에 맞는 경우 채팅 풍선의 표시 텍스트를 지정할 필요가 없습니다.\r\n\r\n대화 디자인 가이드라인을 검토하여 이러한 시각적 요소를 작업에 통합하는 방법을 알아볼 수도 있습니다."
                }
            ]
        },
        "suggestions": [
            {
                "title": "simple response"
            },
            {
                "title": "browse carousel"
            },
            {
                "title": "basic card"
            },
            {
                "title": "Never mind"
            }
        ]
    },
    "status": {
        "code": 200
    },
    "genAi": True,
    "eventTags": []
}

# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/BasicCard.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/Suggestions.json
# https://developers.google.com/assistant/df-asdk/rich-responses?hl=ko#BasicCardSamples

basic_card_json = {
    "result": {
        "source": "dialogflow",
        "score": 0.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "기본 카드는 주로 디스플레이용으로 사용합니다. 간결하고 사용자에게 핵심 (또는 요약) 정보를 제시하며 개발자가 선택할 경우 사용자가 자세히 알아볼 수 있도록 설계되었습니다 (웹링크 사용).",
                    "ssml": "",
                    "displayText": "기본 카드는 주로 디스플레이용으로 사용합니다. 간결하고 사용자에게 핵심 (또는 요약) 정보를 제시하며 개발자가 선택할 경우 사용자가 자세히 알아볼 수 있도록 설계되었습니다 (웹링크 사용)."
                }
            ]
        },
        "basicCard": {
            "title": "베이직카드 타이틀",
            "subtitle": "베이직카드 서브타이틀",
            "formattedText": "This is a basic card.  Text in a basic card can include \"quotes\" and\n    most other unicode characters including emojis.  Basic cards also support\n    some markdown formatting like *emphasis* or _italics_, **strong** or\n    __bold__, and ***bold itallic*** or ___strong emphasis___ as well as other\n    things like line  \nbreaks",
            "image": {
                "imageUri": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                "accessibilityText": "Google Logo"
            },
            "buttons": [
                {
                    "title": "Rich Response > Basic Card",
                    "openUriAction": {
                        "uri": "https://developers.google.com/assistant/df-asdk/rich-responses?hl=ko#basic_card"
                    }
                }
            ]
        },
        "suggestions": [
            {
                "title": "browse carousel"
            },
            {
                "title": "basic card"
            },
            {
                "title": "Never mind"
            }
        ],
        "linkOutSuggestion": {
            "destinationName": "Website",
            "url": "https://assistant.google.com"
        }
    },
    "status": {
        "code": 200
    },
    "genAi": True,
    "eventTags": []
}

# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/BrowseCarousel.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/Suggestions.json
# https://developers.google.com/assistant/df-asdk/rich-responses?hl=ko#BrowsingCarouselSamples

browse_carousel_json = {
    "result": {
        "source": "dialogflow",
        "score": 0.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "탐색 캐러셀은 사용자가 세로로 스크롤하고 컬렉션의 타일을 선택할 수 있는 리치 응답입니다. 탐색 캐러셀은 웹브라우저 (또는 모든 타일이 AMP를 지원하는 경우 AMP 브라우저)에서 선택한 타일을 열어 웹 콘텐츠용으로 특별히 설계되었습니다. 탐색 캐러셀은 나중에 찾아볼 수 있도록 사용자의 어시스턴트 표시 경로에도 유지됩니다.",
                    "ssml": "",
                    "displayText": "탐색 캐러셀은 사용자가 세로로 스크롤하고 컬렉션의 타일을 선택할 수 있는 리치 응답입니다. 탐색 캐러셀은 웹브라우저 (또는 모든 타일이 AMP를 지원하는 경우 AMP 브라우저)에서 선택한 타일을 열어 웹 콘텐츠용으로 특별히 설계되었습니다. 탐색 캐러셀은 나중에 찾아볼 수 있도록 사용자의 어시스턴트 표시 경로에도 유지됩니다."
                }
            ]
        },
        "browseCarousel": {
            "items": [
                {
                    "title": "samsung.com",
                    "openUrlAction": {
                        "url": "https://www.samsung.com/sec/"
                    },
                    "description": "삼성닷컴",
                    "footer": "삼성닷컴",
                    "image": {
                        "imageUri": "https://cdn.worldvectorlogo.com/logos/samsung-8.svg",
                        "accessibilityText": "samsung.com Logo"
                    }
                },
                {
                    "title": "Gemini 1.5",
                    "openUrlAction": {
                        "url": "https://developers.googleblog.com/ko/gemini-15-our-next-generation-model-now-available-for-private-preview-in-google-ai-studio/"
                    },
                    "description": "Google AI Studio에서 비공개 미리보기로 이용 가능한 차세대 모델",
                    "footer": "Gemini",
                    "image": {
                        "imageUri": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/344px-Google_Gemini_logo.svg.png",
                        "accessibilityText": "Google Logo"
                    }
                }
            ]
        },
        "suggestions": [
            {
                "title": "browse carousel"
            },
            {
                "title": "basic card"
            },
            {
                "title": "Never mind"
            }
        ],
        "linkOutSuggestion": {
            "destinationName": "Website",
            "url": "https://assistant.google.com"
        }
    },
    "status": {
        "code": 200
    },
    "genAi": True,
    "eventTags": []
}

# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/BrowseCarousel.json
# https://github.com/dialogflow/fulfillment-webhook-json/blob/master/responses/v2/ActionsOnGoogle/RichResponses/Suggestions.json
# https://developers.google.com/assistant/df-asdk/rich-responses?hl=ko#BrowsingCarouselSamples

carousel_select_json = {
    "result": {
        "source": "dialogflow",
        "score": 0.0,
        "simpleResponses": {
            "simpleResponses": [
                {
                    "textToSpeech": "탐색 캐러셀은 사용자가 세로로 스크롤하고 컬렉션의 타일을 선택할 수 있는 리치 응답입니다. 탐색 캐러셀은 웹브라우저 (또는 모든 타일이 AMP를 지원하는 경우 AMP 브라우저)에서 선택한 타일을 열어 웹 콘텐츠용으로 특별히 설계되었습니다. 탐색 캐러셀은 나중에 찾아볼 수 있도록 사용자의 어시스턴트 표시 경로에도 유지됩니다.",
                    "ssml": "",
                    "displayText": "탐색 캐러셀은 사용자가 세로로 스크롤하고 컬렉션의 타일을 선택할 수 있는 리치 응답입니다. 탐색 캐러셀은 웹브라우저 (또는 모든 타일이 AMP를 지원하는 경우 AMP 브라우저)에서 선택한 타일을 열어 웹 콘텐츠용으로 특별히 설계되었습니다. 탐색 캐러셀은 나중에 찾아볼 수 있도록 사용자의 어시스턴트 표시 경로에도 유지됩니다."
                }
            ]
        },
        "carouselSelect": {
            "items": [
                {
                    "title": "samsung.com",
                    "openUrlAction": {
                        "url": "https://www.samsung.com/sec/"
                    },
                    "description": "삼성닷컴",
                    "footer": "삼성닷컴",
                    "image": {
                        "imageUri": "https://cdn.worldvectorlogo.com/logos/samsung-8.svg",
                        "accessibilityText": "samsung.com Logo"
                    }
                },
                {
                    "title": "Gemini 1.5",
                    "openUrlAction": {
                        "url": "https://developers.googleblog.com/ko/gemini-15-our-next-generation-model-now-available-for-private-preview-in-google-ai-studio/"
                    },
                    "description": "Google AI Studio에서 비공개 미리보기로 이용 가능한 차세대 모델",
                    "footer": "Gemini",
                    "image": {
                        "imageUri": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/344px-Google_Gemini_logo.svg.png",
                        "accessibilityText": "Google Logo"
                    }
                }
            ]
        },
        "suggestions": [
            {
                "title": "25"
            },
            {
                "title": "45"
            },
            {
                "title": "Never mind"
            }
        ],
        "linkOutSuggestion": {
            "destinationName": "Website",
            "url": "https://assistant.google.com"
        }
    },
    "status": {
        "code": 200
    },
    "genAi": True,
    "eventTags": []
}