pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python run_tests.py'
                }
            }
        }
    }
}
