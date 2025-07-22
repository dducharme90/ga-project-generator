# Comprehensive Educational Project Generator

## Overview

This is a Streamlit-based web application that generates comprehensive educational project packages with accessibility modifications and formal lesson plans. The system integrates educational standards from all 50 states across multiple content areas (Mathematics, English Language Arts, Social Studies, and Science) and uses AI to create detailed, standards-aligned educational content with built-in accessibility support.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Frontend**: Streamlit web interface for user interaction
- **Standards Database**: Comprehensive educational standards repository
- **AI Content Generation**: OpenRouter API integration for generating educational content
- **Accessibility Framework**: Built-in special education modifications and accommodations

## Key Components

### 1. Web Interface (`app.py`)
- **Purpose**: Main Streamlit application providing the user interface
- **Features**: Multi-column layout, state management, interactive form controls
- **Architecture Decision**: Streamlit was chosen for rapid prototyping and ease of deployment, providing immediate web interface without complex frontend framework setup

### 2. Standards Database (`standards_database.py`)
- **Purpose**: Centralized repository of educational standards across all 50 states
- **Structure**: Hierarchical dictionary structure (State → Content Area → Grade → Standard → Sub-standards)
- **Coverage**: Mathematics, English Language Arts, Social Studies, and Science
- **Architecture Decision**: In-memory dictionary structure chosen for fast lookups and simple data management, avoiding database complexity for this prototype phase

### 3. Project Generator (`project_generator.py`)
- **Purpose**: AI-powered content generation using OpenRouter API
- **Integration**: Constructs detailed prompts and handles API communication
- **Architecture Decision**: OpenRouter chosen for access to multiple AI models with a single API, providing flexibility and cost-effectiveness

### 4. Accessibility Framework (`accessibility_modifications.py`)
- **Purpose**: Comprehensive special education support and accommodations
- **Categories**: 10 major accommodation types including IEP modifications, 504 plans, ELL support, etc.
- **Architecture Decision**: Separate module for accessibility ensures inclusive design principles are integrated throughout the application

## Data Flow

1. **User Input Collection**: User selects state, content area, grade level, and specific standards through the Streamlit interface
2. **Standards Lookup**: System retrieves relevant standards and sub-standards from the hierarchical database
3. **Configuration Assembly**: User selections are packaged into a configuration object
4. **AI Prompt Construction**: Detailed educational prompt is built incorporating standards, accessibility needs, and project requirements
5. **Content Generation**: OpenRouter API processes the prompt and returns comprehensive educational content
6. **Content Delivery**: Generated project package is displayed to the user through the Streamlit interface

## External Dependencies

### Core Dependencies
- **Streamlit**: Web application framework for the user interface
- **Requests**: HTTP library for API communication with OpenRouter

### API Integration
- **OpenRouter API**: AI content generation service
  - API Key: Stored as environment variable with fallback
  - Endpoint: `https://openrouter.ai/api/v1/chat/completions`
  - Purpose: Generate comprehensive educational content

## Deployment Strategy

### Environment Configuration
- **API Key Management**: OpenRouter API key stored as environment variable (`OPENROUTER_API_KEY`)
- **Session State**: Streamlit session state used for maintaining standards data across user interactions
- **Page Configuration**: Wide layout configured for optimal user experience

### Scalability Considerations
- **Standards Database**: Currently in-memory structure suitable for current scale; can be migrated to external database as needed
- **API Rate Limiting**: Single API provider used; can be extended to multiple providers for redundancy
- **State Management**: Session-based storage appropriate for single-user sessions

### Security Features
- **API Key Protection**: Environment variable usage prevents hardcoded credentials
- **Input Validation**: Standards selection constrained to predefined options
- **Error Handling**: API failure handling to prevent application crashes

## Recent Changes: Latest modifications with dates

### January 22, 2025
- **Major Standards Database Correction**: Updated Georgia science standards to match official Georgia Standards of Excellence
  - **6th Grade**: Changed to S6E1-S6E4 (Universe, Earth-Moon-Sun, Water, Climate/Weather) with accurate sub-elements
  - **7th Grade**: Updated to S7L1-S7L5 (Biodiversity, Cells, Genetics, Ecology, Evolution) with proper life science focus
  - **8th Grade**: Corrected to S8P1-S8P5 (Matter, Energy, Force/Motion, Waves, Gravity/Electricity/Magnetism) with accurate physical science elements
- **Virtual Environment Fix**: Enhanced project generation to properly distinguish between virtual and brick-and-mortar learning environments
- **State Simplification**: Removed all states except Georgia to focus on comprehensive, accurate standards coverage

The application is designed as a comprehensive educational tool that prioritizes accessibility and standards alignment while maintaining simplicity in deployment and usage. The modular architecture allows for easy extension of features and integration of additional educational standards or accessibility modifications as needed.