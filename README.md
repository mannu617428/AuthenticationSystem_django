# User Authentication System

A simple user authentication system built with Django.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

User Authentication System is a Django-based web application that provides user registration, login, and dashboard functionalities. It allows users to securely sign up for an account, log in with their credentials, and access their personalized dashboard based on their user role (admin or regular user).

## Features

- User registration: Users can sign up for an account by providing a username, email address, and password.
- User login: Registered users can log in to their accounts using their credentials.
- Role-based dashboard: Admin and regular users are directed to different dashboards upon login, each tailored to their respective roles.
- Admin dashboard: Admin users have access to administrative functionalities, such as managing users and site settings.
- Regular user dashboard: Regular users have access to features specific to their accounts, such as viewing profile information and managing preferences.

## Installation

To run the User Authentication System locally, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/user-authentication-system.git`
2. Navigate to the project directory: `cd user-authentication-system`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the application at [http://localhost:8000](http://localhost:8000)

## Usage

Once the application is running, follow these steps to use the User Authentication System:

1. Sign up for a new account by providing a username, email address, and password.
2. Log in with your credentials.
3. Depending on your user role (admin or regular user), you'll be directed to the corresponding dashboard.
4. Explore the features available on your dashboard, such as managing user accounts, viewing profile information, and updating preferences.

## Contributing

Contributions to the User Authentication System project are welcome! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).
