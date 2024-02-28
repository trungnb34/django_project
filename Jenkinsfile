pipeline {
  agent any
  stages {
    stage('Checkout branch') {
      steps {
        git(url: 'https://github.com/trungnb34/django_project', branch: 'dev')
      }
    }

    stage('build docker') {
      steps {
        sh 'python -m pip install -r requirements.txt'
      }
    }

  }
}