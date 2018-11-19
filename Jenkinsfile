pipeline{
    agent any
    stages {
        stage('Compile'){

            parallel{
                stage('compile stage 1'){
                    steps{
                        echo "compile 1"
                    }
                }
                stage('compile stage 2'){
                    steps{
                        echo "compile 2"
                    }
                }
            }

        }
        stage('Build'){
            parallel{
                stage('build stage 1'){
                    steps{
                        echo "build 1"
                    }
                }
                stage('build stage 2'){
                    steps{
                        echo "build 2"
                    }
                }
            }

        }
    }
}