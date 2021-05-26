```
This material is based upon work supported by the Defense Advanced
Research Project Agency (DARPA) under Contract No. HR0011-18-C-0013. 
Any opinions, findings, conclusions or recommendations expressed in
this material are those of the author(s) and do not necessarily
reflect the views of DARPA.

Distribution Statement "A" (Approved for Public Release, Distribution
Unlimited)
```

# BESSPIN FETT AWS Subnet Build

## Usage
`python build-subnets.py -r us-west-2 -n 6 -v 123546` <br/>
`-r | region` Which region to build subnets in <br/>
`-n | numUsers` Number of subnets to build <br/>
`-v | vpcId` VPC ID to attach subnets to <br/>
<br/><br/>
Running that command will pull in the CFN skeleton from empty-cloudformation.json and build a new cloudformation template called either `final-us-west-2-cloudformation.json` or `final-us-east-1-cloudformation.json`. <br/> 
Once that is finished that full cloudformation template can be ran to create the subnets.