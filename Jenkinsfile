pipeline {
  agent {
    docker {
      image 'python:3.8.3'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''python3.8 -V # Print out python version for debugging
        pip install --user pipenv
        pipenv install --dev
        pipenv run python manage.py migrate
        pipenv run python manage.py test
        pipenv run coverage run -m pytest'''
      }
    }

    stage('QA') {
      steps {
        sh 'sonar-scanner -Dsonar.qualitygate.wait=true'
      }
    }

  }
}