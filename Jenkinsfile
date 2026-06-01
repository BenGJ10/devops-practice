pipeline {
    agent any

    environment {
        APP_NAME = 'my-flask-app'
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'

                sh '''
                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Flask App') {
            steps {
                echo "Building ${APP_NAME}..."

                sh '''
                    . venv/bin/activate

                    python --version
                    pip --version
                '''
            }
        }

        stage('Run Application Test') {
            steps {
                echo 'Testing Flask application...'

                sh '''
                    . venv/bin/activate

                    python app.py > flask.log 2>&1 &

                    sleep 10

                    curl http://127.0.0.1:5010/health
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployed successfully'
            }
        }
    }

    post {

        success {
            echo 'Pipeline executed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }

        always {
            echo 'Pipeline execution completed'
        }
    }
}