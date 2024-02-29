pipeline {
  agent any
  stages {
    stage('Build docker') {
      steps {
        sh '''
          mkdir -p postgres_data
          docker-compose up --build -d
        '''
      }
    }
    stage('Run unitest') {
      steps {
        sh 'docker-compose run web bash -c "cd Server && python3 manage.py test"'
      }
    }
  }
}