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
        pipenv run coverage run --source '.' --omit 'env/*' manage.py test
        pipenv run coverage xml'''
        stash includes: 'coverage.xml', name: 'COVERAGE_REPORT'
      }
    }

    stage('QA analysis') {
      agent {
        docker {
          image 'sonarsource/sonar-scanner-cli:latest'
          args """
          -e JENKINS_HOME="${JENKINS_HOME}"
          """
        }
      }
      steps {
        echo 'Running SonarQube Analysis...'
        script {
          withSonarQubeEnv('dmeppiel_sq') {
            unstash 'COVERAGE_REPORT'
            sh 'printenv'
            sh "sonar-scanner -X -Dsonar.qualitygate.wait=true"
          }
        }
      }
    }
  }
}