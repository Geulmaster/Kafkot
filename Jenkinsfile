node (label: 'laptop') {
    stage ('clone') {
        sh "git clone git@github.com:Geulmaster/Kafkot.git"
    }
    stage ('build & run') {
        steps: {
            sh "pwd"
            sh "cd Kafkot && docker-compose up -d"
        }
    }
    stage ('clean up') {
        sh "rm -rf Kafkot"
    }
}