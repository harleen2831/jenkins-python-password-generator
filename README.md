# Jenkins-Based Password Generator

This project showcases a Jenkins pipeline that runs a customizable Python script to generate secure passwords. The pipeline is automatically triggered via GitHub webhooks and supports user-defined parameters such as password length, number of digits, and special characters.

---

## What This Project Does

- Automates the execution of a Python-based password generator  
- Accepts configurable parameters through Jenkins UI  
- Triggers builds automatically using GitHub webhooks  
- Prints the generated password and its stats in the Jenkins console output

---

## How It Works

1. Jenkins is connected to this GitHub repository using a webhook.  
2. Whenever a new commit is pushed:
   - Jenkins pulls the updated code
   - Executes the pipeline using default parameter values
   - Runs the Python script and displays the result  
3. You can also trigger the build manually and customize the parameters through the Jenkins UI.

---

##  Parameters

The pipeline supports the following parameters:

- **MIN_LENGTH**: Minimum total length of the password  
- **MIN_NUMBER_LENGTH**: Minimum number of digits (0–2)  
- **MIN_PUNC_LENGTH**: Minimum number of special characters (0–2)  

These values can be adjusted through Jenkins when triggering a manual build.

---

## How to Use

1. Push code changes to this repository  
2. Jenkins (connected via webhook) will detect the push  
3. The pipeline starts automatically and runs the Python script  
4. The generated password is printed in the Jenkins build logs  

Alternatively, use **"Build with Parameters"** in Jenkins to run it manually with custom inputs.

---

## Future Enhancements

- Make character inclusion flags (yes/no) configurable in Jenkins  
- Save the generated password as an artifact  
- Add automated tests for password validation  
- Notify users via email or Slack after password generation

---

## Why Use This?

This project is a great example of how to combine:

- Declarative Jenkins pipelines  
- GitHub integration via webhooks  
- Dynamic scripting with Python  
- Parameterized CI/CD workflows  

It’s ideal for learning Jenkins, DevOps workflows, and building internal tools that require automation.
