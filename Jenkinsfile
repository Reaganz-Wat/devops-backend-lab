def gv

pipeline {
    agent any

    environment {
        NEW_VERSION = '1.3.0'
    }

    stages {
        stage('init') {
            steps {
                script {
                    gv = load 'script.groovy'
                }
            }
        }

        stage('build') {
            steps {
                script {
                    gv.buildApp()
                }
                echo "building version ${NEW_VERSION}"
            }
        }

        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'develop'
                }
            }

            steps {
                script {
                    gv.testApp()
                }
            }
        }

        stage('deploy') {
            steps {
                script {
                    gv.deployApp()
                }
            }
        }
    }
}