resource "aws_instance" "ec2_demo"{
    ami           = var.ami_id
    instance_type = var.instance_type
    key_name      = var.key_pair_name
    
    tags = {
        Name = var.instance_name
    }
}