pipeline {
    agent any  // Run on any available agent

    environment {
        // Add environment variables here if needed
        PYTHON_PATH = 'C:/Users/acer/AppData/Local/Programs/Python/Python313/python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up environment...'
                // Optional: install Python dependencies
                bat '"%PYTHON_PATH%" -m pip install --upgrade pip'
                bat '"%PYTHON_PATH%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Running main.py...'
                // Run your Python script
                bat '"%PYTHON_PATH%" main.py'
            }
        }

        stage('Tests') {
            steps {
                echo 'Running tests...'
                // If you have tests, you can run them here
                // Example: bat '"%PYTHON_PATH%" -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps if any (e.g., copy files, Docker build, etc.)
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
