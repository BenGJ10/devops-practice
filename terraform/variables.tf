variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "The EC2 instance type to use for the web server"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "The ID of the Amazon Machine Image (AMI) to use for the EC2 instance"
  type        = string
  default     = "ami-0c94855ba95c71c99" # Amazon Linux 2 AMI (HVM), SSD Volume Type
}

variable "instance_name" {
  description = "The name tag to assign to the EC2 instance"
  type        = string
  default     = "MyWebServer"
}

variable "key_pair_name" {
  description = "The name of the existing AWS key pair to use for SSH access"
  type        = string
  default     = "my-key-pair"
}