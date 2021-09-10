if [ -f "venv/deps.done" ]; then
	echo "venv already setup"
else
	python3 -m venv venv
	touch venv/deps.done
fi

venv/bin/pip3 install -r requirements.txt
