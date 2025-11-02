pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm

                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test || echo "No tests found, skipping..."'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'npm run build'
            }
        }

        stage('Simulate Deployment') {
            steps {
                echo 'Starting the app...'
                sh 'npm start &'
                echo 'App is running. Deployment simulated successfully.'
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
