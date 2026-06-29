```text
python3 -c "
import os, subprocess
for root, dirs, files in os.walk('.'):
    if 'app.py' in files and '.venv' not in root:
        os.chdir(root)
        subprocess.run(['python3', '-m', 'streamlit', 'run', 'app.py', '--server.port', '8501', '--server.address', '0.0.0.0'])
        break
"
```
