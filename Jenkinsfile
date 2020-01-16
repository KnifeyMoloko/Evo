pipeline {
    agent { docker { image 'python' } }
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
