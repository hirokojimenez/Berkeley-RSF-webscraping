# UC Berkeley RSF Gym Density Analysis Tool

## Technical Overview
This Python application is designed to automate the collection of gym occupancy data from the UC Berkeley Recreational Sports Facility (RSF). It utilizes BeautifulSoup for web scraping and Selenium WebDriver for browser automation. Deployed on an AWS EC2 instance, it facilitates continuous long-term data gathering, allowing for the analysis of gym usage patterns.

## Project Objective
The aim is to provide UC Berkeley students with a data-driven method to identify less crowded times for gym visits, especially during peak periods like the New Year.

## Core Functionality
- **Data Scraping**: Implemented using BeautifulSoup to parse HTML and extract occupancy data.
- **Browser Automation**: Selenium WebDriver is used to automate web interactions.
- **Data Recording**: Occupancy data is captured at regular intervals and stored in CSV format.
- **Cloud Automation**: Continuous operation on AWS EC2 ensures uninterrupted data collection.

## Technical Limitations and Ethical Considerations
- Accuracy is dependent on the RSF website's data.
- Tailored for the UC Berkeley RSF, modifications needed for other sites.
- Adhere to web scraping and data usage guidelines as per the website's terms of service.

## Contributions
Contributions for improvements or adaptations are welcome. Feel free to suggest enhancements, fork the project, or submit pull requests.

## Contact Information
hiroko_yamaguchi@berkeley.edu
