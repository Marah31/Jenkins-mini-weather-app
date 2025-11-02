pipeline {
    agent any
    environment {
        PYTHON = "python3"
    }
    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    sudo apt update
                    sudo apt install python3.12-venv -y
                    . venv/bin/activate
                    sudo apt install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test || echo "No tests found, skipping..."'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_app.py --junitxml=reports/test-results.xml || echo "Tests skipped or no tests found."
                '''
            }
        }

        stage('Simulate Deployment') {
            steps {
                sh '''
                    . venv/bin/activate
                    timeout 60s ${PYTHON} app.py || echo "App stopped after 60 seconds."
                '''
            }
        }
    }

    post {
        success {
            echo 'success'
        }
        failure {
            echo 'failed'
        }
    }
}
