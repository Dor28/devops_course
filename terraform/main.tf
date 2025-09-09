terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure AWS Provider
provider "aws" {
  region = var.aws_region
}


data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_security_group" "demo" {
  name        = "${var.project_name}-sg"
  description = "Security group for demo EC2 instance"

  # Allow HTTP
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-sg"
  }
}


resource "aws_instance" "demo" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  
  # Attach security group
  vpc_security_group_ids = [aws_security_group.demo.id]
  
  # Install nginx on startup
  user_data = <<-EOF
    #!/bin/bash
    amazon-linux-extras install nginx1 -y
    echo "<h1>Terraform Demo - AWS</h1>" > /usr/share/nginx/html/index.html
    echo "<p>Instance: ${var.project_name}</p>" >> /usr/share/nginx/html/index.html
    echo "<p>Region: ${var.aws_region}</p>" >> /usr/share/nginx/html/index.html
    systemctl start nginx
  EOF
  
  tags = {
    Name = "${var.project_name}-instance"
  }
}

