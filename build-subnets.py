import json
import sys
import getopt
def main(argv):
  try:
    opts, args = getopt.getopt(argv,"r:n:",["region=", "numUsers="])
  except getopt.GetoptError:
    print('test.py -r <region>')
    sys.exit(2)
  for opt, arg in opts:
    if opt not in ("-r", "--region", "-n", "--numUsers",  "-v", "--vpcId"):
      print('Usage: test.py -r us-west-2 -n 100')
      raise Exception('Unknown parameter')
      sys.exit(2)
    if opt in ("-r", "--region"):
      region = arg
      cloudformation_output_file = "final-"+region+"-cloudformation.json"
    if opt in ("-n", "--numUsers"):
      number_of_users = arg
    if opt in ("-v", "--vpcId"):
      vpc_id = arg      
  if(vpc_id == "" or number_of_users == "" or region == ""):
    print('Usage: test.py -r us-west-2 -n 100 -v 23894723')
    raise Exception('-r and -n and -v parameters are required')
    sys.exit(2)
  # Read cloudfomration template into dict
  with open('empty-cloudformation.json', "r") as cf:
    cf_tempalte = json.load(cf)
  # Clear output file first
  open(cloudformation_output_file, 'w').close()
  with open(cloudformation_output_file, "a") as file:
    i = 1
    east_count = 0
    west_count = 0
    while i <= int(number_of_users):
      if region == 'us-east-1':
        cidrBlock = "10.0.1."+str(east_count * 8)+"/24",
        east_count += 1
      else:
        cidrBlock = "10.0.0."+str(west_count * 8)+"/24",
        west_count += 1

      cf_tempalte["Resources"].update({
        "userSubnet-"+str(i): {
          "Type" : "AWS::EC2::Subnet",
          "Properties" : {
            "VpcId" : vpc_id,
            "CidrBlock" : cidrBlock
          }
        }
      })
      i+=1
    file.write(json.dumps(cf_tempalte, indent=2).encode('utf-8'))
if __name__ == "__main__":
   main(sys.argv[1:])    