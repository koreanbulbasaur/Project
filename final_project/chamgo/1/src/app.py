from flask import Flask, request, jsonify
import logging

from helper.openai_api import text_complition


app = Flask(__name__)

# 로깅 레벨 설정 (예: INFO, ERROR, DEBUG 등)
app.logger.setLevel(logging.INFO)

# 로깅 핸들러 추가 (여러 개의 핸들러를 추가할 수 있음)
# 여기서는 단순히 콘솔에 로그를 출력하는 핸들러를 사용하겠습니다.
console_handler = logging.StreamHandler()
app.logger.addHandler(console_handler)

@app.route('/')
def home():
    return 'All is well...'


@app.route('/dialogflow/es/receiveMessage', methods=['POST'])
def esReceiveMessage():
    try:
        data = request.get_json()
        # You can use this action to do different things
        action = data['queryResult']['action']
        query_text = data['queryResult']['queryText']

        result = text_complition(query_text)

        if result['status'] == 1:
            return jsonify(
                {
                    'fulfillmentText': result['response']
                }
            )
    except Exception as e:
        # 오류 발생 시 로깅
        app.logger.error("An error occurred: %s", e)
        print("An error occurred: %s", e)
    return jsonify(
        {
            'fulfillmentText': '뭔가가 잘못 되었다'
        }
    )


@app.route('/dialogflow/cx/receiveMessage', methods=['POST'])
def cxReceiveMessage():
    try:
        data = request.get_json()
        # Use this tag peoperty to choose the action
        tag = data['fulfillmentInfo']['tag']
        query_text = data['text']

        result = text_complition(query_text)

        if result['status'] == 1:
            return jsonify(
                {
                    'fulfillment_response': {
                        'messages': [
                            {
                                'text': {
                                    'text': [result['response']],
                                    'redactedText': [result['response']]
                                },
                                'responseType': 'HANDLER_PROMPT',
                                'source': 'VIRTUAL_AGENT'
                            }
                        ]
                    }
                }
            )
    except:
        pass
    return jsonify(
        {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': ['Something went wrong.'],
                            'redactedText': ['Something went wrong.']
                        },
                        'responseType': 'HANDLER_PROMPT',
                        'source': 'VIRTUAL_AGENT'
                    }
                ]
            }
        }
    )
