# Welcome To Class Central


### Development Environment Setup
Follow these steps to install dependencies and setup the development environment. Run these commands from the root of this project


### Postgres Docker Container
About 100mb of resources. Install docker-compose if not available
```
docker-compose up -d
```


### Backend Python Environment

#### Linux/Mac
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```


### Vue Apps
In each vue project/directory, run these commands
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

