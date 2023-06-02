# Flight Reservation System

The Flight Reservation System is a Python application developed using the tkinter library for the user interface. It provides functionalities for searching flights, booking them, and canceling reservations. The project utilizes the pyodbc library for database connectivity.

## Features

The Flight Reservation System offers the following key features:

1. **Search Flight**: Users can search for available flights based on various criteria such as departure location, destination, date, and the number of passengers.

2. **Book Flight**: Once users have found a suitable flight, they can proceed with the booking process. They need to provide passenger details and make the necessary payment to confirm the reservation.

3. **Cancel Reservation**: In case users need to cancel their reservation, they can do so through the system by providing the reservation ID.

## Installation

To use the Flight Reservation System, follow the steps below:

1. Clone the repository to your local machine or download the project files.

2. Install the required fonts. The "Fonts" folder is available in the project repository and contains the "Poppins" and "Product Sans" fonts. Install these fonts on your system.

3. Install the necessary dependencies. Use the following command to install the required packages:

   ```
   pip install pyodbc
   ```

4. Set up the database by executing the SQL script provided in the "Project_Schema.sql" file. This script will create the required tables and relationships in the database.

5. Launch the application by running the "Project.py" file using Python. Make sure you have the correct Python environment and dependencies installed.

## Database Connection

To connect your database first change the `Server = "--YOUR SERVER NAME HERE--" ` with your pc server in the `project.py` file 

```
connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-4LORV5Q\SQLEXPRESS;' 
'Database=FRS;' 'Trusted_connection=yes;')
```

The above code is where you going to change the Server name!!

## Usage

After launching the Flight Reservation System application, you will be presented with a user-friendly interface that allows you to interact with the system. The application provides the following functionality:

1. **Search Flight**: Click on the "Search Flight" button to access the flight search form. Fill in the necessary information, such as departure location, destination, date, and the number of passengers. Click "Search" to view the available flights that match your criteria.

2. **Book Flight**: Once you have found a suitable flight from the search results, select it and click on the "Book" button. Provide the required passenger details, including name, contact information, and payment details. Confirm the booking to complete the reservation process.

3. **Cancel Reservation**: To cancel a reservation, click on the "Cancel Reservation" button. Enter your reservation ID and submit the cancellation request. The system will process the cancellation and provide a confirmation message.

## Database Schema

The Flight Reservation System utilizes a database to store flight, passenger, reservation, and payment information. The structure of the database is represented by the following diagram:

![Database Diagram](Database%20Diagram.png)

The diagram illustrates the relationships between the various tables in the database, ensuring data integrity and consistency.

## Interface Pictures

The "Interface Pictures" folder contains screenshots of the Flight Reservation System application. These images provide visual representations of the user interface and demonstrate how to interact with the system effectively.

## Contributing

Contributions to the Flight Reservation System are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.

## License

The Flight Reservation System is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute the codebase according to the terms of the license.

## Acknowledgments

- This Flight Reservation System is inspired by various airlines reservation systems and online resources

Thank you for using the Flight Reservation System! We hope it meets your requirements and provides a seamless flight booking experience.
