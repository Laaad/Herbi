# Herbi API

A Django REST API for classifying and managing vegetarian/vegan food conversations using AI-powered classification.

## 🍃 What is Herbi?

Herbi is an intelligent API that helps classify conversations about food to determine if they indicate vegetarian or vegan dietary preferences. It uses AI models to analyze food-related conversations and extract structured data about food consumption patterns.

## ✨ Features

- **AI-Powered Classification**: Uses OpenAI models to classify food conversations
- **RESTful API**: Clean, documented API endpoints with Swagger UI
- **Conversation Simulation**: Tools for generating and simulating food-related conversations
- **Food Extraction**: Extracts structured food data from natural language
- **Authentication**: Secure user authentication system
- **Interactive Documentation**: Built-in Swagger UI for API exploration

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- PostgreSQL (optional, SQLite is used by default)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd herbi
   ```

2. **Install dependencies**
   ```bash
   cd herbiapi
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env.django.dev` file in the `herbiapi` directory:
   ```env
   OPENAI_SECRET=your_openai_api_key_here
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/
- **ReDoc**: http://localhost:8000/redoc/
- **Raw Schema**: http://localhost:8000/schema/

## 🔌 API Endpoints

### Authentication
- `POST /login/` - User login with username and password

### Conversations
- `GET /conversations/` - List all conversations with extracted food data
- `GET /conversations/vegs/` - List only vegetarian/vegan conversations

### Admin
- `GET /admin/` - Django admin interface

### Documentation
- `GET /` - Swagger UI documentation
- `GET /redoc/` - ReDoc documentation
- `GET /schema/` - OpenAPI schema

## 🏗️ Project Structure

```
herbiapi/
├── chat/                    # Conversation management app
│   ├── models.py           # SimulatedConversation model
│   ├── views.py            # API views
│   ├── serializers.py      # Data serialization
│   └── food_classifiers/   # AI classification logic
├── login/                  # Authentication app
│   ├── models.py           # User models
│   ├── views.py            # Login views
│   └── serializers.py      # Auth serializers
├── utils/                  # Utility modules
│   ├── conversation_simulator.py
│   ├── llm_interface.py
│   └── openai_client.py
├── core/                   # Django settings and configuration
│   ├── settings.py         # Project settings
│   └── urls.py            # URL routing
└── requirements.txt        # Python dependencies
```

## 🤖 How It Works

1. **Conversation Input**: The system accepts food-related conversations
2. **AI Classification**: Uses OpenAI models to analyze the conversation
3. **Food Extraction**: Extracts structured food data from the text
4. **Diet Classification**: Determines if the foods indicate vegetarian/vegan preferences
5. **Data Storage**: Stores the extracted food data from the classified conversation 

## 🧪 Testing

Run the test suite:
```bash
pytest app_directory/tests
```

## 🛠️ Development

### Code Quality
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes

### Adding New Features
1. Create models in the appropriate app
2. Add serializers for API responses
3. Create views with proper documentation
4. Update URL routing
5. Add tests for new functionality

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_SECRET` | OpenAI API key for AI classification | Yes |