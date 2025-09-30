pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Backend Dependencies') {
            steps {
                bat '''
                    cd backend
                    "C:\\Users\\masha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv flaskenv
                    flaskenv\\Scripts\\python.exe -m pip install --upgrade pip
                    flaskenv\\Scripts\\python.exe -m pip install -r requirements.txt
                    flaskenv\\Scripts\\python.exe -m pip install pyinstaller
                '''
            }
        }

        stage('Install Frontend Dependencies') {
            steps {
                bat 'cd frontend && npm install'
            }
        }

        stage('Build Frontend') {
            steps {
                bat 'cd frontend && npm run build'
            }
        }

        stage('Build Backend Executable (.exe)') {
            steps {
                bat '''
                    cd backend
                    flaskenv\\Scripts\\pyinstaller --onefile --name calculator-app app.py
                '''
                // Результат: backend/dist/calculator-app.exe
            }
        }

        stage('Test') {
            steps {
                bat '''
                    cd backend
                    flaskenv\\Scripts\\python.exe -m pytest
                '''
                bat 'cd frontend && npm test -- --passWithNoTests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to server...'
                // Например:
                // bat 'xcopy /E /Y frontend\\build \\server\\wwwroot\\'
            }
        }
    }
}