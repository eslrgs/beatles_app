resource "aws_instance" "app_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "your-key-name"

  security_groups = ["${aws_security_group.flask_sg.name}"]

  user_data = <<-EOF
                #!/bin/bash
                sudo apt update
                sudo apt install -y python3-pip
                pip3 install -r requirements.txt
                FLASK_APP=app.py flask run --host=0.0.0.0
                EOF

  tags = {
    Name = "beatles_app"
  }
}
