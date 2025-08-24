pipeline {
    agent any

        environment {
    docker_cred = credentials('dockerCred')
        }

    stages {
        stage('fetch_code') {
            steps{
                git branch : 'Main',url : "https://github.com/rahulshri0703/try65.git"
            }

             post {
            success {
                echo "pulled succesful"
                archiveArtifacts  artifacts: "**/*.py"    
                archiveArtifacts  artifacts: "**/*.csv"
                // archiveArtifacts  artifacts: "**/*.pkl"
            }
        }
    }


     stage('install_requirements') {
            
            steps {
                sh 'ls'
               
            }
}


   stage("docker-login3") {
            steps {
              withCredentials([[$class: 'UsernamePasswordMultiBinding', 
                                credentialsId: 'dockerCred',
                                 usernameVariable: 'DOCKER_REGISTRY_USER',
                                  passwordVariable: 'DOCKER_REGISTRY_PWD']]) 
              {
                sh "echo ${DOCKER_REGISTRY_PWD} | docker login -u ${DOCKER_REGISTRY_USER} --password-stdin"
                sh "echo success34567"

             }
        }
        }
    }
    
    
    }