## Definitive Guide to Creating a SQL Database on Cloud with AWS and Python
#### An easy-to-follow comprehensive guide on integrating Amazon RDS, MySQL Workbench, and PyMySQL to build and deploy a database in the cloud for Python applications

Link to article: https://towardsdatascience.com/definitive-guide-to-create-an-sql-database-on-cloud-with-aws-and-python-c818c7270af2

___
### Contents
**Files**
- `Example-Notebook.ipynb`: Main notebook with sample codes on using PyMySQL and general Python functions to connect to Amazon RDS database instance and perform CRUD operations.
- `config.py`: Configuration file comprising key database connection parameters

**Folders**
- `/ssl`: Folder containing the bundle file of SSL certificates (for encrypted SSL connection between local client and RDS database instance)
- `/assets`: Folder containing the various screenshots in the step-by-step guide

___
### Motivation
- In the midst of building a web application for a client, I came across the need to set up a database system to store valuable user traffic data
- While each component (i.e. AWS RDS, MySQL Workbench, and PyMySQL) is easy to work with, integrating them together to form a closed-loop system proved to be relatively challenging.
- This is especially true given that online resources tend to be fragmented, with numerous important caveats and hurdles not clearly explained and illustrated.
- Having overcome these challenges to successfully set up a production database in AWS, I believe it would be important to share this information with the community, including my future self.

___
### References
- [Connect RDS - MySQL Workbench (AWS)](https://aws.amazon.com/premiumsupport/knowledge-center/connect-rds-mysql-workbench/)
- [Be A Better Dev (Youtube)](https://www.youtube.com/channel/UCraiFqWi0qSIxXxXN4IHFBQ)
- [Download SSL Certificate (AWS)](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-download-ssl-certificate-for-managed-database)
