# pygui

### Setup and Installing (new) Dependencies

For initial setup I've created a simple script, `./init.sh` (Script assumes it's ran from the root of the project). This will install all dependencies and create a virtual environment.
For adding new dependencies, add it to the `requirements.txt` file and run the `./init.sh` script.

To use dependencies in a folder, ensure theres a `\_\_init\_\_.py` file in the folder.

For removing now unused dependencies, remove it from `requirements.txt`. Now it won't be installed when running the init script again.
If you want to also remove it locally, remove the venv folder and re-run the `./init.sh` script.
