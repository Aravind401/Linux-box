terraform {
  required_version = ">= 1.0"
}

resource "null_resource" "uninstall_github_cli" {
  provisioner "local-exec" {
    command = <<EOT
      sudo apt remove gh -y
      sudo apt purge gh -y
      sudo apt autoremove -y
      rm -rf ~/.config/gh ~/.cache/gh ~/.local/share/gh
    EOT
  }
}

