# RevShell
TryHackMe !  Vulnversity 

# Purpose 
 This Automates testing which file extensions a web upload endpoint accepts. It repeatedly renames a base file (revshell) to different PHP-related extensions and sends each file to the target upload endpoint. The script prints whether the server response suggests that a particular extension is allowed or rejected.

 # Quick Summary Of Behavior 
1. The script builds a target URL using the target machine IP and a fixed port/path.
2. It iterates a list of candidate file extensions (PHP variants).
3. For each extension it renames the local file to that extension, uploads it with an HTTP POST (multipart/form-data), and checks the server response for the string "Extension not allowed".
4. It prints whether each extension appears to be allowed or not.
