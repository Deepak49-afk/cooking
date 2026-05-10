from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from config import Config
from models.db import init_db
import os

# Initialize Flask Application
app = Flask(__name__, static_folder='../frontend', static_url_path='')
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize CORS
CORS(app, supports_credentials=True)

# Initialize SocketIO for real-time features
socketio = SocketIO(app, cors_allowed_origins="*")

from flask_socketio import join_room, emit

@socketio.on('connect')
def handle_connect():
    pass

@socketio.on('join')
def handle_join(data):
    user_id = data.get('user_id')
    role = data.get('role', 'customer')
    if user_id:
        join_room(user_id)
    if role in ['chef', 'admin']:
        join_room(role)

@socketio.on('place_order')
def handle_place_order(data):
    # pyrefly: ignore [unexpected-keyword]
    emit('new_order', data, room='chef')
    # pyrefly: ignore [unexpected-keyword]
    emit('new_order', data, room='admin')

@socketio.on('order_status_update')
def handle_order_status_update(data):
    customer_id = data.get('customer_id')
    if customer_id and data.get('status') == 'Completed':
        # pyrefly: ignore [unexpected-keyword]
        emit('notification', {'message': "Your order is completed and you will receive it in a few minutes!", 'type': 'order'}, room=customer_id)
    # pyrefly: ignore [unexpected-keyword]
    emit('order_status_update', data, room='admin')

# Initialize MongoDB Collections and Indexes
with app.app_context():
    init_db()

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """Basic health check endpoint"""
    return jsonify({
        "status": "success",
        "message": "Cooing API is running"
    }), 200

# Import and register blueprints
from routes.auth_routes import auth_bp
from routes.profile_routes import profile_bp
from routes.recipe_routes import recipe_bp
from routes.social_routes import social_bp
from routes.order_routes import order_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(profile_bp, url_prefix='/api/profile')
app.register_blueprint(recipe_bp, url_prefix='/api/recipes')
app.register_blueprint(social_bp, url_prefix='/api/social')
app.register_blueprint(order_bp, url_prefix='/api/orders')

from flask import send_from_directory
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    print("Starting Cooing Backend Server...")
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
