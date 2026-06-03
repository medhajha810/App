pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t app:latest .'
            }
        }

        stage('Test') {
            steps {
                script {
                    if (fileExists('tests')) {
                        sh 'docker run --rm app:latest sh -c "pytest -q"'
                    } else {
                        echo 'No tests found, skipping.'
                    }
                }
            }
        }

        stage('Package') {
            steps {
                sh 'docker save -o app.tar app:latest'
                archiveArtifacts artifacts: 'app.tar'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
