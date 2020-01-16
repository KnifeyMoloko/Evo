pipeline {
    agent { docker { image 'python:3.6-buster' } }
    stages {
        stege('Check) {
              steps {
                  sh 'python3 --version'
              }
          }
        stage('Deploy') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python3 -m unittest'
                }
            }
        }
    }
}
