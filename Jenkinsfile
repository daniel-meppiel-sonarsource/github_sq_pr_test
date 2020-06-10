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
        pipenv run coverage run xml'''
      }
    }

    stage('QA branch analysis') {
      agent {
        docker {
          image 'sonarsource/sonar-scanner-cli:latest'
        }
      }
      when {
        not {
          changeRequest()
        }
      }
      steps {
        echo 'Running SonarQube Branch Analysis...'
        script {
          withSonarQubeEnv('dmeppiel_sq') {
            sh "sonar-scanner -X -Dsonar.qualitygate.wait=true \
                        -Dsonar.branch.name=${env.BRANCH_NAME}"
          }
        }
      }
    }

    stage('QA PR analysis') {
      agent {
        docker {
          image 'sonarsource/sonar-scanner-cli:latest'
        }
      }
      when {
          changeRequest()
      }
      steps {
        echo 'Running SonarQube PR Analysis...'
        script {
          withSonarQubeEnv('dmeppiel_sq') {
            sh "sonar-scanner -X \
                -Dsonar.pullrequest.key=${env.CHANGE_ID} \
                -Dsonar.pullrequest.base=${env.CHANGE_TARGET} \
                -Dsonar.pullrequest.branch=${env.CHANGE_BRANCH}"
          }
        }
      }
    }

  }
}