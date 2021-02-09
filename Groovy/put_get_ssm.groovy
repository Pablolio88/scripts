// Looking for component and it's version in SSM parameter store

def call(Map params = [:]) {
    def prefix = params.get("${env.AWS_REGION}/${env.AGO_PRODUCT}/${env.AGO_SERVICE}")
    def output_map = [:]
    for (entry in params) {
        def prefix = params.get("${prefix}/${entry.key}/${entry.value}")
        try {
            println "Looking for SSM parameter with ${prefix} in ${env.AWS_REGION}"
            def parameter_name = sh returnStdout : true,
                script: """aws ssm get-parameters \
                    --names ${prefix} \
                    --query 'Parameters[*].[Name]' \
                    --output text
                """

            if (prefix == 'null' && entry.value != 'Current')) {
                println "Creating parameter of ${prefix} with value of ${entry.value} in ${env.AWS_REGION}"
                sh """aws ssm put-parameter \
                    --name ${prefix} \
                    --type "String" \
                    --value ${entry.value} \
                    --region ${env.AWS_REGION}
                """
                output_map.put("${prefix}", "${entry.value}")
                } else 

            if (prefix != 'null' && entry.value != 'Current') {
                println "Updating version of ${prefix} in ${env.AWS_REGION}"
                    sh """aws ssm put-parameter \
                    --name ${prefix} \
                    --type "String" \
                    --value ${entry.value} \
                    --overwrite \
                    --region ${env.AWS_REGION}
                """
                output_map.put("${prefix}", "${entry.value}")
            } else 

            if (prefix != 'null' && entry.key == 'Current') {
                println "Fetching version of ${prefix} in ${env.AWS_REGION}"
                def parameter_value = sh returnStdout : true,
                script: """aws ssm get-parameters \
                    --names ${prefix} \
                    --query 'Parameters[*].[Value]' \
                    --output text
                """
                output_map.put(parameter_name, parameter_value)
            } else {
                error "You are trying to get Current version of unexisting parameter. Check ${entry.key} version."
            }
        } catch (e) {
            throw e
        }
    }
    return output_map
}
