pipeline {
    agent any
    stages {
        stege('Check) {
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
