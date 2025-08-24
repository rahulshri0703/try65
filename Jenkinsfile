pipeline {
    agent any

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
    }
    
    
    }