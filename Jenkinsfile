pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    sh 'add-apt-repository ppa:deadsnakes/ppa'
                    sh 'apt update'
                    sh 'apt install python3.7'
                }
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python3 -m unittest'
                }
            }
        }
    }
}
