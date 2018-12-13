pipeline {
    agent { node { label 'not-holiday-dev' } }

    stages {
        stage('Build') {
            steps {
                slackSend (color: '#FFFF00', message: "Job '${env.JOB_NAME}' is waiting for approval to deploy. Please visit (${env.BUILD_URL}) to approve")

                sh 'ifconfig'
                script {
                    timeout(time: 10, unit: 'MINUTES') {
                    input(id: "Deploy Gate", message: "Do you want to deploy ${JOB_NAME}? on ${NODE_NAME}", ok: 'Deploy')
                    }
                }
            }
        }

    }
}
