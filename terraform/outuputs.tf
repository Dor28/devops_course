output "instance_id" {
  description = "ID of EC2 instance"
  value       = aws_instance.demo.id
}

output "instance_public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_instance.demo.public_ip
}

output "website_url" {
  description = "URL to access nginx"
  value       = "http://${aws_instance.demo.public_ip}"
}
