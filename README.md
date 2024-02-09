# Map App Documentation (Work in Progress)
 Welcome to the documentation for the Map App! This document provides an overview of the features, functionality, and structure of the Map App project. Please note that this documentation is a work in progress and may be updated as the project evolves.

## Overview
The Map App is a mobile application designed to assist users in finding properties and obtaining information about them. It leverages geolocation services to provide users with accurate location data and offers a user-friendly interface for property search and exploration.

## Features
Current Features:
1. Property Search: Users can search for properties by location using the search field.
2. Property Display: The app displays properties on a map interface, allowing users to visualize their locations.
3. Property Details: Users can view detailed information about properties, including property type, size, bedrooms, bathrooms, availability, and price.
4. Contact Information: The app provides contact information for property owners or agents.
   
## Planned Features (Work in Progress):
1. Filtering: Implementation of filtering options to refine property search results.
2. User Authentication: Integration of user authentication for personalized experiences and property bookmarking.
3. Improved UI/UX: Enhancements to the user interface and experience for smoother navigation and interaction.
4. Chatbot Integration: Introduction of a chatbot feature to assist users with property-related inquiries.
5. Connection to a Database instead of using csv files (they are only used for testing purposes at this stage).
   
## Structure
- The Map App project follows a Model-View-Controller (MVC) architecture for better organization and separation of concerns. Here's a brief overview of each component:

- Model (model.py): Responsible for handling data-related tasks such as retrieving property information, finding property suggestions, and interacting with external services like geolocation APIs.

- View (view.py and view.kv): Contains the user interface elements and layout specifications. The view.py file defines the behavior of UI components, while the view.kv file provides the design specifications using the KivyMD language.

- Controller (main.py): Orchestrates the interaction between the model and view components, handling user input, updating the UI, and managing application state.

## Installation
To run the Map App locally, follow these steps:

1. Clone the project repository from GitHub.
2. Install the required dependencies listed in the requirements.txt file.
3. Execute the main.py file to launch the application.

If you have any feedback, suggestions, or questions about the Map App, please don't hesitate to reach out. Your input is valuable and helps me improve the app.
