pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python3 -m unittest'
                }
            }
        }
    }
}
