from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis = redis.Redis()

@app.route('/api/set')
def write_redis():
    user_hash = request.args.get('hash')
    ip = request.args.get('ip')
    commit = request.args.get('tip')
    redis.set(user_hash, set([ip, tip]))

@app.route('/api/get')
def read_redis():
    user_hash = request.args.get('hash')
    return jsonify(redis.get(user_hash))

if __name__ == "__main__":
    app.run()
