pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t blog:v1 .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name blog-container -p 8000:8000 blog:v1'
            }
        }

    }
}