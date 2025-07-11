import os
import logging
from flask import Flask, render_template, request, jsonify
from password_generator import generate_password, check_password_strength

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

@app.route('/')
def index():
    """Main page with password generator interface"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate password based on user preferences"""
    try:
        data = request.get_json()
        
        # Extract parameters from request
        length = int(data.get('length', 12))
        include_uppercase = data.get('uppercase', True)
        include_lowercase = data.get('lowercase', True)
        include_numbers = data.get('numbers', True)
        include_special = data.get('special', False)
        
        # Validate input
        if length < 1 or length > 128:
            return jsonify({'error': 'Password length must be between 1 and 128 characters'}), 400
        
        if not any([include_uppercase, include_lowercase, include_numbers, include_special]):
            return jsonify({'error': 'At least one character type must be selected'}), 400
        
        # Generate password
        password = generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_numbers=include_numbers,
            include_special=include_special
        )
        
        # Check password strength
        strength = check_password_strength(password)
        
        return jsonify({
            'password': password,
            'strength': strength
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error generating password: {str(e)}")
        return jsonify({'error': 'An error occurred while generating the password'}), 500

@app.route('/check-strength', methods=['POST'])
def check_strength():
    """Check strength of a given password"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({'error': 'Password is required'}), 400
        
        strength = check_password_strength(password)
        return jsonify({'strength': strength})
        
    except Exception as e:
        app.logger.error(f"Error checking password strength: {str(e)}")
        return jsonify({'error': 'An error occurred while checking password strength'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
