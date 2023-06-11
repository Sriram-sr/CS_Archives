This is basically a Python console application. This is implemented on the basis of client server architecture, where the server and client is connected through socket. Python socket library is used. 

It is a STUDENT MANAGEMENT SYSTEM. 

So far while login admin or normal user check is happened. Added features for admin like adding teachers and students, added logic for adding userprofile when we add student or teacher


Things to be done 

       Course API:
        Endpoint to list all courses
        Endpoint to create a new course
        Endpoint to retrieve details for a specific course
        Endpoint to update a course
        Endpoint to delete a course

    Student API:
        Endpoint to list all students
        Endpoint to create a new student
        Endpoint to retrieve details for a specific student
        Endpoint to update a student
        Endpoint to delete a student

    Enrollment API:
        Endpoint to list all enrollments
        Endpoint to create a new enrollment
        Endpoint to retrieve details for a specific enrollment
        Endpoint to update an enrollment
        Endpoint to delete an enrollment

Certainly, here's a list of APIs that could be made available to users in your student management system:

    Course API:
        Endpoint to list all available courses
        Endpoint to retrieve details for a specific course

    Student API:
        Endpoint to retrieve details for the current student
        Endpoint to update the details of the current student

    Enrollment API:
        Endpoint to list the courses that a student is enrolled in
        Endpoint to enroll in a new course        

Task idea,
- write a code for implementing bank server
- important actions such as deposit and withdraw should run as separate process
- datas can be send to common module(service manager) to store in json instead of db
- entire code should run as service instead of running as py file
- modules such as message queue shall be used send data module that stores
- systemevent module shall be used so that individual process need to be can be set  at the time it needed
- regex can be used to validate customer credentials

Any other ideas(other than bank server) can also be considered

Service manager module may have following functionalities,
- Should start all necessary process on running this service 
- should initiate all events and wait
- should cleanup the module temp data if any 
- should log all important steps to separate file