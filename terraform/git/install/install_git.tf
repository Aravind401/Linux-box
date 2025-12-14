terraform {
  required_version = ">= 1.0"
}

resource "null_resource" "install_git" {

  provisioner "local-exec" {
    command = <<EOT
      sudo apt update
      sudo apt install git -y
    EOT
  }

  # Prevents re-running on every apply
  triggers = {
    git_version = "install"
  }
}

