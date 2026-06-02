pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('remove existing containers and images') {
            steps{
                sh 'docker rm -f app-container || true'
                sh 'docker rmi app-image || true'
            }
        }
        
        stage('build image'){
            steps{
                sh "docker build -t app-image ."
            }
        }
        
        stage('run container'){
            steps{
                sh "docker run -d --name app-container -p 5000:5000 app-image"
            }
        }
    }
}