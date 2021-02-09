// Looking for component and it's version in SSM parameter store

def call(Map params = [:]) {
    // Variables definition
    // def awsCredentials  = params.get('awsCredentials')
    // def awsRegion    = params.get('SSMRegion', 'us-east-1')
    // def componentName   = params.get('componentName')
    // def componentsVersion = params.get('componentsVersion')
    def prefix = params.get("${env.AWS_REGION}/${env.AGO_PRODUCT}/${env.AGO_SERVICE}/${env.COMPONENT}/${env.VERSION}")

    try {
        println "Looking for SSM parameter with ${prefix} in ${env.AWS_REGION}"
        def prefix = sh returnStdout : true,
            script: """aws ssm get-parameters \
                --names ${prefix} \
                --query 'Parameters[*].[Name]' \
                --output text
            """

        if (prefix == 'null' && env.VERSION != 'Latest')) {
            println "Creating parameter of ${prefix} with value of ${env.COMPONENT} in ${env.AWS_REGION}"
            sh """aws ssm put-parameter \
                --name ${prefix} \
                --type "String" \
                --value ${env.VERSION} \
                --region ${env.AWS_REGION}                """
            } else 

        if (prefix != 'null' && env.VERSION != 'Latest') {
            println "Updating version of ${prefix} in ${env.AWS_REGION}"
                sh """aws ssm put-parameter \
                --name ${prefix} \
                --type "String" \
                --value ${env.VERSION} \
                --overwrite \
                --region ${env.AWS_REGION}
            """
        } else 

        if (prefix != 'null' && env.VERSION == 'Latest') {
            println "Fetching version of ${prefix} in ${env.AWS_REGION}"
            def env.VERSION = sh returnStdout : true,
            script: """aws ssm get-parameters \
                --names ${prefix} \
                --query 'Parameters[*].[Value]' \
                --output text
            """
        } else {
            error "You are trying to get latest version of unexisting parameter. Check ${env.COMPONENT} version."
        }
    } catch (e) {
        throw e
    }
}