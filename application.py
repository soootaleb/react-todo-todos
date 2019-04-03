from flask import Flask, request

import json

application = Flask(__name__)

# Using a simple dict for the persistance
# YES, the database is lost if the environment is restarted
database = {}

# Messages are
# {
#     "message": 'ADD_CLIENT' | 'ADD_TODO',
#     "data": {
#         "id": int
#         "label": string
#     }
# }

@application.route('/', methods=['POST'])
def todo():
    body = json.loads(request.data.decode())
    message = body['message']
    data = body['data']

    if message == 'ADD_CLIENT':
        user_id = data['id']
        database[user_id] = [] # Empty list for a given ID
        print('Added client {}'.format(user_id))
    elif message == 'ADD_TODO':
        user_id = data['id']
        label = data['label']
        database[user_id].append(label) # Add todo for a given id
        print('Added todo "{}" for client {}'.format(user_id, label))

    return True

if __name__ == "__main__":
    application.debug = True
    application.run()