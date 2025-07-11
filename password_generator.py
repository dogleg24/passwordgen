import random
import string
import re

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_numbers=True, include_special=False):
    """
    Generate a random password based on specified criteria.
    
    Args:
        length (int): Desired length of the password
        include_uppercase (bool): Include uppercase letters (A-Z)
        include_lowercase (bool): Include lowercase letters (a-z)
        include_numbers (bool): Include numbers (0-9)
        include_special (bool): Include special characters
    
    Returns:
        str: Generated password
    
    Raises:
        ValueError: If no character types are selected or invalid length
    """
    if length <= 0:
        raise ValueError("Password length must be a positive number")
    
    # Build character set based on user preferences
    character_set = ""
    
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_numbers:
        character_set += string.digits
    if include_special:
        character_set += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Check if at least one character type is selected
    if not character_set:
        raise ValueError("At least one character type must be selected")
    
    # Generate password ensuring at least one character from each selected type
    password = []
    
    # Add at least one character from each selected type
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Fill the rest of the password length with random characters from the full set
    for _ in range(length - len(password)):
        password.append(random.choice(character_set))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    """
    Analyze password strength and return detailed feedback.
    
    Args:
        password (str): Password to analyze
    
    Returns:
        dict: Dictionary containing strength score, level, and feedback
    """
    if not password:
        return {
            'score': 0,
            'level': 'Very Weak',
            'feedback': ['Password cannot be empty'],
            'color': 'danger'
        }
    
    score = 0
    feedback = []
    
    # Length scoring
    length = len(password)
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
        feedback.append("Consider using at least 12 characters for better security")
    else:
        score += 5
        feedback.append("Password is too short - use at least 8 characters")
    
    # Character variety scoring
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digits = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
    
    character_types = sum([has_upper, has_lower, has_digits, has_special])
    
    if character_types >= 4:
        score += 25
    elif character_types >= 3:
        score += 20
        feedback.append("Consider adding special characters for stronger security")
    elif character_types >= 2:
        score += 10
        feedback.append("Use a mix of uppercase, lowercase, numbers, and special characters")
    else:
        score += 5
        feedback.append("Password should contain different types of characters")
    
    # Pattern checking
    if not re.search(r'(.)\1{2,}', password):  # No repeated characters
        score += 15
    else:
        feedback.append("Avoid repeating the same character multiple times")
    
    # Common patterns
    if not re.search(r'(abc|123|qwe|asd|zxc)', password.lower()):
        score += 15
    else:
        feedback.append("Avoid common keyboard patterns or sequences")
    
    # Entropy bonus for longer passwords with variety
    if length > 16 and character_types >= 3:
        score += 20
    
    # Determine strength level and color
    if score >= 90:
        level = 'Very Strong'
        color = 'success'
    elif score >= 70:
        level = 'Strong'
        color = 'success'
    elif score >= 50:
        level = 'Moderate'
        color = 'warning'
    elif score >= 30:
        level = 'Weak'
        color = 'warning'
    else:
        level = 'Very Weak'
        color = 'danger'
    
    # Add positive feedback for strong passwords
    if score >= 70 and not feedback:
        feedback.append("Excellent password strength!")
    
    return {
        'score': min(score, 100),  # Cap at 100
        'level': level,
        'feedback': feedback,
        'color': color
    }
