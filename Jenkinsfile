pipeline {
    agent none

    triggers {
        githubPush()
    }

    environment {
        IMAGE_NAME = 'app'
    }

    stages {
        stage('Checkout') {
            agent { label 'docker' }
            steps {
                checkout scm
                script {
                    env.IMAGE_TAG = "${(env.BRANCH_NAME ?: 'local').replaceAll('[^A-Za-z0-9_.-]', '-')}-${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Build') {
            agent { label 'docker' }
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Test') {
            agent { label 'docker' }
            steps {
                sh '''
                    docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} sh -lc '
                        if [ -d tests ]; then
                            python -m pytest
                        else
                            echo "No tests directory found, skipping test execution."
                        fi
                    '
                '''
            }
        }

        stage('Package') {
            agent { label 'docker' }
            steps {
                sh '''
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                    docker save -o ${IMAGE_NAME}-${IMAGE_TAG}.tar ${IMAGE_NAME}:${IMAGE_TAG}
                '''
                archiveArtifacts artifacts: "${IMAGE_NAME}-${IMAGE_TAG}.tar", fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Build, test, and packaging completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the build logs for the failing stage.'
        }
        always {
            cleanWs()
        }
    }
}
