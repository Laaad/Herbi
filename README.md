# Herbi - AI-Powered Food Classification System

[![Python](https://img.shields.io/badge/Python-3.13.2-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.3-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

Herbi is an intelligent Django-based application that uses AI to classify food conversations and determine whether they represent vegetarian or vegan dietary preferences. The system simulates conversations between AI agents about food preferences and automatically categorizes the responses.

## 🚀 Features

- **AI-Powered Food Classification**: Uses OpenAI's language models to analyze food preferences
- **Conversation Simulation**: Simulates realistic food-related conversations between AI agents
- **RESTful API**: Provides endpoints to retrieve vegetarian/vegan conversation data
- **Docker Support**: Containerized deployment for easy setup and scaling
- **Threaded Processing**: Supports concurrent simulation processing for high throughput
- **Comprehensive Testing**: Unit tests for food classification logic

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Architecture](#architecture)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

## 🔧 Prerequisites

- Python 3.13.2 or higher
- Docker and Docker Compose (for containerized deployment)
- OpenAI API key
- Git

## 📦 Installation

### Option 1: Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd herbi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env.django.dev` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   OPENAI_SECRET=your-openai-api-key-here
   ```

5. **Run database migrations**
   ```bash
   cd herbiapi
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

### Option 2: Docker Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd herbi
   ```

2. **Set up environment variables**
   Create a `.env.django.dev` file as shown above.

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

The application will be available at `http://localhost:8000`

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Django secret key | Yes | - |
| `DEBUG` | Debug mode | No | False |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | No | [] |
| `OPENAI_SECRET` | OpenAI API key | Yes | - |

### Django Settings

The project uses a modular settings structure:
- `herbiapi/core/settings/base.py` - Base settings
- `herbiapi/core/settings/dev.py` - Development settings
- `herbiapi/core/settings/prod.py` - Production settings

## 🚀 Usage

### Running the Application

1. **Start the Django server**
   ```bash
   cd herbiapi
   python manage.py runserver
   ```

2. **Access the admin interface**
   - URL: `http://localhost:8000/admin/`
   - Default credentials: `admin/admin` (when using Docker)

### Simulating Conversations

The application includes a management command to simulate food conversations:

```bash
cd herbiapi
python manage.py simulate <count> [--threads <thread_count>]
```

**Examples:**
```bash
# Simulate 100 conversations with default 5 threads
python manage.py simulate 100

# Simulate 50 conversations with 10 threads
python manage.py simulate 50 --threads 10
```

### API Endpoints

- **Admin Interface**: `http://localhost:8000/admin/`
- **Vegetarian/Vegan Conversations**: `http://localhost:8000/api/veg-conversations/`

## 📚 API Documentation

### GET /api/veg-conversations/

Retrieves all conversations that were classified as vegetarian or vegan.

**Response Format:**
```json
[
  {
    "id": 1,
    "is_veg": true,
    "foods": ["tofu", "rice", "vegetables"]
  }
]
```

**Example Request:**
```bash
curl http://localhost:8000/api/veg-conversations/
```

## 🏗️ Architecture

### Project Structure

```
herbi/
├── herbiapi/                    # Main Django application
│   ├── chat/                   # Chat application
│   │   ├── food_classifiers/   # Food classification logic
│   │   ├── management/         # Django management commands
│   │   ├── migrations/         # Database migrations
│   │   ├── tests/             # Test files
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # API serializers
│   │   └── views.py           # API views
│   ├── core/                  # Django core settings
│   │   ├── settings/          # Environment-specific settings
│   │   ├── urls.py            # Main URL configuration
│   │   └── wsgi.py            # WSGI configuration
│   └── utils/                 # Utility modules
│       ├── conversation_simulator.py
│       ├── llm_interface.py
│       └── openai_client.py
├── docker-compose.yml         # Docker Compose configuration
├── dockerfile                 # Docker image definition
└── requirements.txt           # Python dependencies
```

### Key Components

#### 1. Food Classification System
- **Base Classifier** (`chat/food_classifiers/base.py`): Abstract base class for food classifiers
- **LLM Classifier** (`chat/food_classifiers/llm_classifier.py`): OpenAI-powered food classification

#### 2. Conversation Simulation
- **Conversation Simulator** (`utils/conversation_simulator.py`): Manages AI agent interactions
- **LLM Interface** (`utils/llm_interface.py`): Abstract interface for language models

#### 3. Data Models
- **SimulatedConversation**: Stores conversation data and classification results

#### 4. API Layer
- **VegetarianOrVeganConversationsView**: REST API endpoint for retrieving classified conversations

## 🧪 Testing

### Running Tests

```bash
cd herbiapi
python -m pytest
```

### Test Structure

- `chat/tests/test_food_classifiers.py`: Tests for food classification logic
- Tests cover vegetarian/vegan detection and food extraction

### Example Test

```python
def test_analyze_meat_detection(self, classifier):
    result = classifier._analyze(["egg", "rice"])
    assert result['is_vegan'] is False
    assert result['is_vegetarian'] is True
```

## 🚀 Deployment

### Production Deployment

1. **Update settings for production**
   - Set `DEBUG=False`
   - Configure proper `ALLOWED_HOSTS`
   - Use environment-specific settings

2. **Database setup**
   - Consider using PostgreSQL for production
   - Set up proper database credentials

3. **Static files**
   ```bash
   python manage.py collectstatic
   ```

4. **Security considerations**
   - Use HTTPS
   - Configure proper CORS settings
   - Set up proper authentication

### Docker Production

```bash
# Build production image
docker build -t herbi:production .

# Run with production settings
docker run -d -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY=your-secret-key \
  -e OPENAI_SECRET=your-openai-key \
  herbi:production
```

## 🤝 Contributing

### Development Guidelines

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use meaningful variable and function names
   - Add docstrings to functions and classes

2. **Testing**
   - Write tests for new features
   - Ensure all tests pass before submitting

3. **Git Workflow**
   ```bash
   git checkout -b feature/your-feature-name
   # Make your changes
   git add .
   git commit -m "Add feature description"
   git push origin feature/your-feature-name
   ```

### Best Practices

- Use type hints for better code clarity
- Keep functions simple and focused
- Avoid global variables
- Use list comprehensions when appropriate
- Document complex logic

## 📝 License

[Add your license information here]

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Changelog

### Version 1.0.0
- Initial release
- AI-powered food classification
- Conversation simulation
- REST API endpoints
- Docker support

---

**Note**: This project requires an OpenAI API key to function. Make sure to set up your API key in the environment variables before running the application. 