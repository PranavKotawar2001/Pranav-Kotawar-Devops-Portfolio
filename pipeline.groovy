pipeline{
    agent any
    stages{
       stage('Pull'){
            steps{
                git branch: 'master',
                url: 'https://github.com/PranavKotawar2001/Pranav-Kotawar-Devops-Portfolio.git'
            }
        }

        // stage('Test') {
        //     steps {
        //         withSonarQubeEnv(installationName: 'Sonar', credentialsId: 'Sonar-secret') {
        //             sh '''
        //                 sonar-scanner \
        //                 -Dsonar.projectKey=python-app \
        //                 -Dsonar.sources=. \
        //                 -Dsonar.python.version=3
        //             '''
        //         }
        //     }
        // }

         stage('Docker-Image-Build'){
            steps{
                sh '''docker build -t pranavkotawar2001/pranav-potfolio:tagname .'''   
            }
        }

        stage('Push-Image-to-Docker-Hub'){
            steps{
                sh '''
                   docker push pranavkotawar2001/pranav-potfolio:tagname
                   docker rmi pranavkotawar2001/pranav-potfolio:tagname''' 
            }
        }
         
        stage('Deploy'){
            steps{
                sh '''
                kubectl apply -f kubernetes/'''  
            }
        }
    }
}