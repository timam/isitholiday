pipeline {
    agent { node { label 'not-holiday-dev' } }

    stage('NotifySlack') {
        steps {
        cucumberSlackSend 'devops'
        slackSend(message: 'waiting for build ', baseUrl: 'www.abc.com', channel: 'devops')
    }

    stages {
        stage('Build') {
            steps {
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