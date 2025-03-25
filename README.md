🌍 Translate App
Translate App is an English-to-Vietnamese translation application powered by a Transformer model. The project consists of:

Backend: An API for translation processing using PyTorch (FastAPI).

Frontend: A web interface built with React, communicating with the API via axios.

📂 Project Structure
bash
Copy
Edit
translate-app/
├── backend/        # Backend (FastAPI + PyTorch)
│   ├── app.py      # Main backend file
│   ├── vocab/      # Vocabulary files
│   │   ├── vocab_en.json
│   │   └── vocab_vi.json
│   ├── src/        # Source code
│   │   └── ...
├── frontend/       # Frontend (React)
│   ├── src/        # React source code
│   ├── package.json  # Frontend dependencies
│   └── ...
└── README.md       # Setup and usage guide
🔗 Model Checkpoint:
[Download here](https://surl.li/deogzi)

🛠 Installation & Setup
1️⃣ Setting up Backend
📌 Prerequisite: Install Miniconda/Anaconda.

Steps to set up the environment:

sh
Copy
Edit
# Navigate to the backend directory
cd backend

# Create a Conda environment
conda create --name translate_app python=3.11 -y

# Activate the environment
conda activate translate_app

# Set environment variable (Windows)
set KMP_DUPLICATE_LIB_OK=TRUE

# Install required dependencies
conda install -c pytorch torchdata=0.5.1
conda install -c conda-forge portalocker=2.7.0
conda install -c pytorch torchtext=0.16.0
2️⃣ Setting up Frontend
📌 Prerequisite: Install Node.js.

Steps to set up the environment:

sh
Copy
Edit
# Open Visual Studio Code (VS Code)
# Navigate to the frontend folder in VS Code

# Open a terminal inside VS Code

# Install dependencies
npm install

# Install axios for API calls
npm install axios
🚀 Running the Application
🔥 Start Backend
sh
Copy
Edit
# Navigate to the backend directory
cd backend

# Activate the Conda environment
conda activate translate_app

# Run the backend server
python app.py
🎨 Start Frontend
sh
Copy
Edit
# Open VS Code
# In the terminal, start React
npm start
📝 Notes
Make sure to activate the Conda environment before running the backend.

Ensure the backend is running before launching the frontend.

If necessary, update the API URL in the frontend (src/api.js or similar) to match the correct backend address, e.g., http://localhost:8000/api/....

