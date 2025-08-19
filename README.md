# AI-Powered Web Platform

This project aims to build a comprehensive, scalable, and modular AI-powered web platform for content creation.

## Core Technologies (Planned)
- **Backend**: Python (FastAPI)
- **Frontend**: React.js with TailwindCSS
- **Containerization**: Docker
- **AI Models**: Hugging Face Transformers, PyTorch, TensorFlow, ONNX
- **Cloud**: Google Cloud Platform (initial focus), AWS, Azure
- **Video Processing**: FFmpeg

## Overview
This platform will provide capabilities for:
- AI-generated sound, images, and lyrics.
- Automated video editing and assembly.
- AI model management and integration.
- Cloud infrastructure for scalability.
- Social media automation and scheduling.

Further details will be added as the project progresses.

## Project Structure

- \`backend/\`: Contains the backend application code (planned: Python/FastAPI).
  - \`backend/src/ai_core/\`: Core classes for AI model and pipeline management.
- \`frontend/\`: Contains the frontend application code (planned: React/TypeScript with TailwindCSS).
  - **Note**: Setup encountered issues in the automated environment; \`npm run build\` may fail due to missing \`react-scripts\`. Manual environment setup is advised for frontend development.
- \`ai_models/\`: Intended for storing or linking to custom AI models. (Currently empty)
- \`pipelines/\`: Contains scripts and modules for specific content generation pipelines.
  - \`pipelines/sound_generation/\`: Proof-of-concept for text-to-audio generation using Hugging Face SpeechT5.
    - **Note**: Script execution (\`generate_audio_hf.py\`) failed during automated setup due to insufficient disk space for model download. Code is present but untested in the environment.
- \`scripts/\`: For utility scripts, deployment scripts, etc. (Currently empty)
- \`docs/\`: Project documentation, including architecture diagrams.
- \`tests/\`: For automated tests (unit, integration, etc.). (Currently empty)

## Getting Started

This project is in its initial setup phase. Detailed setup and execution instructions for each component (backend, frontend, pipelines) will be added as they are developed.

### Prerequisites (General):
- Git
- Python 3.9+ (for backend and some pipelines)
- Node.js & npm (for frontend)
- Docker (for containerization - planned)

### Backend:
- Navigate to \`backend/\`.
- (Further instructions to be added once a runnable backend service is established.)

### Frontend:
- Navigate to \`frontend/\`.
- Run \`npm install\` to install dependencies.
- Run \`npm start\` for development mode.
- Run \`npm run build\` to build the application.
- **Important**: As noted in Project Structure, the automated setup for the frontend faced challenges. If you encounter issues like "react-scripts not found", ensure your Node.js environment is correctly set up and try removing \`node_modules\` and \`package-lock.json\` then running \`npm install\` again.

### Pipelines:
- **Sound Generation (PoC)**:
  - Navigate to \`pipelines/sound_generation/\`.
  - See \`pipelines/sound_generation/README.md\` for instructions on running \`generate_audio_hf.py\`.
  - Be aware of potential large downloads for AI models and Python dependencies.

## Contributing
(Contribution guidelines to be added later.)

## License
(License information to be added later.)
