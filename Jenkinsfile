pipeline {
    agent any

    environment {
        // Укажите ваш GitHub токен для push в main (создайте его в GitHub → Settings → Developer settings → Personal Access Token)
        GITHUB_TOKEN = credentials('github-token')  // Имя учётной записи в Jenkins
    }

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

        stage('Auto-Merge to main (if not on main already)') {
            when {
                not { branch 'main' }  // Выполняется только НЕ в ветке main
            }
            steps {
                script {
                    // Получаем имя текущей ветки
                    def currentBranch = env.GIT_BRANCH.replace('origin/', '')
                    echo "Текущая ветка: ${currentBranch}"

                    // Настройка Git
                    bat '''
                        git config --global user.email "masha.gruzdeva@ya.ru"
                        git config --global user.name "mariia"
                    '''

                    // Мержим в main
                    bat """
                        git checkout main
                        git pull origin main
                        git merge origin/${currentBranch} --no-ff -m "Merge ${currentBranch} into main [auto]"
                        git push https://${GITHUB_TOKEN}@github.com/Gruzdo4ek/devOps.git main
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '✅ Сборка и тесты пройдены. Приложение готово к деплою.'
                echo 'Backend executable: backend/dist/calculator-app.exe'
                echo 'Frontend build: frontend/build/'
                // Здесь можно добавить копирование на сервер, архивацию и т.д.
            }
        }
    }
}