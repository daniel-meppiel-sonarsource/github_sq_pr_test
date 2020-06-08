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
      steps {
        echo 'Running SonarQube Analysis...'
        script {
          def scannerHome = tool 'SQ Scanner Latest';
          withSonarQubeEnv('dmeppiel_sq') {
            sh '${scannerHome}/bin/sonar-scanner -Dsonar.qualitygate.wait=true'
          }
        }
      }
    }

  }
}