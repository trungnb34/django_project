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
  post {
        success {
            // Send email if the build succeeds
            emailext (
                to: 'zimmi123cook@gmail.com',
                subject: 'Build Success Notification',
                body: 'The build has succeeded.'
            )
        }
        failure {
            // Send email if the build fails
            emailext (
                to: 'zimmi123cook@gmail.com',
                subject: 'Build Failure Notification',
                body: 'The build has failed. Please check the Jenkins logs for details.'
            )
        }
    }
}