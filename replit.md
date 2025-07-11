# Advanced Password Generator

## Overview

This is a web-based password generator application built with Flask that allows users to generate secure passwords with customizable criteria and check password strength. The application features a modern, responsive frontend with real-time password strength analysis and provides both password generation and validation capabilities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Technology**: HTML5, CSS3, JavaScript with Bootstrap 5 for responsive design
- **Styling**: Custom CSS with gradient backgrounds, glassmorphism effects, and smooth animations
- **Interactivity**: Vanilla JavaScript for DOM manipulation, AJAX requests, and real-time UI updates
- **UI Framework**: Bootstrap 5 with dark theme for consistent styling and responsive layout

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Architecture Pattern**: Simple MVC pattern with route handlers
- **Entry Point**: `main.py` serves as the application entry point
- **Core Logic**: Separated into `password_generator.py` module for business logic
- **Session Management**: Basic Flask session handling with configurable secret key

### API Structure
- **RESTful Endpoints**: JSON-based API for password generation
- **Route**: `POST /generate` - Accepts password criteria and returns generated password with strength analysis
- **Error Handling**: Proper HTTP status codes and error messages for validation failures

## Key Components

### Password Generation Module (`password_generator.py`)
- **Purpose**: Core business logic for password generation and strength validation
- **Features**: 
  - Customizable character sets (uppercase, lowercase, numbers, special characters)
  - Length validation (1-128 characters)
  - Ensures at least one character from each selected type
- **Security**: Uses Python's `random` module for cryptographically suitable randomness

### Web Application (`app.py`)
- **Purpose**: Flask web server and API endpoints
- **Features**:
  - Main page rendering
  - Password generation API endpoint
  - Input validation and error handling
  - JSON response formatting

### Frontend Interface
- **Main Template**: `templates/index.html` - Single-page application interface
- **JavaScript**: `static/script.js` - Client-side logic and AJAX communication
- **Styling**: `static/style.css` - Custom styling with modern design elements

## Data Flow

1. **User Input**: User configures password criteria through web interface (length, character types)
2. **Client Validation**: JavaScript validates inputs before sending request
3. **API Request**: AJAX POST request sent to `/generate` endpoint with JSON payload
4. **Server Processing**: Flask validates parameters and calls password generation logic
5. **Password Generation**: Core module generates password based on criteria
6. **Strength Analysis**: Password strength is evaluated and scored
7. **Response**: JSON response with generated password and strength metrics
8. **UI Update**: JavaScript updates interface with new password and strength indicators

## External Dependencies

### Python Dependencies
- **Flask**: Web framework for routing and request handling
- **Standard Library**: Uses built-in `random`, `string`, `re`, `os`, and `logging` modules

### Frontend Dependencies
- **Bootstrap 5**: CSS framework via CDN for responsive design and components
- **Font Awesome 6**: Icon library via CDN for UI icons
- **No JavaScript frameworks**: Pure vanilla JavaScript for lightweight performance

### Development Dependencies
- **Environment Variables**: Uses `SESSION_SECRET` for Flask session configuration
- **Debug Mode**: Configurable debug mode for development

## Deployment Strategy

### Development Setup
- **Entry Point**: `main.py` runs Flask development server
- **Host Configuration**: Binds to `0.0.0.0:5000` for external access
- **Debug Mode**: Enabled for development with automatic reloading

### Production Considerations
- **Secret Key**: Environment variable configuration for session security
- **Static Files**: Flask serves static assets (CSS, JS) directly
- **Error Handling**: Comprehensive validation and error responses
- **Logging**: Basic logging configuration for debugging

### File Structure
```
/
├── main.py              # Application entry point
├── app.py               # Flask application and routes
├── password_generator.py # Core password logic
├── templates/
│   └── index.html       # Main web interface
└── static/
    ├── style.css        # Custom styling
    └── script.js        # Client-side logic
```

The application is designed as a self-contained web service with minimal external dependencies, making it suitable for various deployment environments including Replit, Docker containers, or traditional web servers.