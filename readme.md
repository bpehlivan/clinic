# Clinic Project
Doctor-Patient Appointment app to schedule working hours, timeslots and appointments.
## Running The Project
### Running With Docker
`Docker` and `docker-compose` is required to run it this way.
Copy `.env.example` as `.env` file to set environment variables.
```bash
cp .env.example .env
```
 
Environment variables are set to run within the container. You can change the variables as you wish.

Build the container:
```bash
make build
```

run the app:
```bash
make up
```

after this stage API should be available at `http://0.0.0.0:8000/api/v1/`

### Running On Local Environment
`Poetry` as package manager and `python==^3.12`is required for this project. Run Following commands to set up local python environment.
```bash
poetry install &&
poetry shell # create virtual env
```

Run database:
```bash
make db
```

Update `.env` file to access database from local environment:
```.env
POSTGRES_HOST=localhost
```

Then you can run the project:
```bash
python manage.py runserver
```

## Available APIs
Django Rest Framework's own api interface is available. Might be useful for ease-of-use.
### Doctors
#### Create Doctor
Endpoint:
```
POST /api/v1/doctors/
```
Request Body:
```json
{
  "full_name": "Dr. John Doe",
  "is_active": true,
  "start_hour": "08:00",
  "end_hour": "17:00",
  "appointment_slot_choices": "fifteen_minutes",
  "address": "123 Main St, Anytown, USA", // optional
  "phone_number": "+1234567890", // optional
  "email": "john.doe@example.com", // optional
  "license_number": "ABC123456", // optional
  "biography": "Experienced general practitioner", // optional
  "specialization": "family_medicine" // optional
}
```

#### List Doctors
Endpoint:
```
GET /api/v1/doctors/
```
Response:
```json
[
    {
        "id": "9fa65970-aecb-4ad2-bee2-cdbbe127bf27",
        "full_name": "John Doe",
        "specialization": "internal_medicine",
        "start_hour": "08:00:00",
        "end_hour": "17:00:00"
    },
    ...
]
```

#### Retrieve Doctor
Endpoint:
```
GET /api/v1/doctors/{doctor_id}/
```
Response:
```json
{
    "id": "9fa65970-aecb-4ad2-bee2-cdbbe127bf27",
    "full_name": "John Doe",
    "email": "john@doe.com",
    "phone_number": "+9054321456",
    "address": "random street",
    "license_number": "1234567",
    "biography": "random doctor",
    "is_active": true,
    "created_at": "2024-09-26T17:34:28.079481Z",
    "updated_at": "2024-09-26T17:34:28.079495Z",
    "specialization": "internal_medicine"
}
```

#### Get Available Appointment Timeslots for a Doctor
```
GET /api/v1/doctors/{doctor_id}/available_appointment_slots/?start_date=2024-10-05&end_date=2024-10-06
```
Response:
```json
[
    {
        "date": "2024-10-05",
        "available_timeslots": [
            "08.00",
            "08.15",
            "08.30",
            "08.45",
            "09.00",
            "09.15",
            "09.30",
            "09.45",
            "10.00",
            "10.15",
            "10.30",
            "10.45",
            "11.00",
            "11.15",
            "11.30",
            "11.45",
            "12.00",
            "12.15",
            "12.30",
            "12.45",
            "13.00",
            "13.15",
            "13.30",
            "13.45",
            "14.00",
            "14.15",
            "14.30",
            "14.45",
            "15.00",
            "15.15",
            "15.30",
            "15.45",
            "16.00",
            "16.15",
            "16.30",
            "16.45"
        ]
    }
]
```

### Appointments
#### List Appointments  
Endpoint: 
```
GET /api/v1/appointments/
```
Response:
```json
[
  {
    "doctor": "4df67d17-5100-4779-8dab-a32999733167",
    "appointment_start": "2024-09-27T10:00:00Z",
    "appointment_end": "2024-09-27T10:15:00Z",
    "patient_full_name": "buraky",
    "patient_identity_number": "1234244356"
  },
  ...
]
```

#### Create Appointment
Endpoint:
```
POST /api/v1/appointments/
```

Request Body:
```json
{
  "doctor": "9fa65970-aecb-4ad2-bee2-cdbbe127bf27",
  "patient_full_name": "Burkay Pehlivan",
  "patient_identity_number": "1234567",
  "start_at": "2024-09-27T10:00:00Z"
}
```