# Usage
`python test.py -r "us-west-2" -n 6 -v 124356`
`-r | region` Which region to build subnets in
`-n | numUsers` Number of subnets to build
`-v | vpcId` VPC ID to attach subnets to

Running that command will pull in the CFN skeleton from empty-cloudformation.json and build a new cloudformation template called either `final-us-west-2-cloudformation.json` or `final-us-east-1-cloudformation.json`. Once that is finished that full cloudformation template can be ran to create the subnets.