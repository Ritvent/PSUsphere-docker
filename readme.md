# CC6 Docker Configuration


Step-by-step guide to setup and run your Django app with Docker either as a **Developer** or **Client**.

## Prerequisites

- Docker Desktop installed
- Docker Hub account (for development machine only)

---

## For Development Machine (Building & Pushing Image)

### Step 1: Install Docker
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Verify installation:
```bash
   docker --version
   ```

### Step 2: Login to Docker Hub
```bash
docker login
```
Enter your Docker Hub username and password.

### Step 3: Build the Docker Image
```bash
docker build -t my-django-app:latest .
```

### Step 4: Tag the Image
Replace `yourusername` with your Docker Hub username:
```bash
docker tag my-django-app:latest yourusername/django-app:latest
```

### Step 5: Push to Docker Hub
```bash
docker push yourusername/django-app:latest
```

### Step 6: Run Locally (Optional)
```bash
docker-compose up -d
```
Access the app at: http://localhost:8000

### Step 7: Stop the Application
```bash
docker-compose down
```

---

## For Client Machine (Pulling & Running Image)

### Step 1: Install Docker
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Verify installation:
   ```bash
   docker --version
   ```

### Step 2: Create Project Folder
Create a new folder and navigate into it:
```bash
mkdir psusphere-docker
cd psusphere-docker
```

### Step 3: Create docker-compose.yml
Copy the `docker-compose.yml` file from the `/for_client/` folder into your project folder.

**Important:** Update the image name in `docker-compose.yml`:
```yaml
image: yourusername/django-app:latest
```
Replace `yourusername` with the **developer's machine** Docker Hub username.

### Step 4: Pull and Run the Application
```bash
docker-compose up -d
```

### Step 5: Access the Application
Open your browser and go to: http://localhost:8000

### Step 6: Create Admin User (First Time Only)
```bash
docker-compose exec web python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 7: View Logs (Optional)
```bash
docker-compose logs -f web
```
Press `Ctrl + C` to exit logs.

### Step 8: Stop the Application
```bash
docker-compose down
```

---

## Updating the Application

### On Development Machine:
1. Make your code changes
2. Rebuild the image:
   ```bash
   docker-compose build
   ```
3. Push the new version:
   ```bash
   docker push yourusername/django-app:latest
   ```

### On Client Machine:
1. Pull the latest version:
   ```bash
   docker-compose pull
   ```
2. Restart the application:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

---

##  Useful Commands

| Command | Description |
|---------|-------------|
| `docker-compose up -d` | Start the application in background |
| `docker-compose down` | Stop the application |
| `docker-compose logs -f web` | View application logs |
| `docker-compose ps` | Check running containers |
| `docker-compose exec web python manage.py migrate` | Run database migrations |
| `docker images` | List all Docker images |
| `docker ps` | List running containers |

---

