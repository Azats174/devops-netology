output "instance_ip_addr" {
     value       = aws_instance.web.private_ip 
     description = "The private ip addr"
      
     }
