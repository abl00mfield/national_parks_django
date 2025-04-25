# ParkNotes

**Plan your adventures and record your memories!**  
ParkNotes is a web application that allows users to explore official U.S. National Parks, save parks to their personal collection, view park photo galleries, and add personal notes and ratings. From planning future adventures to remembering past trips, ParkNotes helps you create your own national park story.

---

## 📦 Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/abloomfield/national_parks_django.git
   cd parknotes
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   pipenv install
   ```

3. **Set up your environment variables:**

   Create a `.env` file in the project root containing:

   ```
   NPS_API_KEY=your_real_api_key_here
   ```

   > Get a free API key from the [NPS Developer Portal](https://www.nps.gov/subjects/developer/get-started.htm).

4. **Set up the PostgreSQL database:**

   - Ensure PostgreSQL is installed and running locally.
   - Create a database named `national_parks`:

   ```bash
   createdb national_parks
   ```

5. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **(Optional) Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser
   ```

---

## 🌲 Import National Parks Data

After setting up your database:

1. Open the Django shell:

   ```bash
   python manage.py shell
   ```

2. Run the import script:

   ```python
   from main_app.park_data_importer import import_parks
   import_parks()
   ```

✅ This will populate the database with official U.S. National Parks and their photo galleries.

---

## 🚀 Running the Development Server

Start the server:

```bash
python manage.py runserver
```
