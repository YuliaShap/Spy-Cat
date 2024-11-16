# Spy-Cat

Overview
The Spy Cat Agency Management System is a CRUD application designed to streamline the processes of managing spy cats, their missions, and associated targets. This project demonstrates the ability to create RESTful APIs, interact with a SQL-like database, and integrate third-party services.

The system allows the agency to efficiently handle spy cat records, assign and manage missions, and track mission progress, ensuring smooth operations for their covert activities.

<b>Features</b><p>
Spy Cats<p>
1. Create a Spy Cat: 
2. Add a new spy cat with the following attributes:
   - name: The cat's name.
   - years_of_experience: The cat's years of spying experience.
   - breed: The breed of the cat (validated with TheCatAPI).
   - salary: The cat's salary.
3. Update a Spy Cat: Modify an existing spy cat's salary.
4. Delete a Spy Cat: Remove a spy cat from the system.
5. List Spy Cats: Retrieve all spy cats.
6. Get a Single Spy Cat: View detailed information about a specific spy cat.<p>

Missions and Targets<p>
1. Create a Mission:
- Assign a mission to a cat with a list of targets.
- Targets include:
   - name
   - country
   - notes
   - is_complete
- Each mission can have between 1 and 3 targets.
2. Update Mission Targets:
- Update Notes: Modify notes for a target.
  - Notes cannot be updated if the target or mission is marked as complete.
- Mark Target as Complete: Finalize a target's status.
3. Mark Mission as Complete: Once all targets are completed, the mission can be marked as finished.
4. Delete a Mission:
- Missions cannot be deleted if assigned to a spy cat.
5. Assign a Cat to a Mission: Link a mission to an available spy cat.
6. List Missions: Retrieve all missions.
7. Get a Single Mission: View detailed information about a specific mission.


<b>Technologies Used</b><p>
- Framework: Django with Django REST Framework
- Database: PostgreSQL
- Third-party Integration: TheCatAPI for validating cat breeds.


<b>Installation and Setup</b><p>
1. Clone the Repository<p>
git clone https://github.com/YuliaShap/Spy-Cat.git<p>
cd spy-cat-agency<p>

2. Create and Activate a Virtual Environment<p>

   python3 -m venv .venv<p>
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate<p>

3. Install Dependencies<p>
pip install -r requirements.txt

4. Run Migrations<p>
python manage.py migrate
5. Start the Development Server<p>
python manage.py runserver<p>
6. Access the API<p>
Visit: http://127.0.0.1:8000

<b>Postman Collection</b><p>
A detailed Postman collection with all endpoints is available here<p>
<a>https://blue-robot-243087.postman.co/workspace/Team-Workspace~863c048b-8dad-4894-8171-f910094b45a0/collection/21778755-a68e23df-c1b3-46e1-a905-f5d68bb65075?action=share&creator=21778755</a>

<b>Notes</b><p>
- Validation: All request bodies are validated to ensure correctness. Meaningful status codes and error messages are returned for invalid data.
- Third-party API Integration: Cat breeds are validated using real-time data from TheCatAPI.
- Postman: Test and explore the API with the provided Postman collection.


<b>If you have any questions or feedback, feel free to reach out via the repository issues or contact me directly. Thank you for reviewing the project!</b><p>
