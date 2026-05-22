pipeline{
    agent any
    stages{
        stage('Pull'){
            steps{
                git 'https://github.com/PranavKotawar2001/Pranav-Kotawar-Devops-Portfolio.git'
            }
        }

        stage('Test') {
            steps {
                withSonarQubeEnv(installationName: 'Sonar', credentialsId: 'Sonar-secret') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=python-app \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3
                    '''
                }
            }
        }

         stage('Docker-Image-Build'){
            steps{
                sh '''docker build -t pranavsudhirkotawar/backend:latest .'''   
            }
        }
        
        stage('Push-Image-to-Docker-Hub'){
            steps{
                sh '''
                   docker push pranavsudhirkotawar/backend:latest
                   docker rmi pranavsudhirkotawar/backend:latest''' 
            }
        }
         
        stage('Deploy'){
            steps{
                sh '''
                kubectl apply -f k8s/'''  
            }
        }
    }
}