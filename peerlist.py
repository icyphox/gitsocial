from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis = redis.Redis()

@app.route('/api/set')
def write_redis():
    user_hash = request.args.get('hash')
    ip = request.args.get('ip')
    tip = request.args.get('tip')
    print(tip)
    print(type(tip))
    print(request.args)
    redis.set(user_hash, str(ip))
    redis.set(user_hash, str(tip))

@app.route('/api/get')
def read_redis():
    user_hash = request.args.get('hash')
    return jsonify(redis.get(user_hash))

if __name__ == "__main__":
    app.run()
