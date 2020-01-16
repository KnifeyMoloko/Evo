pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh 'for n in `seq 1 10`; do echo $n; sleep 1; done'
                }
                timeout(time: 3, unit: 'MINUTES') {
                    sh 'python3 -m unittest'
                }
            }
        }
    }
}
