pipeline {
    agent { node { label 'not-holiday-dev' } }

        stage('Build') {
            steps {

                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

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