

## Install

```
cd aws
python -m venv venv
echo ". venv/bin/activate" >v
. v
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Config

- create config.yaml: `cp config.yaml_example config.yaml`
- Edit the file 'config.yaml': change the stack_name and (optionally) the other params

## CDK Installation

  - If needed, clean previous old/non-working npm/node install, bu running 
  - If needed, install node.js + npm according to the file 
  - Do: `sudo npm install -g aws-cdk`
  - Verify cdk installation: `cdk --version`
  - cd to the cdk folder: cd `aws/cdk_stack`
  - Create Python venv (if needed) and activate
  - Install CDK-specific dependencies: `pip install -r requirements.txt`
  - Init the CDK project: `cdk init app --language python`

## Deployment of the stack

   - Either delete the current stack (at the console/CloudFormation) or change the name of the stack (at config.yaml)

   - If needed, edit the CDK stack at aws/cdk_stack/stack.py
 
   - Deploy: `cd aws; ./create_and_deploy_stack`


# IMPORTANT: The file 'set_stack_env_vars', that is automatically generated, contain sensitive secret. 

## Deployment of changed Lambdas

   - Change the code under aws/lambdas
   - Set the env variables: `cd aws; . set_stack_env_vars
   - Deploy: ./update_lambdas 

## Stack Opertation Highlights

