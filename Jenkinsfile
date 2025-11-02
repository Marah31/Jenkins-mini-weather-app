pipeline {
  agent {
    docker {
      image 'python:3.10-slim'  
      args '-u root:root'       
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }
    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest test_app.py --junitxml=reports/test-results.xml
        '''
      }
    }
    stage('Run App') {
      steps {
        sh '''
          . venv/bin/activate
          timeout 60s python3 app.py || echo "App stopped after timeout."
        '''
      }
    }
  }

  post {
    success { echo 'Pipeline succeeded!' }
    failure { echo 'Pipeline failed.' }
  }
}
