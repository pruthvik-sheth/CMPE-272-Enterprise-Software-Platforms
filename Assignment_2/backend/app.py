from flask import Flask, request, jsonify
from flask_cors import CORS
from mastodon import Mastodon
from dotenv import load_dotenv
import os

# Written by Pruthvik Sheth and Yugm Patel

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Mastodon API client
mastodon = Mastodon(
    access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
    api_base_url=os.getenv('MASTODON_BASE_URL')
)

# Creating a new post
@app.route('/post', methods=['POST'])
def create_post():
    content = request.json.get('content')
    try:
        status = mastodon.status_post(content)
        give = jsonify({'id': str(status['id']), 'content': status['content']})
        print(give)
        return give, 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Retrieving a post by ID 
@app.route('/retrieve/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        status = mastodon.status(post_id)
        return jsonify({'id': str(status['id']), 'content': status['content']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Deleting a post by ID
@app.route('/delete/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        mastodon.status_delete(post_id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)