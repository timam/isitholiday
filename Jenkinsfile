pipeline {
    agent { node { label 'not-holiday-dev' } }
    stages {
        stage('Build') {
            steps {
                sh 'ifconfig'
                script {
                    // process cucumber reports
                    step([$class: 'CucumberReportPublisher', jsonReportDirectory: 'target/', fileIncludePattern: '*.json'])

                    // send report to slack
                    cucumberSendSlack: channel: 'devops', json: 'target/test-results.json'

                    timeout(time: 10, unit: 'MINUTES') {
                    input(id: "Deploy Gate", message: "Do you want to deploy ${JOB_NAME}? on ${NODE_NAME}", ok: 'Deploy')
                    }
                }
            }
        }
    }
}