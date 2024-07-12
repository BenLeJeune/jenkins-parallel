node {
    stage('Checkout SCM') {
        checkout scm
    }
    stage('Setup Virtual Environment') {
        sh '''
            python3 -m venv venv
            source venv/bin/activate
            pip install -r requirements.txt
        '''
    }
    stage('Start') {
        echo 'Running the startup Python script'
        sh '''
            source venv/bin/activate
            python3 start.py
        '''
    }
    stage('Parallel') {
        parallel(
            stage1: {
                stage('First parallel stage') {
                    echo 'Stage 1 here!'
                }
            },
            stage2: {
                stage('Second parallel stage') {
                    echo 'Stage 2 here!'
                }
            }
        )
    }
    stage('Cleanup') {
        echo 'Cleaning up after the parallel stages are done!'
    }
}