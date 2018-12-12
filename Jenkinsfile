pipeline {
    agent { node { label 'not-holiday-dev' } }
    stages {
        stage('Build') {
            steps {
                sh 'ifconfig'
                script {
                    timeout(time: 10, unit: 'MINUTES') {
                    input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
                    }
                }
            }
        }
    }
}
