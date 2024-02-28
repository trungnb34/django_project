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
  }
}