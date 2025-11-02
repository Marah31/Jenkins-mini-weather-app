pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                if [ -f test_app.py ]; then
                    echo "Running tests..."
                    python3 -m unittest discover -s . -p "test_*.py"
                else
                    echo "No tests found, skipping..."
                fi
                '''
            }
        }

        stage('Simulate Deployment') {
            steps {
                sh 'nohup python3 app.py &'
                echo 'App is running. Deployment simulated successfully.'
            }
        }
    }

    post {
        success {
            echo 'Success'
        }
        failure {
            echo 'Failed'
        }
    }
}
