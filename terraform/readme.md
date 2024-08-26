# Installing Terraform on Photon OS using Docker Container
Step 01:
```
cd /usr/local/hesiod/terraform/
```

Step 02:
```
docker pull hashicorp/terraform
```

# Syntax for Running Terraform Modules
Each directory contains a `main.tf` file to perform the action associated with the directory. i.e. create a folder for the given description of the runtime and save the `main.tf` (and associated variables files) to the folder. 

To `init` run:
```
docker  run  -v $(pwd):$(pwd) -w $(pwd) -i -t hashicorp/terraform init
```

To `validate` run:
```
docker  run  -v $(pwd):$(pwd) -w $(pwd) -i -t hashicorp/terraform validate
```

To `plan` run:
```
docker  run  -v $(pwd):$(pwd) -w $(pwd) -i -t hashicorp/terraform plan
```

To `apply` run:
```
docker  run  -v $(pwd):$(pwd) -w $(pwd) -i -t hashicorp/terraform apply
```