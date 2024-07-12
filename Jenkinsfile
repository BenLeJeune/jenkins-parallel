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
    def projects = [:]
    readCSV(file: "/tmp/MyCSV.csv").each { line ->
        def proj_name = line[0]
        projects[proj_name] = {
            stage(proj_name) {
                echo proj_name
            }
        }
    }  
    stage('Parallel') {
        parallel projects
    }
    stage('Cleanup') {
        echo 'Cleaning up after the parallel stages are done!'
    }
}