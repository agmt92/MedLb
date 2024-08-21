# MedLeb: Medication and Pharmacy Database

MedLeb, a comprehensive web application built using Django, designed to provide extensive search capabilities for medications and pharmacies. It also includes features for user authentication, data visualization, and user feedback.

Visit the live website: [MedLeb](https://agmt92.pythonanywhere.com)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Contributing](#contributing)

## Project Overview

This project is part of the DJ4E (Django for Everybody) curriculum by Dr. Chuck Severance. It includes several functionalities such as user authentication, medication and pharmacy search, data visualization, and user feedback.

## Features

- **User Authentication**: Create an account, log in, and log in with GitHub.
- **Medication Search**: Search the medication database by various parameters. Logged-in users can favorite/unfavorite medications.
- **Pharmacy Search**: Search the extensive pharmacy and pharmacist database, get phone numbers, and view exact or approximate locations.
- **Data Visualization**: Visualize medication data using D3.js.
- **User Feedback**: Authorized users can report missing drugs, mistakes, or leave feedback.
- **Data Scraping and Cleaning**: Custom Python scripts to scrape, clean, and inject data into the database.

## Technologies Used

- **Django**: Web framework for building the application.
- **D3.js**: For data visualization.
- **MySQL**: Database management system.
- **Python**: For backend development and data processing.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For client-side scripting.
- **Bootstrap**: For responsive design.
- **FuzzyWuzzy**: For string matching and data cleaning.
- **Pandas**: For data manipulation and analysis.
- **SQLAlchemy**: For database interaction in data processing scripts.


## Project Structure

```
medleb/
│
├── accounts/                # User authentication and account management
├── ads/                     # Advertisement management
├── autos/                   # Auto-related functionalities (from taught projects)
├── cats/                    # Cat-related functionalities (from taught projects)
├── hello/                   # Basic app for greetings (from taught projects)
├── home/                    # Home page and static content
├── meds/                    # Medication database and search functionality
├── mysite/                  # Main project settings and URLs
├── pharma/                  # Pharmacy database and search functionality
├── polls/                   # Polls app (from taught projects)
├── scripts/                 # Custom scripts for data scraping and cleaning
├── site/                    # Site-specific settings and configurations
├── visual/                  # Data visualization with D3.js
├── .gitignore               # Git ignore file
├── manage.py                # Django management script
└── README.md                # Project documentation
```

## Database Models

### Meds App

- **Medication**: Stores information about medications.
  - `name`: CharField, name of the medication.
  - `description`: TextField, description of the medication.
  - `category`: CharField, category of the medication.
  - `price`: DecimalField, price of the medication.
  - `availability`: BooleanField, availability status.

### Pharma App

- **Pharmacy**: Stores information about pharmacies.
  - `name`: CharField, name of the pharmacy.
  - `address`: CharField, address of the pharmacy.
  - `phone_number`: CharField, phone number of the pharmacy.
  - `location`: PointField, geographical location of the pharmacy.
  - `approximate_location`: BooleanField, whether the location is approximate.

- **Pharmacist**: Stores information about pharmacists.
  - `name`: CharField, name of the pharmacist.
  - `pharmacy`: ForeignKey, related pharmacy.
  - `phone_number`: CharField, phone number of the pharmacist.

### Accounts App

- **UserProfile**: Extends the default Django user model.
  - `user`: OneToOneField, related user.
  - `favorites`: ManyToManyField, related medications.

## Acknowledgements

Special thanks to:

- **PythonAnywhere Team** for providing the virtual environment for running linux, the free platform, and MySQL hosting.
- **Dr. Chuck Severance** from **University of Michigan** for the extensive computer science curriculum and guidance:
  - [Python for Everybody (py4e)](https://www.coursera.org/specializations/python) by Dr. Chuck Severance
  - [Django for Everybody (dj4e)](https://www.coursera.org/specializations/django) by Dr. Chuck Severance
  - [PostgreSQL for Everybody (PG4E)](https://www.coursera.org/specializations/postgresql-for-everybody) by Dr. Chuck Severance
  - [Web Design for Everybody (WD4E)](https://www.coursera.org/specializations/web-design) by Colleen Van Lent (Note: This course is not free)

This project was achieved through the extensive knowledge acquired from the above courses.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

The materials in Doctor Chuck's courses are available under a Creative Commons License to allow for teachers to make use of these materials in their own courses. Some of these courses are made available as part of a packaged curriculum to small Liberal Arts universities for direct adoption through Lower Cost Models for Independent Colleges Consortium (LCMC) and Rize Education.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
---

Feel free to reach out if you have any questions or suggestions!
