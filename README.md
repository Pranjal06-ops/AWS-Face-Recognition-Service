🚀 AWS Face Recognition Service

A **ready-to-run REST API** for face recognition built with **FastAPI**, featuring a **dummy CNN model**, Docker support, and AWS S3 & SQS integration placeholders.  
Structured for **scalability**, **cloud deployment**, and **hands-on experimentation** with backend and cloud technologies.  

---

✨ Features

- 🖼 **REST API**: `/face/recognize` endpoint for image upload  
- 🤖 **Dummy CNN model**: always predicts `class 1` (replaceable with a real model)  
- 🐳 **Dockerized**: containerized for easy deployment  
- ☁️ **AWS placeholders**: S3 for image storage & SQS for queue processing  
- ✅ **Unit tests** included for quick verification  
- ⚡ **FastAPI-powered**: lightweight, high-performance backend  

---

⚙️ Quick Start

1️⃣ Install Dependencies

2️⃣ Run Locally
uvicorn app.main:app --reload

Test the API with a sample image: curl -X POST "http://127.0.0.1:8000/face/recognize" -F "file=@tests/sample_face.jpg"

Expected output: { "predicted_class": 1 }

3️⃣ Run with Docker
docker build -t face-recognition-service ./docker
docker run -p 8000:8000 face-recognition-service
Access API at: http://localhost:8000/face/recognize

📂 Folder Structure
app/        → FastAPI app, models & routes
docker/     → Dockerfile
scripts/    → Dummy training script
tests/      → Unit tests
README.md
requirements.txt
.gitignore

☁️ AWS Integration (Placeholders)
S3 upload: app/utils.py
SQS queue: app/utils.py
Use .env to securely load AWS credentials:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
Replace dummy functions with real AWS logic when deploying.

🔮 Future Enhancements

Replace dummy CNN with a trained model for real predictions 🤖
Async processing for high-concurrency API requests ⚡
Deploy to AWS EC2, Lambda, or Elastic Beanstalk 
Store prediction results in a database 
Logging & monitoring with AWS CloudWatch 📊

🏆 Author
Pranjal Haldankar
Master’s IT Student, UMass Boston

Topics: fastapi | python | face-recognition | docker | aws | backend | REST API | machine-learning



```bash
pip install -r requirements.txt
