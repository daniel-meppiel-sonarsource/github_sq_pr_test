pipeline {
  agent none

  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:3.8.3'
        }
      }
      steps {
        sh '''python3.8 -V # Print out python version for debugging
        python3 -m venv env
        . ./env/bin/activate
        pip install pipenv
        pipenv install --dev
        pipenv run python manage.py migrate
        pipenv run python manage.py test
        pipenv run coverage run -m pytest'''
      }
    }

    stage('QA') {
      agent {
        docker {
          image 'sonarsource/sonar-scanner-cli:latest'
        }
      }
      steps {
        echo 'Running SonarQube Analysis...'
        script {
          withSonarQubeEnv('dmeppiel_sq') {
            sh 'sonar-scanner -X -Dsonar.qualitygate.wait=true'
          }
        }
      }
    }

  }
}