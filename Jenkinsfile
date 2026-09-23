pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                checkout scm 
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 
                    call venv\\Scripts\\activate
                    pytest -v test_app.py
                
            }
        }
    }
}

