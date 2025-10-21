pipeline {
    agent any

    environment {
        REGISTRY = "localhost:5001"
        BACKEND_IMAGE = "${REGISTRY}/calculator-backend:latest"
        FRONTEND_IMAGE = "${REGISTRY}/calculator-frontend:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Frontend (React)') {
            steps {
                bat 'cd frontend && npm install && npm run build'
            }
        }

        stage('Build and Push Backend Image') {
            steps {
                script {
                    bat """
                        cd backend
                        docker build -t ${BACKEND_IMAGE} .
                        docker push ${BACKEND_IMAGE}
                    """
                }
            }
        }

        stage('Build and Push Frontend Image') {
            steps {
                script {
                    bat """
                        cd frontend
                        docker build -t ${FRONTEND_IMAGE} .
                        docker push ${FRONTEND_IMAGE}
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                bat '''
                    docker-compose down --remove-orphans
                    docker-compose up -d
                '''
                echo '✅ Приложение запущено! Доступно по http://localhost'
            }
        }

        stage('Smoke Test') {
            steps {
                bat 'curl -f http://localhost:5000/ || exit 1'
                bat 'curl -f http://localhost/ | findstr "Sum Calculator" || exit 1'
                echo '✅ Smoke-тесты пройдены'
            }
        }
    }
}