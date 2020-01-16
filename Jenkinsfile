pipeline {
    agent any
    stages {
        stage('Check) {
              steps {
                  sh 'python --version'
              }
          }
        stage('Deploy') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python -m unittest'
                }
            }
        }
    }
}
