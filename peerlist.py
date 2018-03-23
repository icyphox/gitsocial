from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis = redis.Redis()

@app.route('/api/set_peer')
def write_redis():
    user_hash = request.args.get('hash')
    ip = request.args.get('ip')
    tip = request.args.get('tip')
    print(tip)
    print(type(tip))
    print(request.args)
    redis.set(user_hash, str(ip) + '/' + str(tip))
    
    return "OK"


@app.route('/api/get_peer')
def read_redis():
    user_hash = request.args.get('hash')
    return jsonify(redis.get(user_hash))


if __name__ == "__main__":
    app.run()
