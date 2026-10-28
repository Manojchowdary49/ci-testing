
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\goran\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\goran\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pytest -v --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('test-results.xml')) {
                    junit 'test-results.xml'
                } else {
                    echo 'Test report was not generated.'
                }
            }
        }
    }
}
