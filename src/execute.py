def execute(inputs):
    context = inputs.get("context")
    team_name = context.get("teamName")
    activity_id = context.get("incidentId")

    #Get activity slack format
    try:    
        activity_defaults = api.run('transposit_mc_api.get_activity_defaults', {
            "team": team_name
        })[0]
    except ValueError as ex:
        workflow.log.fail(f"Error getting activity defaults:\n{str(ex)}")
        
    channel_name = activity_defaults.get("prettyIdPlaceholder")
    channel_name = channel_name.replace("[activity number]", str(activity_id))
    
    # Output action results/data
    custom_output_params = {"channel_name": channel_name}
    return workflow.log.done(f"Templated channel name is: {channel_name}", {}, custom_output_params)

# For sample code and reference material, visit
# https://www.transposit.com/docs/references/python-operations
