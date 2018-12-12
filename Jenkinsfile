pipeline {
    agent { node { label 'not-holiday-dev' } }
    stages {
        stage('Build') {
            steps {
                sh 'ifconfig'
                script {
                    timeout(time: 10, unit: 'MINUTES') {
                    input(id: "Deploy Gate", message: "Do you want to deploy ${JOB_NAME}?", ok: 'Deploy')
                    }
                }
            }
        }
    }
}