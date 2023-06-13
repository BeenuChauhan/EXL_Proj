import os, json, sys
import azureml.core
from azureml.core.authentication import AzureCliAuthentication
from azureml.core import Workspace
from azureml.core.runconfig import RunConfiguration

# To print the version of azureml.core
print("azureml.core SDK Version:", azureml.core.VERSION)

# To read the config.json file available in devops repo
#with open("aml_config/config.json") as f:
  #  config = json.load(f)
# Establish connection to ML workspace
workspace_name = 'MyspiritualteamProject_ML'
resource_group = 'Myspiritualteam'
subscription_id = '95eac194-52e7-4dfc-a915-c2d8f9c3fc29'
location = 'East US 2'
cli_auth = AzureCliAuthentication()

try:
    ws = Workspace.get(
        name=workspace_name,
        subscription_id=subscription_id,
        resource_group=resource_group,
        auth=cli_auth
    )

except:
    # this call might take a minute or two.
    print("Creating new workspace")
    ws = Workspace.create(
        name=workspace_name,
        subscription_id=subscription_id,
        resource_group=resource_group,
        # create_resource_group=True,
        location=location,
        auth=cli_auth

    )

# print Workspace details
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep="\n")

#Now that the Azure ML connection is configured, you can use it in your 
#pipeline steps to perform actions like deploying models, running experiments, or deploying ML pipelines
from azureml.core import Experiment

# Attach/submit Experiment
ws = Workspace.from_config(auth=cli_auth)
experiment_name = "Beenu_experiment"
exp = Experiment(workspace=ws, name=experiment_name)
print(exp.name, exp.workspace.name, sep="\n")
# to run an experiment on workspace(also editing the config)
#run = experiment.start_logging()
run_config_user_managed = RunConfiguration()
run_config_user_managed.environment.python.user_managed_dependencies = True
print("Submitting an experiment.")
src = ScriptRunConfig(
    script="train.py",
    run_config=run_config_user_managed)
run = exp.submit(src)

# Shows output of the run on stdout.
run.wait_for_completion(show_output=True, wait_post_processing=True)

# Raise exception if run fails
if run.get_status() == "Failed":
    raise Exception("Training on local failed with following run status: {} and logs: \n {}".format(run.get_status(), 
    run.get_details_with_logs()))
    

# Writing the run id to /aml_config/run_id.json
run_id = {}
run_id["run_id"] = run.id
run_id["experiment_name"] = run.experiment.name
with open("run_id.json", "w") as outfile:
    json.dump(run_id, outfile)
