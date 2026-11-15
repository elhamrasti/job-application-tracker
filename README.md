

# Job Application Tracker



A web application for tracking job applications, built with Python Flask and SQLite, and deployed to an Ubuntu virtual machine using Ansible.



## Project Overview



The application allows users to:



- Add job applications.

- View applications.

- Edit application details.

- Delete applications.

- Add notes.

- Track application status.



## Technologies



| Technology | Purpose |

|---|---|

| Python | Application programming |

| Flask | Web framework |

| SQLite | Database |

| Gunicorn | WSGI application server |

| Ubuntu Linux | Deployment environment |

| Ansible | Configuration management |

| Vagrant | Virtual machine management |

| VirtualBox | Virtualization |

| Git | Version control |



## Architecture



- Host machine: Windows 11

- Control node: Ubuntu on WSL2

- Virtualization: Vagrant and VirtualBox

- Managed node: Ubuntu Server virtual machine

- Application server: Gunicorn

- Application port: 5000



Ansible connects to the virtual machine over SSH and automates deployment.



## Repository Structure



```text

job-application-tracker-project/

├── app/

│   ├── app.py

│   ├── init\_db.py

│   ├── requirements.txt

│   ├── templates/

│   └── static/

├── ansible/

│   ├── inventory/

│   │   └── hosts.ini.example

│   └── playbooks/

│       ├── deploy-job-tracker.yml

│       └── install-nginx.yml

├── .gitignore

└── README.md

```



## Deployment



### Prerequisites



- Windows with WSL2 and Ubuntu

- Ansible installed in WSL2

- Vagrant

- VirtualBox

- A running Ubuntu virtual machine

- SSH access from WSL2 to the virtual machine



### 1. Configure Ansible inventory



Copy the example inventory:



```bash

cp ansible/inventory/hosts.ini.example ansible/inventory/hosts.ini

```



Edit `ansible/inventory/hosts.ini` and configure the SSH private key path for your environment.



Never upload your private SSH key to GitHub.



### 2. Check the playbook



```bash

ansible-playbook \\

&#x20; -i ansible/inventory/hosts.ini \\

&#x20; ansible/playbooks/deploy-job-tracker.yml \\

&#x20; --syntax-check

```



### 3. Deploy the application



```bash

ansible-playbook \\

&#x20; -i ansible/inventory/hosts.ini \\

&#x20; ansible/playbooks/deploy-job-tracker.yml

```



The playbook automates:



- Installing Python packages.

- Creating the application directory.

- Copying application files.

- Creating a Python virtual environment.

- Installing dependencies.

- Initializing the SQLite database if it does not exist.

- Configuring Gunicorn as a systemd service.

- Enabling and starting the application.



### 4. Access the application



If port 5000 is forwarded from the VM to the host, open:



http://127.0.0.1:5000



## Database and Data Persistence



The SQLite database is initialized automatically during the first deployment if it does not exist.



Existing database files are not copied from the development machine or overwritten by the deployment playbook.



The database is intentionally excluded from this public repository because it contains application data.



## Testing



The deployment was tested by:



- Checking Ansible playbook syntax.

- Deploying the application to an Ubuntu VM.

- Accessing the application through a web browser.

- Testing application creation, editing, deletion, and notes.

- Running the playbook again to check idempotency.

- Verifying that application data remained available after redeployment.



## Learning Outcomes



This project demonstrates practical experience with:



- Linux administration.

- Ansible playbooks and automation.

- SSH connectivity and inventory configuration.

- Python virtual environments.

- Flask application deployment.

- Gunicorn and systemd services.

- SQLite database initialization and persistence.

- Idempotent infrastructure automation.



## Notes



This is a learning and portfolio project, not a production-ready deployment.



